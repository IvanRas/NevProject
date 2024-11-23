from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView


from web_projects.models import NewsLetter, User, Message, Mailing

# Create your views here.

# CRUD для получателей (Recipient)


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    fields = ['last_name', 'email', 'comment']
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')


class UserUpdateView(UpdateView):
    model = User
    fields = ['last_name', 'comment']
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')


# CRUD для сообщений (Message)


class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MessageCreateView(CreateView):
    model = Message
    fields = ['topic', 'letter']
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['topic', 'letter']
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('message_list')

# CRUD для рассылок (Mailing)


class NewsLetterListView(ListView):
    model = NewsLetter
    template_name = 'newsletter_list.html'
    context_object_name = 'newsletters'


class NewsLetterCreateView(CreateView):
    model = NewsLetter
    fields = ['end_at', 'message', 'recipients']
    template_name = 'newsletter_form.html'
    success_url = reverse_lazy('newsletter_list')


class NewsLetterUpdateView(UpdateView):
    model = NewsLetter
    fields = ['end_at', 'message', 'recipients']
    template_name = 'newsletter_form.html'
    success_url = reverse_lazy('newsletter_list')


class NewsLetterDeleteView(DeleteView):
    model = NewsLetter
    template_name = 'newsletter_delete.html'
    success_url = reverse_lazy('newsletter_list')





class HomeListView(ListView):
    model = User
    template_name = 'web_projects/base.html'
    context_object_name = 'products'


def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


class WebProjectsContactsView(View):
    def get(self, request):
        return render(request, 'web_projects/contacts.html')

    def post(self, request):
        #Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

