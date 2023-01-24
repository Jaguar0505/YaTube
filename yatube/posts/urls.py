from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('', views.index, name="index"),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('justpage/',views.JustStaticPage.as_view()),
    path('about/author/',views.AboutAuthorView.as_view()),
    path('about/tech', views.AboutTechView.as_view()),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
