import pytest

from main import BooksCollector

class TestBooksCollector:

    # ---all positive---

    # проверяем добавление одной книги
    def test_add_new_book(self, collector):
        book_name = "Хоббит"
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    # проверяем, что после добавления книги, у нее отсутствует жанр по дефолту
    def test_add_new_book_has_no_genre(self, collector):
        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)

        assert collector.get_book_genre(book_name) == ""

    # проверяем возможность указания жанра для книги
    def test_set_book_genre(self, collector):
        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        book_genre = "Комедии"
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre

    # проверяем возможность получения жанра по книге
    def test_get_book_genre(self, collector):
        book_name = "Что делать, если ваш кот хочет вас убить"
        collector.add_new_book(book_name)
        book_genre = "Фантастика"
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    # проверяем запрос списка с конкретными жанрами
    def test_get_books_with_specific_genre(self, collector):
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
    def test_get_books_genre(self, collector):
        book_name = "Что делать, если ваш кот хочет вас убить"
        collector.add_new_book(book_name)
        book_genre = "Ужасы"
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_genre() == {book_name: book_genre}

    # проверяем запрос книг подходящих детям
    def test_get_books_for_children(self, collector):
        book_name = "Что делать, если ваш кот хочет вас убить"
        collector.add_new_book(book_name)
        book_genre = "Комедии"
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_for_children() == [book_name]

    # проверяем возможность добавления книги в избранное
    def test_add_book_in_favorites(self, collector):
        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    # проверяем удаление книги из избранного
    def test_delete_book_from_favorites(self, collector):
        book_name = "Гордость и предубеждение и зомби"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    # проверяем получение списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
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
    def test_add_new_book_invalid_names(self, book_name, collector):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    # проверяем что нельзя получить жанр для несуществующей книги
    def test_set_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre("nonexistent_book", "Комедии")
        assert collector.get_book_genre("nonexistent_book") is None
