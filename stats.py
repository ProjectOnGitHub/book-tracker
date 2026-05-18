from typing import List, Dict
from models import Book


def calculate_average_rating(books: List[Book]) -> float:
    if not books:
        return 0.0

    total_rating = sum(book.rating for book in books)
    return round(total_rating / len(books), 2)


def get_statistics_by_author(books: List[Book]) -> Dict[str, Dict]:
    stats = {}

    for book in books:
        author = book.author
        if author not in stats:
            stats[author] = {
                "book_count": 0,
                "total_rating": 0,
                "books": []
            }

        stats[author]["book_count"] += 1
        stats[author]["total_rating"] += book.rating
        stats[author]["books"].append(book.title)

    for author in stats:
        stats[author]["average_rating"] = round(
            stats[author]["total_rating"] / stats[author]["book_count"], 2
        )

    return stats


def display_author_statistics(stats: Dict[str, Dict]) -> None:
    if not stats:
        print("\n📊 Статистика по авторам отсутствует")
        return

    print("\n" + "=" * 50)
    print("📊 СТАТИСТИКА ПО АВТОРАМ")
    print("=" * 50)

    sorted_authors = sorted(stats.items(), key=lambda x: x[1]["book_count"], reverse=True)

    for author, data in sorted_authors:
        print(f"\n👨‍💼 Автор: {author}")
        print(f"   📚 Книг прочитано: {data['book_count']}")
        print(f"   ⭐ Средняя оценка: {data['average_rating']}")
        print(f"   📖 Список книг: {', '.join(data['books'])}")