# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case to handle priority
match priority:
    case "high":
        priority_text = "high priority"
    case "medium":
        priority_text = "medium priority"
    case "low":
        priority_text = "low priority"
    case _:
        priority_text = "unspecified priority"

# Use if to handle time sensitivity
if time_bound == "yes":
    time_text = "that requires immediate attention today!"
else:
    time_text = "Consider completing it when you have free time."

# Provide a fully customized reminder
print(f"Reminder: '{task}' is a {priority_text} task {time_text}")
