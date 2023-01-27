from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group , User
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context = { 'page_obj' : page_obj}
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = author.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'author':author,
    'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.select_related('author','group'),id=post_id)
    post_list = post.author.posts.all()
    context = {'post':post,
    'post_list':post_list,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', request.user)
    return render(request, 'posts/create_post.html', {'form': form})



class JustStaticPage(TemplateView):
    template_name = 'app_name/just_page.html'

class AboutAuthorView(TemplateView):
    template_name = 'app_name/author.html'

class AboutTechView(TemplateView):
    template_name = 'app_name/tech.html'