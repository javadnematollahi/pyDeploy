from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str
    time: str
    status: int


