from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    description: str
    completed: bool = False
    

class Note(BaseModel):
    id: int
    content: str
    
class Reminder(BaseModel):
    id: int
    reminder_text: str
    remind_at: str  # ISO formatted datetime string

class UserMsg(BaseModel):
    message: str