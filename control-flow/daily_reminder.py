# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a HIGH priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a HIGH priority task. Try to complete it soon to stay on track."
    case "medium":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a MEDIUM priority task that is time-sensitive. Make sure to address it today."
        else:
            reminder = f"Reminder: '{task}' is a MEDIUM priority task. You can schedule it at a convenient time."
    case "low":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a LOW priority task but is time-sensitive. Try not to delay it."
        else:
            reminder = f"Note: '{task}' is a LOW priority task. Consider completing it when you have free time."
    case _:  # Default for invalid input
        reminder = f"'{task}' has an unspecified priority. Please check your input."

# Print the customized reminder
print("\n" + reminder)
