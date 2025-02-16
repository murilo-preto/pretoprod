# functions/mycalendar.py

from datetime import datetime, timedelta
import calendar
from typing import Dict, List

def calculate_duration_minutes(current_time, next_time) -> int:
    """Calculate duration in minutes between two times"""
    if next_time is None:  # Last event of the day
        # Assume it lasts until the end of the workday if it's the last event
        end_of_day = current_time.replace(hour=18, minute=0)  # 6 PM
        return ((end_of_day.hour * 60 + end_of_day.minute) - 
                (current_time.hour * 60 + current_time.minute))
    return ((next_time.hour * 60 + next_time.minute) - 
            (current_time.hour * 60 + current_time.minute))

def generate_calendar_html(day_data: Dict) -> str:
    """Generate HTML calendar view for a single day's activities."""
    
    # Parse the date
    date_obj = datetime.strptime(day_data['date'], '%d-%B-%Y')
    
    # Format date string and day name
    date_str = date_obj.strftime('%B %d, %Y')
    day_name = calendar.day_name[date_obj.weekday()]
    
    # Generate events HTML with durations
    events_html = ""
    entries = day_data['entries']
    
    for i, entry in enumerate(entries):
        current_time = entry['time']
        next_time = entries[i + 1]['time'] if i < len(entries) - 1 else None
        
        duration = calculate_duration_minutes(current_time, next_time)
        time_str = entry['time'].strftime('%I:%M %p')
        activity = entry['activity']
        
        # Calculate height based on duration (1 minute = 2px)
        height = max(duration * 2, 50)  # Minimum height of 50px
        
        # Check if it's a special event
        special_class = 'special-event' if activity.startswith('[') and activity.endswith(']') else ''
        
        event_html = f"""
        <div class="event {special_class}" style="height: {height}px;">
            <div class="time">
                <span class="time-value">{time_str}</span>
                <span class="duration">({duration} min)</span>
            </div>
            <div class="activity">{activity}</div>
        </div>
        """
        events_html += event_html
    
    # HTML template with CSS styling using f-string
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Daily Calendar View</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 2rem;
                background-color: #f5f5f5;
            }}
            .calendar-container {{
                max-width: 800px;
                margin: 0 auto;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                padding: 20px;
            }}
            .date-header {{
                text-align: center;
                padding: 1rem;
                background-color: #f8f9fa;
                border-radius: 5px;
                margin-bottom: 1rem;
            }}
            .date-header h2 {{
                margin: 0;
                color: #2c3e50;
            }}
            .timeline {{
                position: relative;
                padding: 1rem;
                display: flex;
                flex-direction: column;
                gap: 4px;
            }}
            .event {{
                display: flex;
                padding: 0.5rem;
                border-left: 3px solid #3498db;
                background-color: #f8f9fa;
                transition: transform 0.2s;
                min-height: 50px;
                box-sizing: border-box;
            }}
            .event:hover {{
                transform: translateX(5px);
                background-color: #e9ecef;
            }}
            .time {{
                min-width: 120px;
                display: flex;
                flex-direction: column;
                color: #2c3e50;
            }}
            .time-value {{
                font-weight: bold;
            }}
            .duration {{
                font-size: 0.8em;
                color: #666;
                margin-top: 4px;
            }}
            .activity {{
                flex-grow: 1;
                color: #34495e;
                display: flex;
                align-items: center;
            }}
            .special-event {{
                border-left-color: #e74c3c;
                background-color: #fff5f5;
            }}
        </style>
    </head>
    <body>
        <div class="calendar-container">
            <div class="date-header">
                <h2>{date_str}</h2>
                <p>{day_name}</p>
            </div>
            <div class="timeline">
                {events_html}
            </div>
        </div>
    </body>
    </html>
    """

def save_calendar_view(day_data: Dict, output_file: str = 'calendar.html') -> None:
    """Save the calendar view to an HTML file."""
    html_content = generate_calendar_html(day_data)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)