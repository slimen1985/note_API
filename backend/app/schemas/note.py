from pydantic import BaseModel


class NoteBaseModel(BaseModel):
    title: str
    content: str
    owner_id: int


class NoteCreateModel(NoteBaseModel):
    pass


class RoleUpdateModel(NoteBaseModel):
    pass


class RoleModel(NoteBaseModel):
    id: int

    class Config:
        orm_mode = True