from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category
from .constants import INDEX_PUBL_NUM


def get_published_posts():
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def post_detail(request, post_id):
    post = get_object_or_404(get_published_posts(), id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = get_published_posts().filter(category=category)
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })


def index(request):
    post_list = get_published_posts()[:INDEX_PUBL_NUM]
    return render(request, 'blog/index.html', {'post_list': post_list})
