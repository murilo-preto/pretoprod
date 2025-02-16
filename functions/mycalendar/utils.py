def calculate_duration_minutes(current_time, next_time) -> int:
    """Calculate duration in minutes between two times"""
    if next_time is None:  # Last event of the day
        # Assume it lasts until the end of the workday if it's the last event
        end_of_day = current_time.replace(hour=18, minute=0)  # 6 PM
        return ((end_of_day.hour * 60 + end_of_day.minute) - 
                (current_time.hour * 60 + current_time.minute))
    return ((next_time.hour * 60 + next_time.minute) - 
            (current_time.hour * 60 + current_time.minute))