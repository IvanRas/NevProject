from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.core.mail import send_mail
from django.utils import timezone
from .forms import UserForm, MessageForm, NewsLetterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


from web_projects.models import NewsLetter, User, Message

# Create your views here.

# CRUD для получателей (Recipient)


# @method_decorator(cache_page(60 * 2), name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = cache.get('user_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('user_queryset', queryset, 60 * 2)
        return queryset


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user_list')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return UserForm
        if self.request.user.has_perm("catalog.can_unpublish_product"):
            return UserForm
        if self.request.user.has_perm("catalog.remove_any_product"):
            return UserForm
        return UserForm


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')


# CRUD для сообщений (Message)


class MessageListView(LoginRequiredMixin,ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'message_delete.html'
    success_url = reverse_lazy('message_list')

# CRUD для рассылок (Mailing)


class NewsLetterListView(LoginRequiredMixin, ListView):
    model = NewsLetter
    template_name = 'newsletter_list.html'
    context_object_name = 'newsletters'


class NewsLetterCreateView(LoginRequiredMixin, CreateView):
    model = NewsLetter
    form_class = NewsLetterForm
    template_name = 'newsletter_form.html'
    success_url = reverse_lazy('newsletter_list')


class NewsLetterUpdateView(LoginRequiredMixin, UpdateView):
    model = NewsLetter
    form_class = NewsLetterForm
    template_name = 'newsletter_form.html'
    success_url = reverse_lazy('newsletter_list')


class NewsLetterDeleteView(LoginRequiredMixin, DeleteView):
    model = NewsLetter
    template_name = 'newsletter_delete.html'
    success_url = reverse_lazy('newsletter_list')

# Генерация отчета и отправка рассылки


class SendMailingView(View):
    def post(self, request, mailing_id):
        mailing = self.get_object(mailing_id)
        recipients = mailing.recipients.all()

        # Инициация отправки
        for recipient in recipients:
            try:
                send_mail(
                    mailing.message.subject,
                    mailing.message.body,
                    'from@example.com',  # email from
                    [recipient.email],
                    fail_silently=False,
                )
                status = 'Успешно'
                server_response = 'Письмо отправлено успешно.'
            except Exception as e:
                status = 'Не успешно'
                server_response = str(e)

            # Сохранение попытки рассылки
            NewsLetter.objects.create(
                mailing=mailing,
                status=status,
                server_response=server_response
            )

        # Обновление статуса рассылки
        if mailing.status == 'Создана':
            mailing.status = 'Запущена'
            mailing.first_sent_at = timezone.now()
            mailing.save()

        return render(request, 'mailing_status.html', {'mailing': mailing})

    def get_object(self, mailing_id):
        return NewsLetter.objects.get(id=mailing_id)


# Главная страница

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_mailings'] = NewsLetter.objects.count()
        context['active_mailings'] = NewsLetter.objects.filter(status='Запущена').count()
        context['unique_recipients'] = User.objects.count()
        return context
