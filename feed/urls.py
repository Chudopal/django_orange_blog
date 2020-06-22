from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name="list-of-posts"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('authors/', views.AuthorListView.as_view(), name="list-of-authors"),
    path('authors/<int:pk>/', views.posts_of_user, name="posts-of-author"),
    path('posts/<int:pk>', views.my_posts, name='my-posts'),
]
