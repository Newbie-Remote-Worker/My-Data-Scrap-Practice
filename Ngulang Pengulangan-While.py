#4. Pengulangan While

all_books_in_library = 10
print('librarian said, "read all books"')

books_have_been_read = 0
print(f'have been read {books_have_been_read} books')

while books_have_been_read < all_books_in_library:
    books_have_been_read = books_have_been_read + 1
    print(f'have been read {books_have_been_read} books')

print(f'all books {books_have_been_read} have been read')
