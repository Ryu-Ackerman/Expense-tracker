## Expense Tracker
A CLI application for tracking personal finances. It provides detailed tracking and automated monthly summaries.

### Features
*   Log new expenses with a category and amount.
*   Add funds to the total balance.
*   Calculate and display average spending over a specified number of days.
*   Automatically archives the previous month's total spending into `monthly.csv` at the start of a new month.
*   Manages a configurable history limit for transactions in `tracker.csv` to keep the log size manageable.
*   Checks for a negative balance on startup and prompts for correction.
*   Supports setting a custom currency.

### Usage
-   **Log a new expense:**
    ```sh
    python app.py new
    ```
-   **Add funds to your balance:**
    ```sh
    python app.py add
    ```
-   **Calculate average spending:**
    ```sh
    python app.py average
    ```
-   **Change currency:**
    ```sh
    python app.py currency -c
    ```
-   **Change transaction history limit:**
    ```sh
    python app.py limit -c
    ```
-   **View all commands:**
    ```sh
    python app.py -h
    ``` 