"""
Goal

Simulate session expiry in Python (without Django, Flask, or external tools). Just pure Python, using in-memory storage.

What You Need to Implement

1.Create a session with an expiry time (e.g., 60 seconds).
Each session could be a dictionary containing:
session_id
user_id
expiry_time (timestamp when it should expire)
2.Validate session → check if the session is still active.
If the current time > expiry time → expired.
3.Delete expired sessions automatically whenever you check sessions.

What You’ll Learn
1/Tracking time-based expiration in memory.
2/How scalable applications manage session lifecycle.
3/Simulating token/session validation.

"""
import time

class SessionManager:
    def __init__(self, expiry_seconds):
        """
        expiry_seconds: how long a session is valid
        """
        self.expiry_seconds = expiry_seconds
        self.sessions = {}  # key: session_id, value: creation_time

    def create_session(self, session_id):
        """
        Creates a new session with the current time.
        """
        self.sessions[session_id] = time.time()
        return f"Session {session_id} created"

    def is_session_active(self, session_id):
        """
        Returns True if the session exists and is not expired.
        If expired, delete it and return False.
        """
        if session_id not in self.sessions:
            return False

        creation_time = self.sessions[session_id]
        if time.time() - creation_time > self.expiry_seconds:
            # session expired
            del self.sessions[session_id]
            return False
        return True

    def delete_session(self, session_id):
        """
        Deletes a session manually.
        Return "Deleted" if session was present, else "Not Found".
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            return "Deleted"
        else:
            return "Not Found"

"""
How it works

create_session("abc123") → stores session with current timestamp.

is_session_active("abc123") → checks if still within expiry limit.

If expired → removes it and returns False.

delete_session("abc123") → manually removes a session."

"""