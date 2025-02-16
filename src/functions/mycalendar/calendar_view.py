from datetime import datetime, timedelta
import calendar
from typing import Dict, List
from .utils import calculate_duration_minutes
from .template_loader import load_template

MIN_EVENT_HEIGHT = 50

def get_work_week_dates(date_obj: datetime) -> List[datetime]:
    """Get all dates for the work week (Mon-Fri) containing the given date.
    
    Args:
        date_obj (datetime): The date to find the work week for.
    
    Returns:
        List[datetime]: List of dates from Monday to Friday.
    """
    monday = date_obj - timedelta(days=date_obj.weekday())
    return [monday + timedelta(days=i) for i in range(5)]

def generate_day_html(day_data: Dict) -> str:
    """Generate HTML for a single day column.
    
    Args:
        day_data (Dict): Data for the day.
    
    Returns:
        str: HTML string for the day.
    """
    if not day_data:
        return ""
        
    date_obj = datetime.strptime(day_data['date'], '%d-%B-%Y')
    date_str = date_obj.strftime('%B %d')
    day_name = calendar.day_name[date_obj.weekday()]
    
    events_html = ""
    entries = day_data['entries']
    
    for i, entry in enumerate(entries):
        current_time = entry['time']
        next_time = entries[i + 1]['time'] if i < len(entries) - 1 else None
        
        duration = calculate_duration_minutes(current_time, next_time)
        time_str = entry['time'].strftime('%I:%M %p')
        activity = entry['activity']
        
        height = max(duration * 2, MIN_EVENT_HEIGHT)
        special_class = 'special-event' if activity.startswith('[') and activity.endswith(']') else ''
        
        event_template = load_template('event.html')
        event_html = event_template.format(
            special_class=special_class,
            height=height,
            time_str=time_str,
            duration=duration,
            activity=activity
        )
        events_html += event_html
    
    day_template = load_template('day.html')
    return day_template.format(
        date_str=date_str,
        day_name=day_name,
        events=events_html
    )

def generate_week_calendar_html(days_data: List[Dict]) -> str:
    """Generate HTML for the full work week view.
    
    Args:
        days_data (List[Dict]): List of data for each day.
    
    Returns:
        str: HTML string for the week.
    """
    if not days_data:
        return "<p>No data available</p>"
    
    first_day = datetime.strptime(days_data[0]['date'], '%d-%B-%Y')
    week_dates = get_work_week_dates(first_day)
    week_str = f"Week of {week_dates[0].strftime('%B %d')} - {week_dates[4].strftime('%B %d, %Y')}"
    
    days_html = ""
    for day_data in days_data:
        days_html += generate_day_html(day_data)
    
    main_template = load_template('main.html')
    css_content = load_template('styles.css')
    
    return main_template.format(
        styles=css_content,
        week_str=week_str,
        days=days_html
    )

def save_week_calendar_view(days_data: List[Dict], output_file: str = 'calendar.html') -> None:
    """Save the work week calendar view to an HTML file.
    
    Args:
        days_data (List[Dict]): List of data for each day.
        output_file (str): The output file path.
    """
    html_content = generate_week_calendar_html(days_data)
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")