class Book:
    """Represents a book in the library with title, author, and availability status."""
    
    def __init__(self, title, author):
        """Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available.
        
        Returns:
            bool: True if available, False if checked out
        """
        return not self._is_checked_out


class Library:
    """Manages a collection of books in the library."""
    
    def __init__(self):
        """Initialize a Library instance with an empty book collection."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library collection.
        
        Args:
            book (Book): A Book instance to add to the library
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by its title.
        
        Args:
            title (str): The title of the book to check out
        """
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in the library.")
    
    def return_book(self, title):
        """Return a book by its title.
        
        Args:
            title (str): The title of the book to return
        """
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book '{title}' not found in the library.")
    
    def list_available_books(self):
        """Print all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")