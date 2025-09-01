"""
Task 4: Rate Limiter Simulation

Simulate a Simple Rate Limiter in Python
Rate limiting is a system design concept used in APIs to prevent excessive use or abuse by limiting the number of requests a user/client can make in a certain time window. For example, a user might be limited to making 10 requests per minute. This prevents server overload, ensures fair usage, and improves security.

In production, frameworks like Django Rest Framework use throttle classes or middleware to implement this. But at the core, rate limiting can be built using simple Python data structures like dictionaries and timestamps.

In this task, you will implement a basic rate limiter that allows only a fixed number of requests for each user within a specified time window (e.g., 60 seconds). If a user exceeds the limit, they should be blocked until the time window resets.

What You’ll Learn:

How rate limiting works under the hood

How to use time-based logic to simulate access control

How to implement fair access to services in a scalable system
"""
import time

class RateLimiter:
    def __init__(self, max_requests, time_window):
        """
        max_requests: maximum allowed requests
        time_window: time window in seconds
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_logs = {}  # key: user_id, value: list of timestamps

    def allow_request(self, user_id):
        """
        Returns True if the user's request is allowed under the rate limit,
        else returns False.
        """
        current_time = time.time()

        if user_id not in self.user_logs:
            self.user_logs[user_id] = []

        # Remove timestamps outside of the time window
        self.user_logs[user_id] = [
            t for t in self.user_logs[user_id] if current_time - t < self.time_window
        ]

        if len(self.user_logs[user_id]) < self.max_requests:
            # Allow request
            self.user_logs[user_id].append(current_time)
            return True
        else:
            # Block request
            return False
