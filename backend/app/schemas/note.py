from pydantic import BaseModel


class NoteBaseModel(BaseModel):
    title: str
    content: str
    owner_id: int


class NoteCreateModel(NoteBaseModel):
    pass


class NoteUpdateModel(NoteBaseModel):
    pass


class NoteModel(NoteBaseModel):
    id: int

    class Config:
        orm_mode = True