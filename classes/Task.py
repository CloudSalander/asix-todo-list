from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    def __init__(self,name,subject,priority=Priority.LOW,url = "",description=""):
        self.name = name
        self.subject = subject
        self.priority = priority
        self.url = url
        self.description = description