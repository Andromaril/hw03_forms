from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.contrib.auth.models import User
from django.shortcuts import redirect
from posts.forms import PostForm


User = get_user_model()


def index(request):
    """View - функция для главной страницы проекта."""

    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title_index = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title_index': title_index,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """View - функция для страницы с постами, отфильтрованными по группам."""

    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title_group = 'Записи сообщества'
    context = {
        'group': group,
        'posts': posts,
        'title_group': title_group,
        'page_obj': page_obj,

    }

    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    """View - функция для страницы с постами пользователя,
       вошедшего на сайт.
    """

    author = get_object_or_404(User, username=username)
    count = Post.objects.filter(author=author).count()
    paginator = Paginator(author.posts.all(), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'author': author,
               'count': count,
               'page_obj': page_obj,

               }
    return render(request, 'posts/profile.html', context)


def post_view(request, post_id):
    """View - функция для страницы определенного поста."""

    post = get_object_or_404(Post, pk=post_id)
    count = Post.objects.filter(author=post.author).count()

    context = {'post': post,
               'count': count,
               }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    """View - функция для создания поста."""

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            group = form.cleaned_data['group']
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', request.user.username)
        return render(request, 'posts/create_post.html', {"form": form})
    form = PostForm()
    return render(request, 'posts/create_post.html', {"form": form, })


def post_edit(request, post_id):
    """View - функция для редактирования проекта."""

    is_edit = True
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return redirect('/posts/%s' % post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_detail', post_id)
        return render(request, 'posts/create_post.html',
                      {"form": form, 'post': post, "is_edit": is_edit, })
    form = PostForm(instance=post)
    return render(request, 'posts/create_post.html',
                  {"form": form, 'post': post,
                   "is_edit": is_edit, })
