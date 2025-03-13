from sqlalchemy.orm import Session
from app.models import Snippet
from app.schemas import SnippetCreate
from app.utils import generate_unique_id

def create_snippet(db: Session, snippet: SnippetCreate):
    snippet_id = generate_unique_id()
    db_snippet = Snippet(id=snippet_id, **snippet.dict())
    db.add(db_snippet)
    db.commit()
    db.refresh(db_snippet)
    return db_snippet

def get_snippet(db: Session, snippet_id: str):
    return db.query(Snippet).filter(Snippet.id == snippet_id).first()

def update_snippet(db: Session, snippet_id: str, snippet: SnippetCreate):
    db_snippet = db.query(Snippet).filter(Snippet.id == snippet_id).first()
    if db_snippet:
        db_snippet.content = snippet.content
        db_snippet.is_public = snippet.is_public
        db_snippet.expiration = snippet.expiration
        db.commit()
        db.refresh(db_snippet)
    return db_snippet
