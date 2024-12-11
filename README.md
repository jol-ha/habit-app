# Habit Tracking App

## QUICKSTART 
    - ensure that pandas is installed
    - enter in the Jupyter-Console:


import habit_tracker

habit_tracker.habit()

follow the instructions, for testing purpose you can also enter "tdf" or "test_data_file.csv"
    when asked for a data storage file

## Legal Notice
This app is a personal project created for educational purposes. Use at your own risk.
## Background
The Habit App was developed as part of a Python course at IU Academy in December 2024. The primary objective was to gain hands-on experience with Python programming.
## Requirements
    • Python 3.6 or higher
    • pip to install dependencies (specifically pandas)

## Setup Instructions
    1. Download the repository from GitHub as a ZIP file.
    2. Extract the ZIP file to a specific folder on your computer.
    3. Open a terminal window and navigate to the folder where you saved the habit_app.
    4. Install pandas by running the following command: pip install pandas
    5. Launch Python by typing python3 in the terminal.
## User Guide
    RUN THE APP:
	- In the Python shell, import the main module by entering: "import habit_tracker"
	- Start the app by running: "habit_tracker.habit()"
    - Follow the on-screen instructions to interact with the app.
    APP TESTING
    You can use the "test_data_file.csv" to test the app's functionality. This test file contains sample data that can be used to check the entry, calculation, and deletion features.

## Notes:
    Make sure that the csv file is properly initialized before you attempt to enter or calculate data.
    The app currently supports up to 6 habits.

## APP STRUCTURE

The app consists of several Python modules and CSV files that handle different aspects of habit tracking. Please visit the [App-Struktur](./structure.txt) file to have an overview of the app's structure.



1. habit_tracker.py

    This is the main entry point for the app.
    You can specify a CSV file to serve as the storage for your raw habit data.
    The app allows you to choose from the following options:
        [i] Initiation
        [e] Entry
        [c] Calculation
        [d] Delete Habit

1.1 initiation.py

    Start by running habit_tracker.py as described in the User Guide.
    Choose option [i] to initialize the app and enter your habits.
    Follow the instructions on the screen:
        You can define 6 habits that you want to track.
        For each habit, specify if it's tracked daily (d) or weekly (w).
    The app will save this data in a CSV file for future tracking.

1.2 entry.py
    
    Start by running habit_tracker.py as described in the User Guide.
    Choose option [e] for habit entry.
    You will be prompted to enter the date when the habit was tracked.
    For each habit, you will indicate whether you completed it by entering:
        y for Yes
        n for No
    For weekly habits, you should only enter y or n once per week, while daily habits can be tracked every day using d for no statement.
    All data will be stored in the CSV file that was created during the initialization process (via initiation.py).

1.3 calculation_daily/weekly.py

    Start by running habit_tracker.py as described in the User Guide.
    Choose option [c] to evaluate your habit tracking data.
    You will get an overview of your CSV file:
        Count of y and n for each daily habit.
        Percentage of y responses and the longest streak of y entries.
        Similar statistics for weekly habits.
    elaborate_weekly.py is a helper module that supports the calculation_weekly.py functionality.

1.4 delete_habit.py

    Start by running habit_tracker.py as described in the User Guide.
    Choose option [d] to remove a habit from the app.
    Follow the prompts to select and delete a habit.


```python

```
