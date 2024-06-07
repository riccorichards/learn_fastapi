from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import TaskAdd, Task, TaskID
from repository import TaskRepo


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("")
async def add_tasks(task: Annotated[TaskAdd, Depends()]) -> TaskID:
    task_id = await TaskRepo.add_one(task)
    return task_id


@router.get("")
async def find_all() -> list[Task]:
    tasks = await TaskRepo.find_all()
    return tasks