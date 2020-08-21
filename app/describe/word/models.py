from typing import Any

from sqlalchemy import (
    Column,
    create_engine,
    DateTime,
    ForeignKey,
    Integer,
    Unicode,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    backref,
    relationship,
    scoped_session,
    sessionmaker,
)

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
BaseModel: Any = declarative_base()
BaseModel.query = db_session.query_property()


class LanguageModel(BaseModel):
    __tablename__ = "language"
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)


class CategoryModel(BaseModel):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    topic = Column(Unicode)


class DefinitionModel(BaseModel):
    __tablename__ = "definition"
    id = Column(Integer, primary_key=True)
    text = Column(Unicode)


class WordModel(BaseModel):
    __tablename__ = "word"
    id = Column(Integer, primary_key=True)
    word = Column(Unicode)
    definition = relationship(
        DefinitionModel,
        backref=backref(
            'words',
            uselist=True,
            cascade='delete, all'
        )
    )
    language = relationship(
        LanguageModel,
        backref=backref(
            'words',
            uselist=True,
            cascade='delete, all'
        )
    )
    category = relationship(
        CategoryModel,
        backref=backref(
            'words',
            uselist=True,
            cascade='delete, all'
        )
    )
