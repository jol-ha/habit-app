import csv
import pandas as pd

def calculate(csv_file_path):
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Extract the 'date' column (assuming there's a column named 'date')
    date_column = 'date'  # Adjust this name if needed to match your actual column name
    if date_column not in df.columns:
        print(f"Warning: Column '{date_column}' not found in the data.")
        return
    
    # Check each column in the first row beyond the header (i.e., row 0) for 'Weekly'
    weekly_columns = [col for col in df.columns if str(df[col].iloc[0]).lower() == 'weekly']
    
    # Optionally, save these groups to a new CSV file
    weekly_df = df[[date_column] + weekly_columns]  # Ensure 'date' comes first
    
    # Save the DataFrame to a new CSV file
    weekly_df.to_csv('weekly_columns_file.csv', index=False)
    
    # Initialize a dictionary to store the counts
    weekly_counts = {}
   
    # Counting 'y' and 'n' for Weekly columns
    for col in weekly_df.columns:
        if col == date_column:
            continue  # Skip the date column in counting
        y_count = weekly_df[col].str.lower().eq('y').sum()
        n_count = weekly_df[col].str.lower().eq('n').sum()
        total_count = y_count + n_count
        y_percentage = (y_count / total_count) * 100 if total_count > 0 else 0  # Avoid division by zero
           
        weekly_counts[col] = {
            'y': y_count,
            'n': n_count,
            'percentage_y': y_percentage,
        }
        
    # Output the counts and percentages for Weekly columns
    print("WEEKLY HABIT COUNTS:\n")
    for col, count in weekly_counts.items():
        print(f"Habit '{col:15}':\n  'y' count: {count['y']}, 'n' count: {count['n']}")
        print(f"  'y' percentage: {count['percentage_y']:>20.2f}%")
        print()
    
    # Return the total y and n, and give the percent and the max_streak for weekly
    total_y_count = 0
    total_n_count = 0
    
    for col in weekly_df.columns:
        if col == date_column:
            continue  # Skip the date column in counting
        total_y_count += weekly_df[col].str.lower().eq('y').sum()
        total_n_count += weekly_df[col].str.lower().eq('n').sum()
    
    # Output the total sum of "y" and "n"
    print(f"Total 'y' count across all weekly habits: {total_y_count}")
    print(f"Total 'n' count across all weekly habits: {total_n_count}")
    
    # Optional: Calculate the percentages
    total_count = total_y_count + total_n_count
    if total_count > 0:
        total_y_percentage = (total_y_count / total_count) * 100
        print(f"Percentage of successful finishing the weekly tasks: {total_y_percentage:.2f}% \n")
    else:
        print("No 'y' or 'n' entries found across all weekly columns.")
