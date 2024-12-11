import csv
from datetime import datetime

def add_habit(csv_file_path):
    """
    This function initializes the habit tracking app by allowing the user to define
    6 habits and specify their frequencies (daily or weekly).

    - The user is prompted to enter the name of each habit.
    - For each habit, the user specifies how often it should be tracked: daily or weekly.
    - The habits and their frequencies are saved to a CSV file with the current date.
    """

    # Create empty lists to store habit names and their frequencies
    habit_names = []
    frequencies = []

    # Get the current date for the CSV file (used as the header and for habit tracking)
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Loop until exactly 6 habits have been entered
    while len(habit_names) < 6:
        # Prompt user for habit name
        habit_name = input(f"Enter the name of habit {len(habit_names) + 1}: ")

        # Ensure user inputs a valid frequency (daily or weekly)
        while True:
            frequency_input = input(f"How often should {habit_name} occur? (d for daily, w for weekly): ").lower()

            # Validate and convert the short input into full frequency names
            if frequency_input in ["d", "daily"]:
                frequency = "Daily"
                break
            elif frequency_input in ["w", "weekly"]:
                frequency = "Weekly"
                break
            else:
                print("Invalid input! Please enter 'd' or 'daily' for daily, 'w' or 'weekly' for weekly.")

        # Add the habit name and corresponding frequency to their respective lists
        habit_names.append(habit_name)
        frequencies.append(frequency)

    # Open the CSV file in write mode to store habit data
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write a header row with "date" for date and the names of the habits
        header = ["date"] + habit_names
        writer.writerow(header)

        # Write the second row with the current date and the habit frequencies
        data_row = ["Interval"] + frequencies
        writer.writerow(data_row)

    # Confirm successful creation of the CSV file
    print(f"CSV file '{csv_file_path}' created successfully.")




