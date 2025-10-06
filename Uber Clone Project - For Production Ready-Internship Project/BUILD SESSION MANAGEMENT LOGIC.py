# Write your Python code here
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
        # Your code here
        self.sessions[session_id] = time.time()
        return f"Sessions '{session_id}' created."

    def is_session_active(self, session_id):
        """
        Returns True if the session exists and is not expired.
        If expired, delete it and return False.
        """
        # Your code here
        if session_id not in self.sessions:
            return False
        
        creation_time = self.sessions[session_id]
        if time.time() - creation_time < self.expiry_seconds:
            return True
        else:
            del self.sessions[session_id]
            return False

    def delete_session(self, session_id):
        """
        Deletes a session manually.
        Return "Deleted" if session was present, else "Not Found".
        """
        # Your code here
        if session_id in self.sessions:
            del self.sessions[session_id]
            return"Deleted"
        return "Not Found"