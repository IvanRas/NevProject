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
from web_projects.views import (UserCreateView, HomeView, UserUpdateView, UserDeleteView, UserListView, SendMailingView,
                                NewsLetterUpdateView, NewsLetterCreateView, NewsLetterDeleteView, NewsLetterListView,
                                MessageUpdateView, MessageDeleteView, MessageListView, MessageCreateView)

app_name = WebProjectsConfig.name


urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('user/', UserListView.as_view(), name='user_list'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    path('messages/', MessageListView.as_view(), name='messages_list'),
    path('messages/create/', MessageCreateView.as_view(), name='messages_create'),
    path('messages/update/<int:pk>/', MessageUpdateView.as_view(), name='messages_update'),
    path('messages/delete/<int:pk>/', MessageDeleteView.as_view(), name='messages_delete'),

    path('newsletter/', NewsLetterListView.as_view(), name='newsletter_list'),
    path('newsletter/create/', NewsLetterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/update/<int:pk>/', NewsLetterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/delete/<int:pk>/', NewsLetterDeleteView.as_view(), name='newsletter_delete'),

    path('send-mailing/<int:mailing_id>/', SendMailingView.as_view(), name='send_mailing'),

]
