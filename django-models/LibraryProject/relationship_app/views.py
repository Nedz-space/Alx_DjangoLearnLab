# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
    
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# User Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, 'relationship_app/logout.html')

def check_role(role):
    def _check(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return _check

def check_admin(user):
    return user.userprofile.role == 'Admin'

def check_librarian(user):
    return user.userprofile.role == 'Librarian'

def check_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(check_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin! You have exclusive access.")

@login_required
@user_passes_test(check_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian! You have access to librarian resources.")

@login_required
@user_passes_test(check_member)
def member_view(request):
    return HttpResponse("Welcome, Member! Enjoy your access.")
