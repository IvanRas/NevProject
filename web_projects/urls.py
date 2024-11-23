"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import index

from django.urls import path

from web_projects.apps import WebProjectsConfig
from web_projects.views import UserCreateView, UserDetailView, HomeListView, UserUpdateView, UserDeleteView, UserListView

app_name = WebProjectsConfig.name


urlpatterns = [
    path('', HomeListView.as_view(), name="user"),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/', UserListView.as_view(), name='user'),
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete')
]
