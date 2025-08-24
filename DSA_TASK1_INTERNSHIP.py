#Task 1: Queue Simulation (System Design Concept: Queues & Background Processing)

# Write your Python code here
class TaskQueue:
    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

    def enqueue(self, task):
        """
        Add a task to the queue.
        Example:
        >>> q.enqueue("send_email")
        """
        # Your code here
        self.tasks.append(task)

    def dequeue(self):
        """
        Remove and return the task that was added first.
        If queue is empty, return "Queue is empty".
        Example:
        >>> q.dequeue()  # -> "send_email"
        """
        # Your code here
        if not self.tasks:
            return "Queue is empty"
        return self.tasks.pop(0)

    def peek(self):
        """
        Return the task at the front without removing it.
        If queue is empty, return "Queue is empty".
        """
        # Your code here
        if not self.tasks:
            return "Queue is empty"
        return self.tasks[0]

    def size(self):
        """
        Return the number of tasks currently in the queue.
        """
        # Your code here
        return len(self.tasks)

