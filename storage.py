import json
import os
from typing import List, Optional
from datetime import datetime
from models import Book

DATA_FILE = "books.json"

def load_books() -> List[Book]:
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Book.from_dict(book_data) for book_data in data]
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Ошибка при чтении файла. Создаётся новый файл.")
        return []
    except Exception as e:
        print(f"❌ Ошибка загрузки данных: {e}")
        return []


def save_books(books: List[Book]) -> bool:
    try:
        data = [book.to_dict() for book in books]
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"❌ Ошибка сохранения данных: {e}")
        return False


def add_book(books: List[Book], author: str, title: str, rating: int,
             date_read: Optional[str] = None) -> tuple[bool, str]:
    for book in books:
        if book.author.lower() == author.lower() and book.title.lower() == title.lower():
            return False, f"Книга '{title}' автора {author} уже существует!"

    try:
        if not date_read:
            date_read = datetime.now().strftime("%Y-%m-%d")

        new_book = Book(author, title, rating, date_read)
        books.append(new_book)
        return True, f"✅ Книга '{title}' успешно добавлена!"
    except ValueError as e:
        return False, f"❌ Ошибка валидации: {e}"
    except Exception as e:
        return False, f"❌ Ошибка при добавлении книги: {e}"

def delete_book(books: List[Book], author: str, title: str) -> tuple[bool, str]:
    initial_length = len(books)

    books[:] = [book for book in books
                if not (book.author.lower() == author.lower()
                        and book.title.lower() == title.lower())]

    if len(books) < initial_length:
        return True, f"🗑️ Книга '{title}' автора {author} удалена!"
    else:
        return False, f"❌ Книга '{title}' автора {author} не найдена!"


def find_book(books: List[Book], author: str, title: str) -> Optional[Book]:
    for book in books:
        if book.author.lower() == author.lower() and book.title.lower() == title.lower():
            return book
    return None