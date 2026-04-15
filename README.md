# qa_python
# Список реализованных тестов:

# --- positive tests ---
# 1. test_add_new_book_has_no_genre - проверка, что после добавления книги жанр по умолчанию пустой
# 2. test_set_book_genre - проверка присвоения жанра к добавленной книге
# 3. test_get_book_genre - проверка возвращения жанра по названию книги
# 4. test_get_books_with_specific_genre - проверка вывода списка книг по определенному жанру
# 5. test_get_books_genre - проверка возврата словаря всех книг и жанров
# 6. test_get_books_for_children - проверка возврата списка книг, подходящих для детей
# 7. test_add_book_in_favorites - проверка добавления книги в избранное
# 8. test_delete_book_from_favorites - проверка удаления книги из избранного
# 9. test_get_list_of_favorites_books - проверка вывода списка избранных книг

# --- negative tests ---

# 10, 11. test_add_new_book_invalid_names (parametrized) - проверка граничных значений имени книги с использованием параметризации
# 12. test_set_genre_for_nonexistent_book - проверка невозможности установки жанра несуществующей книге
# Sprint_4
