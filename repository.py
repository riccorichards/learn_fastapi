from schemas import TaskAdd, Task, TaskID
from db import TaskOrm
from db import new_session
from sqlalchemy import select

class TaskRepo:
    @classmethod
    async def add_one(cls, data: TaskAdd) -> TaskID:
       async with new_session() as session:
           task_dict = data.model_dump()

           task = TaskOrm(**task_dict)
           session.add(task)
           await session.flush()
           await session.commit()

           return {"OK": True, "tast_id": task.id}
        

    @classmethod
    async def find_all(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schema = [Task.model_validate(task_model) for task_model in task_models]

            return task_schema


        