import csv
from datetime import datetime

# Initialize an empty list to store entries
my_list = []

def enter_date(): 
    """Prompt the user to enter a date or use the current date.
    
    The user can input a specific date in the format YYYY-MM-DD or press return
    to use the current date. The date is then added to the list 'my_list' and returned.
    """
    while True:
        date = input("Enter a date (YYYY-MM-DD) or take the actual one by pressing return: ")
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")  # Use the current date if no input is given
            break
        else:
            # Validate the entered date format
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    my_list.append(date)
    return date
    
        
def enter(csv_file_path):
    """Allow the user to input daily or weekly task statuses, and append the entries to a CSV file.
    
    This function handles user input for six tasks, asking whether each task is done ('y' for yes, 
    'n' for no, 'd' for done) and appends the data (including date) to the given CSV file.
    
    - The user will first enter a date (either custom or current).
    - Then, they will be prompted to enter a status for each of six tasks, selecting 'y', 'n', or 'd'.
    - If the input is valid, the corresponding entry is appended to a list, which is later written to the CSV.
    - If an invalid input is entered, the process is aborted, and the list is cleared.
    """
    
    # Clear the list at the start of the function to avoid appending old data
    my_list.clear()

    # Prompt for date input and store it
    enter_date()

    # Explain the input format for the user
    print("\nFollowing entries allow y/n/d meaning yes, no, done. \n"
          "Explanation: daily tasks should be entered every day. \n"
          "WEEKLY tasks should be ENTERED just ONCE PER WEEK as y or n. \n"
          "The other six entries can be made by 'd' for already done.")

    # Open the CSV file in read mode to access headers and first data row
    try:
        with open(csv_file_path, mode="r") as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Read the header row
            next(csv_reader)  # Skip the first data row (we're appending a new row)

    except FileNotFoundError:
        print(f"The file '{csv_file_path}' was not found. Please ensure it exists.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Loop through the first six tasks and prompt for user input
    for x in range(1, len(headers)):  # Dynamically adapt based on the number of headers
        while True:
            entry = input(f"For {headers[x]}, please enter y/n/d: ").lower()

            # Handle valid entries and append them to the list
            if entry in ["y", "n", "d"]:
                my_list.append(entry)
                print("Entry appended to the list.")
                break  # Break the loop to move on to the next task
            else:
                print("Invalid entry. Please enter 'y', 'n', or 'd'.")

    # Output the list of entries for verification
    print(my_list)
    
    # Append the entries (including the date) to the CSV file
    try:
        with open(csv_file_path, mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(my_list)  # Write the new row with date and entries
            print(f"Data successfully added to {csv_file_path}")
    
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

    # Clear the list after appending to the CSV
    my_list.clear()
