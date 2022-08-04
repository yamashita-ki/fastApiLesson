from typing import Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    titile: Optional[str] = Field(None, example = "Go to Coffee Store")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id:int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    done: bool = Field(False, description = "Done Flag")

    class Config:
        orm_mode = True