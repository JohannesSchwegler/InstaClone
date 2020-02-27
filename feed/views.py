from __future__ import print_function
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
import json
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment, Like
from users.models import Follower
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class PostListView(ListView):
    model = Post
    template_name = "feed/index.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]  # "date_posted" for oldest to newest


class UserPostListView(ListView):
    model = Post
    template_name = "users/profile.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        current_user = self.request.user.id
        follower = Follower.objects.filter(
            user_id=current_user, follower_id=user.id).exists()

        postCount = Post.objects.filter(author=user.id).count()
        followed = Follower.objects.filter(follower_id=user.id).count()

        context['followed'] = followed
        context['postCount'] = postCount
        context['is_ownProfil'] = (user.id == current_user)
        context['is_follower'] = follower
        context['currentUser'] = self.request.user.username
        context['userProfile'] = user
        context['posts'] = Post.objects.filter(
            author=user).order_by('-date_posted')
        return context


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # field for the form , date will be filled in autmatically
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # before submit set author to current user
        form.instance.author = self.request.user
        return super().form_valid(form)  # pass form to parent

    def test_func(self):
        post = self.get_object()  # return current-post
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


@csrf_exempt
def addComment(request):
    if request.method == 'GET':
        do_something()

    elif request.method == 'POST':

        current_user = request.user
        comment = json.loads(request.body)["comment"]
        postId = json.loads(request.body)["postId"]
        Comment.objects.create(user_id=request.user.id,
                               post_id=postId, content=comment)

        return JsonResponse({"user": request.user.username, "comment": comment})


@csrf_exempt
def addLike(request):
    if request.method == 'GET':
        do_something()

    elif request.method == 'POST':

        current_user = request.user
        postId = json.loads(request.body)["postId"]
        try:
            liked = Like.objects.get(user_id=request.user.id, post_id=postId)
        except Like.DoesNotExist:
            liked = None

        if liked is None:
            Like.objects.create(user_id=request.user.id, post_id=postId)
            return JsonResponse({"user": request.user.username, "like": "add"})
        else:
            Like.objects.filter(user_id=request.user.id,
                                post_id=postId).delete()
            return JsonResponse({"user": request.user.username, "like": "remove"})


@csrf_exempt
def addFollower(request):
    if request.method == 'GET':
        do_something()

    elif request.method == 'POST':

        current_user = request.user.id
        userId = json.loads(request.body)["userId"]
        try:
            Follower.objects.create(follower_id=userId, user_id=current_user)

        except IntegrityError as e:
            print("geht net")

        print(userId)
        return JsonResponse({"user": request.user.username, "like": "remove"})


@csrf_exempt
def getFollowers(request):
    if request.method == 'POST':
        do_something()

    elif request.method == 'GET':
        userId = request.GET.dict()["userId"]
        followed = Follower.objects.filter(follower_id=userId)
        print(followed)
        listAll = []
        for i in followed:

            listAll.append(({"userimage": i.user.profile.image.url, "username": i.user.username,
                             "description": i.user.profile.description, "userId": i.user.id}))

        print(listAll)
        return JsonResponse({"list": listAll})
