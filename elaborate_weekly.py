import pandas as pd
import csv

def elab(): #elaborate
    """
    This function processes a CSV file containing weekly habit data, performs data cleaning, 
    and calculates the longest streak of consecutive 'y' (yes) entries for each habit.

    Steps:
    1. Reads the weekly habit data from a CSV file named 'weekly_columns_file.csv'.
    2. Replaces any 'd' (done) entries with NaN to represent missing values.
    3. Drops rows with any NaN values (i.e., removes incomplete entries).
    4. Displays the cleaned DataFrame for review.
    5. Saves the cleaned data to a new CSV file called 'cleaned_data.csv'.
    6. Calculates and prints the maximum 'y' streak (consecutive 'y' entries) for each habit.
    """
    
    # Specify the path to the CSV file containing the weekly habit data
    csv_weekly = "weekly_columns_file.csv"
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_weekly)
    
    # Replace all occurrences of 'd' with NaN (Not a Number) to mark as missing
    df.replace('d', pd.NA, inplace=True)
    
    # Drop rows containing NaN values (incomplete data)
    df.dropna(inplace=True)
    
    # Save the cleaned DataFrame to a new CSV file
    df.to_csv('cleaned_data.csv', index=False)
    
    def max_y_streak(column):
        """
        This helper function calculates the longest streak of consecutive 'y' (yes) entries
        in a given column.

        Parameters:
        - column (pandas Series): A column containing 'y', 'n', and possibly other values.
        
        Returns:
        - max_streak (int): The maximum number of consecutive 'y' entries.
        """
        
        max_streak = 0
        current_streak = 0
        
        # Iterate over the values in the column to calculate the streaks
        for value in column:
            if str(value).strip().lower() == 'y':  # Check if the value is 'y'
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 0  # Reset the streak if 'n' or other value is found
        
        return max_streak
    
    # Calculate and print the maximum 'y' streak for each habit column
    
    for i in range(1, len(df.columns)):  # skip first lane
        col = df.columns[i]
        max_streak = max_y_streak(df[col])
        print(f"Max 'y' streak for habit '{col:>15}': {max_streak}")

