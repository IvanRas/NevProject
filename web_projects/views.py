from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView


from web_projects.models import NewsLetter, Message, Message, Mailing

# Create your views here.


class NewsLetterCreateView(CreateView):
    model = NewsLetter
    fields = ['created_at', 'updated_at', 'status', 'receiver', 'recipients']
    template_name = 'web_projects/blog_form.html'
    success_url = reverse_lazy('web_projects:home')


class NewsLetterDetailView(DetailView):
    model = NewsLetter
    template_name = 'web_projects/blog.html'
    context_object_name = 'newsletter'


class NewsLetterUpdateView(UpdateView):
    model = NewsLetter
    fields = ['status', 'receiver', 'recipients']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('web_projects:home')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])



class NewsLetterDeleteView(DeleteView):
    model = NewsLetter
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('web_projects:home')


class Null():
    success_url = reverse_lazy('web_projects:home')


class HomeListView(ListView):
    model = NewsLetter
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


class CatalogContactsView(View):
    def get(self, request):
        return render(request, 'web_projects/contacts.html')

    def post(self, request):
        #Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductDetailView(DetailView):
    model = NewsLetter
    template_name = 'web_projects/product_detail.html'
    context_object_name = 'newsletter'
