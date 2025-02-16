def calculate_duration_minutes(current_time, next_time) -> int:
    """Calculate the duration in minutes between two times."""
    
    # Check if the next event time is provided
    if next_time is None:
        # If there is no next event, return a default duration of 10 minutes
        return 10
    
    # If there is a next event, calculate the duration until that event
    next_time_minutes = next_time.hour * 60 + next_time.minute
    current_time_minutes = current_time.hour * 60 + current_time.minute
    duration_minutes = next_time_minutes - current_time_minutes
    
    return duration_minutes
