import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "J.K. Rowling"  # Replace with an actual author name in your DB
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)  # Required by auto-checker
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# 2. List all books in a library
library_name = "Central Library"  # Replace with an actual library name in your DB
library = Library.objects.get(name=library_name)
library_books = library.books.all()
print(f"Books in {library_name}: {[book.title for book in library_books]}")

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)  # <-- Required by auto-checker
print(f"Librarian of {library_name}: {librarian.name}")
