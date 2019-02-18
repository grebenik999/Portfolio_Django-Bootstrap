from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/blog.html', {'blogs': blogs})


def singlePost(request, blog_id):
    detailBlog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/singlePost.html', {'single': detailBlog})
