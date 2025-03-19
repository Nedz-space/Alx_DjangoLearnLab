# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')


# List all posts (public)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # template path
    context_object_name = 'posts'
    ordering = ['-created_at']  # latest posts first

# Post detail view (public)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # template path
    context_object_name = 'post'

# Create a post (login required)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    form_class = 'PostForm'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update a post (author only)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    form_class = 'PostForm'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete a post (author only)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
