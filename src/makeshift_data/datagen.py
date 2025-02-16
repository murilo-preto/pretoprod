import datetime
import random

# Define possible activities
activities_morning = [
    "Check emails", "Study AI", "Team meeting", "Review reports", "Write documentation",
    "Fix bugs", "Plan project tasks", "Read industry news", "Prepare presentation"
]

activities_afternoon = [
    "Check client demands", "Code implementation", "Debug application", "Update project status",
    "Research new tools", "Optimize database", "Test software", "Write report", "Review pull requests"
]

# Generate ten files with different dates and randomized activities
start_date = datetime.date(2025, 2, 6)  # Starting from a past date

for i in range(10):
    current_date = start_date + datetime.timedelta(days=i)
    date_str = current_date.strftime("%m-%d-%Y")
    filename = f"{date_str}.txt"

    log = []
    log.append(f"09:02 {date_str} - [Workday start]")

    time = datetime.datetime.strptime("09:12", "%H:%M")
    random.shuffle(activities_morning)
    for activity in activities_morning[:5]:
        log.append(f"{time.strftime('%H:%M')} {date_str} - {activity}")
        time += datetime.timedelta(minutes=random.randint(5, 15))

    log.append(f"11:54 {date_str} - [Lunch Break]")
    log.append(f"12:25 {date_str} - [Resume working]")

    time = datetime.datetime.strptime("13:25", "%H:%M")
    random.shuffle(activities_afternoon)
    for activity in activities_afternoon[:5]:
        log.append(f"{time.strftime('%H:%M')} {date_str} - {activity}")
        time += datetime.timedelta(minutes=random.randint(5, 15))

    log.append(f"16:03 {date_str} - [Workday end]")

    with open(f"data/{filename}", "w") as f:
        f.write("\n".join(log))

print("Files generated successfully.")