from collections import UserDict

class Field():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Title(Field):
    pass


class Author(Field):
    pass


class Isbn(Field):
    def __init__(self, isbn):
        if not isbn.isdigit() or len(isbn) != 13:
            raise ValueError("ISBN must be a number with thirteen digits")
        super().__init__(isbn)


class BookRecord():
    def __init__(self, title):
        self.title = Title(title)
        self.authors = []
        self.isbns = []

    def add_author(self, author):
        self.authors.append(Author(author))

    def edit_author(self, old_author, new_author):
        for author in self.authors:
            if author.value == old_author:
                self.authors[self.authors.index(author)] = Author(new_author)
                return
        raise ValueError("Old author does not exist")
    
    def add_isbn(self, isbn):
        self.isbns.append(Isbn(isbn))

    def edit_isbn(self, old_isbn, new_isbn):
        for i, isbn in enumerate(self.isbns):
            if isbn.value == old_isbn:
                self.isbns[i] = Isbn(new_isbn)
                return
        raise ValueError("Old ISBN does not exist")
    
    def find_isbn(self, isbn):
        for isbn_in_lst in self.isbns:
            if isbn == isbn_in_lst.value:
                return isbn_in_lst
        raise ValueError("ISBN does not exist")
    
    def __str__(self):
        authors = ", ".join(a.value for a in self.authors)
        isbns = ", ".join(i.value for i in self.isbns)
        return f"Title: {self.title.value}, Authors: {authors}, ISBNs: {isbns}"


class Library(UserDict):
    def add_book(self, record):
        self.data[record.title.value] = record

    def find_book(self, title):
        book = self.data.get(title)
        if book is None:
            raise ValueError("This book does not exist")
        return book

    def delete_book(self, title):
        if title in self.data:
            del self.data[title]
        else:
            raise ValueError("This book does not exist")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


if __name__ == "__main__":
    library = Library()

    war_and_peace = BookRecord("War and Peace")
    war_and_peace.add_author("Tolstoy")
    war_and_peace.add_isbn("1234567890123")

    book_1984 = BookRecord("1984")
    book_1984.add_author("Orwell")
    book_1984.add_isbn("9876543210123")

    library.add_book(war_and_peace)
    library.add_book(book_1984)

    print(library)
    library.find_book("1984")

    book_1984.edit_author("Orwell", "George Orwell")
    war_and_peace.find_isbn("1234567890123")

    library.delete_book("1984")

    print(library)