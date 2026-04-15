import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    # создаем экземпляр (объект) класса BooksCollector
    # collector = BooksCollector()

    # добавляем две книги
    # collector.add_new_book('Гордость и предубеждение и зомби')
    # collector.add_new_book('Что делать, если ваш кот хочет вас убить')

    # проверяем, что добавилось именно две
    # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # ---all positive---
    # проверяем, что после добавления книги, у нее отсутствует жанр по дефолту
    def test_add_new_book_has_no_genre(self):
        collector = BooksCollector()

        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)

        assert collector.get_book_genre(book_name) == ""

    # проверяем возможность указания жанра для книги
    def test_set_book_genre(self):
        collector = BooksCollector()

        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        book_genre = "Комедии"
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre

    # проверяем возможность получения жанра по книге
    def test_get_book_genre(self):
        collector = BooksCollector()

        book_name = "Что делать, если ваш кот хочет вас убить"
        collector.add_new_book(book_name)
        book_genre = "Фантастика"
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    # проверяем запрос списка с конкретными жанрами
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        book1_name = "Что делать, если ваш кот хочет вас убить"
        collector.add_new_book(book1_name)
        book2_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book2_name)
        book_genre = "Фантастика"

        collector.set_book_genre(book1_name, book_genre)
        collector.set_book_genre(book2_name, book_genre)
        assert collector.get_books_with_specific_genre(book_genre) == [
            book1_name,
            book2_name,
        ]

    # проверяем получение словаря книг и жанров
    def test_get_books_genre(self):
        collector = BooksCollector()

        book_name = "Что делать, если ваш кот хочет вас убить"
        collector.add_new_book(book_name)
        book_genre = "Ужасы"
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_genre() == {book_name: book_genre}

    # проверяем запрос книг подходящих детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        book_name = "Что делать, если ваш кот хочет вас убить"
        collector.add_new_book(book_name)
        book_genre = "Комедии"
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_for_children() == [book_name]

    # проверяем возможность добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    # проверяем удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    # проверяем получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        book1_name = "Что делать, если ваш кот хочет вас убить"
        collector.add_new_book(book1_name)
        book2_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book2_name)
        collector.add_book_in_favorites(book1_name)
        collector.add_book_in_favorites(book2_name)
        assert collector.get_list_of_favorites_books() == [book1_name, book2_name]

    # ---all negative---

    # проверяем, что нельзя добавить книгу с невалидным числом символов в имени

    @pytest.mark.parametrize(
        "book_name",
        ["", "a" * 42],
    )
    def test_add_new_book_invalid_names(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    # проверяем что нельзя получить жанр для несуществующей книги
    def test_set_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre("nonexistent_book",'"Комедии')
        assert collector.get_book_genre("nonexistent_book") is None
