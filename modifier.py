import json
from datetime import datetime
import csv
from os import path

class Holder:

    def __init__(self, month, amount):
        self.month = month
        self.amount = amount

    def turn_to_dict(self):
        return {
            'month': self.month,
            'amount': self.amount
        }
        
def return_lst():
    with open('tracker.csv') as f:
        lst = []
        reader = csv.DictReader(f)
        
        for i in reader:
            lst.append(i)

        return lst

lst = return_lst()


def modify():

    date = datetime.now().astimezone()

    MONTHS = {
        '1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
        '5': 'May','6': 'Jun', '7': 'Jul','8': 'Aug',
        '9': 'Sep','10': 'Oct','11': 'Nov','12': 'Dec'
    }

    file_exists = path.isfile('monthly.csv')

    with open('date.json') as f:

        total = 0
        reader = json.load(f)

        if str(date.month) not in reader['month']:

            reader = {
                'month': 
                {
                    f'{date.month}': MONTHS[f'{date.month}']
                }
            }

            with open('date.json', 'w') as file:
                json.dump(reader, file ,indent=4)

            with open('category.json') as f:
                r = json.load(f)

                currency = r['currency']['type']
                final_amount = r['total_money']['t']

                for i in r:
                    try:
                        total += r[i]['amount']
                    except KeyError:pass

                r = {
                    'currency': {
                        'type': currency
                    },
                    'total_money':{
                        't':final_amount
                    }
                }

                with open('category.json', 'w') as f:
                    json.dump(r, f, indent=3)

                with open('monthly.csv', 'a', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=['month','amount'])

                    if not file_exists:
                        writer.writeheader()
                    if date.month == '1': 
                        data = Holder(MONTHS['12'], total)# if it is January then the in monthly.csv will be written Dec.
                    else: 
                        data = Holder(MONTHS[str(date.month-1)], total)#otherwise just the previous month
                    writer.writerow(data.turn_to_dict())

def track_limit():

    with open('configs.json') as f:
        reader2 = json.load(f)

    user_limit = reader2['user']['limit']
    if len(lst) > user_limit:
        del lst[0:len(lst)-user_limit-1]


def change_limit():
    with open('configs.json') as f:
        r = json.load(f)

    current_limit = r['user']['limit']
    user = int(input(f'Enter the new limit (current limit -> {current_limit}): '))

    if user < current_limit and len(lst) > user:
        del lst[0:len(lst)-user]

    r = {
        'user': {'limit': user}
    }

    with open('configs.json', 'w') as f:
        json.dump(r,f,indent=3)

with open('tracker.csv', 'w', newline='') as smth:
    writer = csv.DictWriter(smth, fieldnames=['category', 'amount', 'date'])
    writer.writeheader()
    for l in lst:
        writer.writerow(l)


def negative_checker():
    with open('category.json') as f:
        reader = json.load(f)

    if reader['total_money']['t'] < 0:

        print(f'Looks like your balance has gone negative! ({reader['total_money']['t']} {reader['currency']['type']})')

        while True:

            y_n = input('Change it? y/n: ')

            if y_n == 'y':
                new_amount = float(input('Enter the amount you currently have: '))
                reader['total_money']['t'] = new_amount
                break

            elif y_n not in ('y', 'n'):
                print('The response needs to be y or n!')
                continue
            
            else:break
    with open('category.json', 'w') as f:
        json.dump(reader,f, indent=3)