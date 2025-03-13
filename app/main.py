from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import Snippet
from app.schemas import SnippetCreate, SnippetResponse
from app.crud import create_snippet, get_snippet, update_snippet
import os

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Serve Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/snippets/", response_model=SnippetResponse)
def create_snippet_endpoint(snippet: SnippetCreate, db: Session = Depends(get_db)):
    return create_snippet(db, snippet)

@app.get("/snippets/{snippet_id}", response_model=SnippetResponse)
def get_snippet_endpoint(snippet_id: str, db: Session = Depends(get_db)):
    snippet = get_snippet(db, snippet_id)
    if not snippet:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet

@app.put("/snippets/{snippet_id}", response_model=SnippetResponse)
def update_snippet_endpoint(snippet_id: str, snippet: SnippetCreate, db: Session = Depends(get_db)):
    return update_snippet(db, snippet_id, snippet)

# Serve HTML Page
@app.get("/")
def serve_homepage():
    return FileResponse("static/index.html")
