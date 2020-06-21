from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name="list-of-posts"),
    path('<int:pk>', views.PostDetailView.as_view(), name="post-detail"),
]