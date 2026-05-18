from datetime import datetime
from typing import Dict, Any


class Book:
    def __init__(self, author: str, title: str, rating: int, date_read: str = None):
        self.author = author
        self.title = title
        self.rating = rating
        self.date_read = date_read if date_read else datetime.now().strftime("%Y-%m-%d")
        self._validate()

    def _validate(self):
        if not self.author or not self.author.strip():
            raise ValueError("Автор не может быть пустым")
        if not self.title or not self.title.strip():
            raise ValueError("Название не может быть пустым")
        if not 1 <= self.rating <= 5:
            raise ValueError("Оценка должна быть от 1 до 5")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Book':
        return cls(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date_read=data.get("date_read", datetime.now().strftime("%Y-%m-%d"))
        )

    def __str__(self) -> str:
        return f"{self.author} - {self.title} | Оценка: {self.rating}⭐ | Прочитано: {self.date_read}"

    def __repr__(self) -> str:
        return f"Book(author='{self.author}', title='{self.title}', rating={self.rating}, date_read='{self.date_read}')"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return (self.author.lower() == other.author.lower() and
                self.title.lower() == other.title.lower())

    def __hash__(self) -> int:
        return hash((self.author.lower(), self.title.lower()))
