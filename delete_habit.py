import csv
from datetime import datetime

def delete_habit(csv_file_path):
    """
    This function allows the user to delete a column from the CSV file, except for the first column.
    It prompts the user to select a column and removes it from the list.
    """

    # Read the CSV file to get the current data
    with open(csv_file_path, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Check if there are enough rows to proceed
    if len(rows) < 2:
        print("The CSV file doesn't have enough data to delete a column.")
        return

    # The first row contains headers, exclude the first column ("Datum")
    headers = rows[0][1:]  # Skip the first column (Datum)
    
    # If there are no columns to delete, return early
    if not headers:
        print("No columns to delete.")
        return

    # Prompt the user to choose which column to delete (excluding the first column)
    print("Available columns to delete:")
    for i, header in enumerate(headers, start=1):
        print(f"{i}: {header}")
    
    try:
        column_to_delete = int(input("Enter the column number to delete: "))
        
        # Validate input
        if column_to_delete < 1 or column_to_delete > len(headers):
            print("Invalid choice. No column deleted.")
            return
        
        # Calculate the actual column index in the rows (remember to add 1 to account for "Datum")
        column_index = column_to_delete

        # Delete the selected column from each row
        for row in rows:
            del row[column_index]

        # Write the updated rows back to the CSV file
        with open(csv_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f"Column '{headers[column_to_delete - 1]}' deleted successfully.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
