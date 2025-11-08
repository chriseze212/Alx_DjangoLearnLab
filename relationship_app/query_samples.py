import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
library_books = library.books.all()
print(f"Books in {library_name}: {[book.title for book in library_books]}")

# 3. Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian of {library_name}: {librarian.name}")
