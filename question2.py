# Name: Ferran
# Student ID: 1113542
# Date of Submission: 2024/11/28
import heapq

class PriorityQueueManager:
    def __init__(self):
        self.tasks_heap = []  # Max heap (negative priority to simulate max-heap behavior)

    def insert_task(self, task_name, priority):
        # Insert the task into the heap 
        heapq.heappush(self.tasks_heap, (-priority, task_name))

    def retrieve_highest_priority(self):
        if not self.tasks_heap:
            return None
        # Retrieve and remove the highest priority task
        priority, task_name = heapq.heappop(self.tasks_heap)
        return task_name

    def list_tasks(self):
        # Sort the heap tasks in descending order of priority
        return [(task_name, -priority) for priority, task_name in sorted(self.tasks_heap, reverse=True)]

def main():
    # Input 
    num_operations = int(input())  # number of operations
    queue_manager = PriorityQueueManager()
    result = []

    for _ in range(num_operations):
        operation = input().strip().split()
        if operation[0] == "ADD":
            task_name = operation[1]
            priority = int(operation[2])
            queue_manager.insert_task(task_name, priority)
        elif operation[0] == "GET":
            task = queue_manager.retrieve_highest_priority()
            if task:
                result.append(task)
            else:
                result.append("No tasks available.")

    # Output the tasks retrieved by GET operations
    for task in result:
        print(task)

    # Output remaining tasks sorted by priority
    remaining_tasks = queue_manager.list_tasks()
    print("Remaining tasks:", remaining_tasks)

if __name__ == "__main__":
    main()
