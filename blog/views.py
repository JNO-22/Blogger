from django.shortcuts import render
from blog.models import Post

def blog_index(req):
    posts= Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts
    }
    return render(req, "blog/index.html", context)

def blog_category(req, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(req, "blog/category.html", context)

def blog_detail(req,pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(req, "blog/detail.html", context)