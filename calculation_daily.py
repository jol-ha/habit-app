import csv
import pandas as pd

def calculate(csv_file_path):

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Extract the 'date' column and the columns with 'daily' values
    date_column = df['date']  # Assuming 'date' is the name of the date column
    daily_columns = [col for col in df.columns if str(df[col].iloc[0]).lower() == 'daily']
    
    # Create a new DataFrame with the date column at the first position
    daily_df = df[daily_columns]
    result_df = pd.concat([date_column, daily_df], axis=1)

    # Save the result into a new CSV file
    result_df.to_csv('daily_column.csv', index=False)
    
    # Initialize a dictionary to store the counts
    daily_counts = {}
    
    # Function to calculate the max streak
    def calculate_streaks(column):
        max_streak = 0
        current_streak = 0
        
        # Iterate through the values of the column
        for value in column:
            if str(value).lower() == 'y':
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 0
    
        return max_streak
    
    # Count 'y' and 'n' in daily columns
    for col in daily_df.columns:
        y_count = daily_df[col].str.lower().eq('y').sum()
        n_count = daily_df[col].str.lower().eq('n').sum()
        total_count = y_count + n_count
        y_percentage = (y_count / total_count) * 100 if total_count > 0 else 0  # Avoid division by zero
        max_streak = calculate_streaks(daily_df[col])
    
        daily_counts[col] = {
            'y': y_count,
            'n': n_count,
            'percentage_y': y_percentage,
            'max_streak': max_streak
        }
        
    # Output Daily-Spalten
    print("DAILY HABIT COUNTS:\n")
    for col, count in daily_counts.items():
        print(f"Habit '{col:15}':,\n  'y' count: {count['y']}, 'n' count: {count['n']}")
        print(f"  'y' percentage: {count['percentage_y']:>20.2f}%, streak: {count['max_streak']}")
        print()
    
    # Return the total y and n, and give the percent and the max_streak for daily
    total_y_count = 0
    total_n_count = 0
    
    for col in daily_df.columns:
        total_y_count += daily_df[col].str.lower().eq('y').sum()
        total_n_count += daily_df[col].str.lower().eq('n').sum()
    
    # Output total amount "y" and "n"
    print(f"Total 'y' count across all daily habits:  {total_y_count}")
    print(f"Total 'n' count across all daily habits:  {total_n_count}")
    
    # Optional: Calculate percentages
    total_count = total_y_count + total_n_count
    if total_count > 0:
        total_y_percentage = (total_y_count / total_count) * 100
        print(f"Percentage of fulfilling the daily tasks: {total_y_percentage:.2f}%\n\n")
    else:
        print("No 'y' or 'n' entries found across all daily columns.")
