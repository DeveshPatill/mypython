"""
Task 3: In-Memory File Storage System

Simulate a File Storage System in Python (In-Memory)
In backend systems like Django, user-uploaded files such as profile pictures, invoices, or reports need to be stored, retrieved, or deleted. In production, cloud storage services like AWS S3, Google Cloud Storage, or Azure Blob are typically used. However, all of them operate on a very simple principle — storing and retrieving files using unique paths or keys.

In this task, you will simulate a very basic file storage system in memory using a Python dictionary. Each file will be stored using a string key (the filename or path), and its content will be the corresponding value (string content or binary-like data).

The focus of this exercise is to understand the basic file storage operations and how a cloud-like storage interface can be abstracted using plain Python.

What You’ll Learn:

How file storage systems organize and retrieve data

How to abstract file operations (create, read, delete)

How to simulate a production storage system with simple logic
"""
class InMemoryFileStorage:
    def __init__(self):
        """
        Initialize the file storage with an empty dictionary.
        """
        self.storage = {}

    def save_file(self, path, content):
        """
        Save a file to the given path with the given content.
        If the file already exists, overwrite it.
        """
        self.storage[path] = content
        return f"File '{path}' saved."

    def read_file(self, path):
        """
        Return the content of the file at the given path.
        If the file does not exist, return "File Not Found".
        """
        return self.storage.get(path, "File Not Found")

    def delete_file(self, path):
        """
        Delete the file at the given path.
        Return "Deleted" if deleted successfully,
        or "File Not Found" if it doesn't exist.
        """
        if path in self.storage:
            del self.storage[path]
            return "Deleted"
        else:
            return "File Not Found"

    def list_files(self):
        """
        Return a sorted list of all file paths currently stored.
        """
        return sorted(self.storage.keys())
