from functions.parser import parse_work_logs
from functions.mycalendar import save_week_calendar_view

# Get all logs
logs = parse_work_logs("makeshift_data")

# Create the week view
save_week_calendar_view(logs)