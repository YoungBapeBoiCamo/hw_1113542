# Name: Ferran
# Student ID: 1113542
# Date of Submission: 2024/11/28

# Task class to represent each task with profit and deadline
class Task:
    def __init__(self, profit, deadline):
        self.profit = profit
        self.deadline = deadline

def schedule_tasks(n, tasks):
    # Sort tasks by profit in descending order
    tasks.sort(key=lambda x: x.profit, reverse=True)
    
    # Array to keep track of filled slots (1-based indexing for slots)
    slots = [False] * (n + 1)  # Slots 1 to n (0 is unused)
    
    total_profit = 0
    scheduled_tasks = []
    
    # Try to schedule each task
    for task in tasks:
        # Start from the task's deadline and look for the first available slot
        for i in range(task.deadline, 0, -1):
            if not slots[i]:  # If slot i is free
                slots[i] = True  # Mark the slot as filled
                total_profit += task.profit
                scheduled_tasks.append(task.profit)
                break  # Move to the next task
    
    return total_profit, scheduled_tasks

# Input: First enter the number of tasks
n = int(input("Enter number of tasks: "))

# Input: Then enter the profit and deadline of each task
tasks = []
for _ in range(n):
    profit, deadline = map(int, input().split())
    tasks.append(Task(profit, deadline))

# Schedule tasks and calculate the maximum profit
max_profit, scheduled = schedule_tasks(n, tasks)

# Output the result
print("Maximum Profit:", max_profit)
print("Scheduled Tasks:", scheduled)
