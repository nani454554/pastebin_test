from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SnippetCreate(BaseModel):
    content: str
    is_public: bool = True
    expiration: Optional[datetime] = None

class SnippetResponse(SnippetCreate):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True
