from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str
    description: str | None = None


class ProjectCreate(ProjectBase):
    pass

class UserBase(BaseModel):
    email: str


class Project(ProjectBase):
    id: int
    users:list[UserBase]= []
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str
class User(UserBase):
    id: int
    is_active: bool
    projects: list[Project] = []

    class Config:
        orm_mode = True