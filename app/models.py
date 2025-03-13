from sqlalchemy import Column, String, Text, Boolean, DateTime
from datetime import datetime
from app.database import Base

class Snippet(Base):
    __tablename__ = "snippets"

    id = Column(String, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    is_public = Column(Boolean, default=True)
    expiration = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
