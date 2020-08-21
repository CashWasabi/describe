from uuid import UUID
from dataclasses import dataclass


@dataclass(frozen=True)
class Language:
    id: UUID
    name: str


@dataclass(frozen=True)
class Category:
    id: UUID
    topic: str


@dataclass(frozen=True)
class Definition:
    id: UUID
    text = Column(Unicode)


@dataclass(frozen=True)
class Word:
    id: UUID
    word: str
    definition: Definition
    language: Language
    category: category
