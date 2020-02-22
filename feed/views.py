from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


class PostListView(ListView):
    model = Post
    template_name= "feed/index.html"   #<app>/<model>_<viewtype>.html
    context_object_name="posts"
    ordering=["-date_posted"]         #"date_posted" for oldest to newest



class UserPostListView(ListView):
    model = Post
    template_name= "users/profile.html"   #<app>/<model>_<viewtype>.html
    context_object_name="posts"


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context['posts'] = Post.objects.filter(author=user).order_by('-date_posted')
        context['posts'] = Post.objects.filter(author=user).order_by('-date_posted')
        return context

   




class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']          # field for the form , date will be filled in autmatically

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user     #before submit set author to current user
        return super().form_valid(form)              #pass form to parent

    def test_func(self):
        post = self.get_object()                     #return current-post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})