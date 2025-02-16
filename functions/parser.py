import os
import datetime

def parse_work_logs(directory):
    parsed_data = []
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            date_str = filename.replace(".txt", "")
            try:
                # Convert the filename to a date object
                date_obj = datetime.datetime.strptime(date_str, "%m-%d-%Y").strftime("%d-%B-%Y")
                # print(date_obj)
            except ValueError:
                continue
            
            # Open and read the content of the file
            with open(os.path.join(directory, filename), "r") as f:
                lines = f.readlines()
            
            # Initialize a dictionary to store the log entries for the day
            daily_log = {"date": date_obj, "entries": []}
            
            # Process each line in the file
            for line in lines:
                parts = line.strip().split(" - ", 1)
                if len(parts) == 2:
                    # Extract time and activity from the line
                    time_str, activity = parts
                    time_obj = datetime.datetime.strptime(time_str.split()[0], "%H:%M").time()
                    # Append the entry to the daily log
                    daily_log["entries"].append({"time": time_obj, "activity": activity})
            
            # Add the daily log to the parsed data
            parsed_data.append(daily_log)
    
    return parsed_data