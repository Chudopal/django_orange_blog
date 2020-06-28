from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name="list-of-posts"),
    path('authors/', views.AuthorListView.as_view(), name="list-of-authors"),
    path('<int:pk>/', views.post_detail_view, name='post-detail'),
    path('authors/<int:pk>/', views.posts_of_user, name="posts-of-author"),
    path('posts/<int:pk>', views.my_posts, name='my-posts'),
    path('posts/create/', views.CreatePost.as_view(), name='create-post'),
    path('posts/<int:pk>/update/', views.UpdatePost.as_view(), name='update-post'),
    path('posts/<int:pk>/delete/', views.DeletePost.as_view(), name='delete-post'),
]
