from django.urls import path, include
from . import views
#/authors


urlpatterns = [
        path('', views.AuthorListView.as_view(), name="list-of-authors"),
        path('', include('django.contrib.auth.urls')),#registration
        path('<int:pk>', views.my_account, name='account'),
        path('<int:pk>/posts', views.posts_of_user, name="posts-of-author"),
        path('<int:pk>/followers', views.followers_of_user, name="followers-of-user"),
        path('<int:pk>/update', views.UpdateUser.as_view(), name='update-account'),
        path('signup', views.SignUpView.as_view(), name='signup'),
]