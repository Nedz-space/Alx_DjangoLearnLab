# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import SearchForm
from django.db.models import Q


def book_list(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        books = books.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        book = Book.objects.create(title=title, author_id=author)
        return redirect('book_list')
    return render(request, 'books/book_form.html')

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'book': book})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

def secure_view(request):
    response = render(request, 'bookshelf/secure_page.html')
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self'"
    return response
