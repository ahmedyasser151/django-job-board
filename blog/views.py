from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, POST_CATEGORY

post_category = [category[0] for category in POST_CATEGORY]

def count_posts_for_each_category():
    num_posts = []

    for category in post_category:
        count = Post.objects.filter(category=category).count()
        num_posts.append([category,count])

    return num_posts

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    num_posts = count_posts_for_each_category()
    extra_context = {"post_category": post_category, 'num_posts':num_posts}
    template_name = "blog/blog.html"

def post_list(request):
    posts = Post.objects.filter(status=1).all()
    context = {"posts": posts, "post_category": post_category}
    return render(request, 'blog/blog.html', context=context)
