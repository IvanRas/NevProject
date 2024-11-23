from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView


from web_projects.models import Mailing, User, Message, Mailing

# Create your views here.


class UserListView(ListView):
    model = User
    template_name = 'user/home.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(publication_sign=True)


class UserCreateView(CreateView):
    model = User
    fields = ['last_name', 'email', 'comment']
    template_name = 'web_projects/user_form.html'
    success_url = reverse_lazy('web_projects:home')


class UserDetailView(DetailView):
    model = User
    template_name = 'web_projects/user.html'
    context_object_name = 'user'

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.count_of_views += 1
    #     self.object.save()
    #     return self.object


class UserUpdateView(UpdateView):
    model = User
    fields = ['last_name', 'comment']
    template_name = 'web_projects/user_form.html'
    success_url = reverse_lazy('web_projects:home')

    def get_success_url(self):
        return reverse('user:user_detail', args=[self.kwargs.get('pk')])


class UserDeleteView(DeleteView):
    model = User
    template_name = 'web_projects/user_delete.html'
    success_url = reverse_lazy('blog:home')


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

