from dataclasses import dataclass
from books import *

########################################
# NON PYDANTIC DATA CLASSES
# (because I can, maybe)
########################################

Books = [BOOK1, BOOK2]

Book_Categories = [
    "MLOps",
    "DevOps",
    "Algorithms", 
    "Data Structures",
    "Design Patterns",
    "Cloud Computing"
    "Software Engineering",
]

@dataclass
class BookMetaData():
    title: str
    author: str
    summary: str
    category: str
    description: str

@dataclass
class BookChaper():
    title: str
    summary: str
    quotes: list
    bullets: list
    read_time: int
    importance: int

@dataclass
class BookSummary():
    chapters: list
