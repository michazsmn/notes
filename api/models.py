from .db import Base
from sqlalchemy import Integer, String, Boolean, Column


class notes(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    completed = Column(Boolean, index=True)

