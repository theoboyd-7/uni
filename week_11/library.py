class Book:

    def __init__(self, title, author, isbn):
        self.available = True
        self.title = title
        self.author = author
        self.isbn = isbn

    def borrow_book(self):
        if self.available == True:
            self.available = False
            return f"The {self.title} has been borrowed"
        return f"The {self.title} is currently being borrowed"

    def return_book(self):
        if self.available == False:
            self.available = True
            return f"The {self.title} has been returned"
        return f"The {self.title} is currently not being borrowed"

    def __str__(self):
        output = f"Title is {self.title} written by {self.author} and ISBN {self.isbn}"
        return output


class DigitalBook(Book):

    compatibility_options = set(['Kindle', 'PDF', 'Apple'])

    def __init__(self, title, author, isbn):
        # Call the superclass constructor with title, author, and isbn
        super().__init__(title, author, isbn)
        self.compatibility = {'Kindle'}

    def borrow_book(self):
        # Don't remove the pass
        pass

    def return_book(self):
        # Don't remove the pass (same as borrow_book)
        pass

    def set_compatibility(self, compatibility):
        if compatibility in self.compatibility_options:
            self.compatibility = compatibility
            return f"Compatibility is now {self.compatibility}"

    def __str__(self):
        # Remove the pass and write code for this method
        # (printing a digital book should also display its compatibility)
        output = f"Title is {self.title} written by {self.author} and ISBN {self.isbn} "
        output += f"and is compatible on {self.compatibility}"
        return output


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available == True:
                    return book.borrow_book()
        return f"Book with ISBN {isbn} is not in the library"

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.return_book()

    def __str__(self):
        output = "Library contains:\n"
        for book in self.books:
            status = ''
            if book.available == True:
                status = 'Available'
            else:
                status = 'Borrowed'
            output += f"{book} and is currently {status}\n"
        return output


def test_book():
    book = Book('Frankenstein', 'Mary Shelley', '978-0486282114')
    print(book.borrow_book())
    print(book)
    print(book.return_book())

#test_book()

def test_digital_book():
    digital_book = DigitalBook(
        'Orlando: A Biography', 'Virginia Woolf', '978-0156031516')
    print(digital_book.borrow_book())
    print(digital_book.set_compatibility("PDF"))
    print(digital_book)

#test_digital_book()

def test_library():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    book3 = Book("Jane Eyre", "Charlotte Bronte", "978-0141441146")
    book4 = DigitalBook("1984", "George Orwell", "978-0451524935")

    library = Library()
    # Add the books to the library here and try borrowing and returning them
    # Remember to print the library object at each step
    library.add_book(book1)
    print(library)
    library.add_book(book2)
    print(library)
    library.add_book(book3)
    print(library)
    library.add_book(book4)
    print(library)

    print(library.borrow_book("978-0451524935"))
    print(library)

    print(library.return_book("978-0451524935"))
    print(library)

test_library()