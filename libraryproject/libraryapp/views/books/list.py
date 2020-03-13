import sqlite3
from django.shortcuts import redirect, render, reverse
from libraryapp.models import Book
from ..connection import Connection


def book_list(request):
    if request.method == 'GET':
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     select
        #         b.id,
        #         b.title,
        #         b.isbn,
        #         b.author,
        #         b.year,
        #         b.librarian_id,
        #         b.location_id
        #     from libraryapp_book b
        #     """)

        #     all_books = []
        #     dataset = db_cursor.fetchall()

        #     for row in dataset:
        #         book = Book()
        #         book.id = row['id']
        #         book.title = row['title']
        #         book.isbn = row['isbn']
        #         book.author = row['author']
        #         book.year = row['year']
        #         book.librarian_id = row['librarian_id']
        #         book.location_id = row['location_id']

        #         all_books.append(book)
        all_books = Book.objects.all()

        title = request.GET.get('title', None)
        # title = request.GET['title']

        if title is not None:
            all_books = all_books.filter(title__contains=title)

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     INSERT INTO libraryapp_book
        #     (
        #         title, author, isbn,
        #         year, location_id, librarian_id
        #     )
        #     VALUES (?, ?, ?, ?, ?, ?)
        #     """,
        #     (form_data['title'], form_data['author'],
        #     form_data['isbn'], form_data['year_published'],
        #     request.user.librarian.id, form_data["location"]))
        
        # instantiate...
        new_book = Book(
            title = form_data['title'],
            author = form_data['author'],
            isbn = form_data['isbn'],
            year = form_data['year_published'],
            librarian_id = request.user.librarian.id,
            location_id = form_data["location"]
        )

        # and then save to the db
        print(new_book.librarian.user.username)
        new_book.save()

        # Or...
        # Use a shortcut to do both at the same time
        # new_book = Book.objects.create(
        #     title = form_data['title'],
        #     author = form_data['author'],
        #     isbn = form_data['isbn'],
        #     year = form_data['year_published'],
        #     location_id = request.user.librarian.id,
        #     librarian_id = form_data["location"]
        # )

        return redirect(reverse('libraryapp:books'))
