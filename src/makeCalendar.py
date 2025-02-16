from functions.parser import parse_work_logs
from functions.mycalendar import save_week_calendar_view

data = "makeshift_data"

# Get all logs
logs = parse_work_logs(data)

# Create the week view
save_week_calendar_view(logs)