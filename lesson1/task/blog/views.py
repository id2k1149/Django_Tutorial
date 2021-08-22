from django.shortcuts import render

from .models import Post


def post_list(request):
    # get all posts ordered by published_date
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
