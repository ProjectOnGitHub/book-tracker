#!/usr/bin/env python3
from typing import List
from models import Book
from storage import load_books, save_books, add_book, delete_book
from stats import calculate_average_rating, get_statistics_by_author, display_author_statistics

def display_menu():
    print("\n" + "=" * 50)
    print("📚 ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
    print("=" * 50)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")
    print("-" * 50)


def add_book_interactive(books: List[Book]) -> None:
    print("\n📖 ДОБАВЛЕНИЕ НОВОЙ КНИГИ")
    print("-" * 30)

    author = input("Введите автора: ").strip()
    if not author:
        print("❌ Автор не может быть пустым!")
        return

    title = input("Введите название: ").strip()
    if not title:
        print("❌ Название не может быть пустым!")
        return

    try:
        rating = int(input("Введите оценку (1-5): ").strip())
        if not 1 <= rating <= 5:
            print("❌ Оценка должна быть от 1 до 5!")
            return
    except ValueError:
        print("❌ Оценка должна быть целым числом!")
        return

    success, message = add_book(books, author, title, rating)
    print(message)

    if success:
        save_books(books)


def display_all_books(books: List[Book]) -> None:
    if not books:
        print("\n📚 Библиотека пуста. Добавьте первую книгу!")
        return

    print("\n" + "=" * 60)
    print("📚 ВСЕ КНИГИ В БИБЛИОТЕКЕ")
    print("=" * 60)

    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")

    print(f"\n📊 Всего книг: {len(books)}")


def show_average_rating(books: List[Book]) -> None:
    avg_rating = calculate_average_rating(books)

    print("\n" + "=" * 40)
    print("⭐ СРЕДНЯЯ ОЦЕНКА")
    print("=" * 40)

    if books:
        print(f"Средняя оценка всех книг: {avg_rating} / 5.0")
        print(f"Всего оценено книг: {len(books)}")

        ratings_distribution = {}
        for book in books:
            ratings_distribution[book.rating] = ratings_distribution.get(book.rating, 0) + 1

        print("\nРаспределение оценок:")
        for rating in sorted(ratings_distribution.keys()):
            count = ratings_distribution[rating]
            bar = "⭐" * count
            print(f"  {rating} звёзд: {bar} ({count} книг)")
    else:
        print("Нет книг для оценки")


def delete_book_interactive(books: List[Book]) -> None:
    if not books:
        print("\n📚 Библиотека пуста. Нечего удалять!")
        return

    print("\n🗑️ УДАЛЕНИЕ КНИГИ")
    print("-" * 30)

    author = input("Введите автора книги для удаления: ").strip()
    title = input("Введите название книги для удаления: ").strip()

    if not author or not title:
        print("❌ Автор и название не могут быть пустыми!")
        return

    success, message = delete_book(books, author, title)
    print(message)

    if success:
        save_books(books)


def show_author_statistics(books: List[Book]) -> None:
    stats = get_statistics_by_author(books)
    display_author_statistics(stats)


def main():
    print("🚀 Запуск Трекера прочитанных книг...")

    books = load_books()
    print(f"📚 Загружено книг: {len(books)}")

    while True:
        display_menu()

        choice = input("\nВыберите действие (1-6): ").strip()

        if choice == '1':
            add_book_interactive(books)
        elif choice == '2':
            display_all_books(books)
        elif choice == '3':
            show_average_rating(books)
        elif choice == '4':
            show_author_statistics(books)
        elif choice == '5':
            delete_book_interactive(books)
        elif choice == '6':
            print("\n👋 До свидания! Хорошего дня!")
            break
        else:
            print("❌ Неверный выбор! Пожалуйста, выберите число от 1 до 6.")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Программа прервана пользователем. До свидания!")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        print("Пожалуйста, сообщите об ошибке разработчику.")