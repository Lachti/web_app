# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Book

from .models import Rental

from .forms import UserForm

def index(request):
    if (request.user.is_authenticated()):
        books = Book.objects.filter(is_rented=False)
        rentals = Rental.objects.filter(user=request.user, is_active=True)
        return render(request, 'library.html', {'books' : books, 'rentals' : rentals})

def rent_book(request, book_id):
    if (request.user.is_authenticated()):
        book_set = Book.objects.filter(id=book_id, is_rented=False)
        if book_set.count() == 0:
            return render(request, 'action.html', {'response' : 'This book does not exist or is not available'})
        book = book_set[0]

        rental = Rental()
        rental.user = request.user
        rental.book = book
        rental.is_active = True

        book.is_rented = True

        book.save()
        rental.save()

        return render(request, 'action.html', {'response' : 'You rented: ' + str(book.title)})

def return_book(request, book_id):
    if (request.user.is_authenticated()):
        book_set = Book.objects.filter(id=book_id)
        if book_set.count() == 0:
            return render(request, 'action.html', {'response' : 'This book does not exist'})
        rented_book = book_set[0]

        rental_set = Rental.objects.filter(user=request.user, book=rented_book, is_active=True)
        if rental_set.count() == 0:
            return render(request, 'action.html', {'response' : 'You have not rented this book'})
        rental = rental_set[0]

        rented_book.is_rented = False
        rental.is_active = False

        rented_book.save()
        rental.save()

        return render(request, 'action.html', {'response' : 'Thank you for returning: ' + str(rented_book.title)})


