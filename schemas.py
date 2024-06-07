from pydantic import BaseModel
from typing import Optional


class TaskAdd(BaseModel):
    title: str
    desc: Optional[str] = None
    complete: bool


class Task(TaskAdd):
    id: int

class TaskID(BaseModel):
    OK: bool = True
    task_id: int     