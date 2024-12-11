def habit():
    # Print a brief guide on how to use the app
   
    """
    Function to interact with the user and guide them through various options:
    1. Initiate a habit.
    2. Log daily or weekly progress.
    3. View habit progress summary.
    4. Delete a habit from the list.
    """
    
    # Prompt the user for a filename to store data (default is 'raw_data.csv')
    csv_file_path = input("Provide a filename for storing data (default: raw_data.csv): ")
    # For testing the program you can use tdf to work with the test data-file
    if csv_file_path=="tdf": #tdf as short for test_data_file.csv
        csv_file_path ="test_data_file.csv"    
    
    # If the user doesn't provide a filename, use the default
    if not csv_file_path:
        csv_file_path = "raw_data.csv"
    
    print(f"Using the file: {csv_file_path}")
    
    print("""
    Recommendations:
    1. Use "i" to initiate tasks.
    2. Use "e" for entry to log daily/weekly progress.
    3. Use "c" for calculate to view a progress summary.
    4. Use "d" to delete a habit.
    """)
    
    # Ask the user to user_choice between initiation, entry, or calculation
    user_choice = input("press the key, either: [i],[e],[c], or [d]: \n\n")
    
    # Execute the corresponding functionality based on user input
    if user_choice == "i":
        print("You have chosen initiation.\n")
        import initiation as init
        
        init.add_habit(csv_file_path) #add habit to follow
    elif user_choice == "e":
        print("You have chosen to make entries.\n")
        import entry as ent
        ent.enter(csv_file_path)
    elif user_choice == "c":
        print("You have chosen to analyze your habits.\n")
        import calculation_daily as calc_d
        calc_d.calculate(csv_file_path)  # Calculate daily habits summary
        import calculation_weekly as calc_w
        calc_w.calculate(csv_file_path)  # Calculate weekly habits summary
        import elaborate_weekly as ew
        ew.elab()  # Elaborate on the weekly data
    elif user_choice == "d":
        print ("You have chosen to delete a habit from the list.\n")
        import delete_habit as dh
        dh.delete_habit(csv_file_path)
    else:
        print("Invalid entry. Please user_choice a valid option.")
