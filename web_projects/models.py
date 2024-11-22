from django.db import models

# Create your models here.

CHOICES = {'Завершена', 'Создана', 'Запущена'}
STATUS = {'Успешно', 'Не успешно'}


class Recipient(models.Model):
    last_name = models.CharField(max_length=250, verbose_name='Ф.И.О.', help_text='Введите получателя')
    email = models.CharField(max_length=250, verbose_name='Email ', help_text='Введите получателя', unique=True)
    comment = models.TextField(max_length=250, verbose_name='комментарий', help_text='Введите комментарий')

    def __str__(self):
        return f'{self.last_name}'

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'


class Message(models.Model):
    topic = models.TextField(max_length=100, verbose_name='тема', help_text='Введите тему')
    letter = models.TextField(max_length=100, verbose_name='сообщение', help_text='Введите сообщение')

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class NewsLetter(models.Model):
    created_at = models.DateTimeField(verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    status = models.CharField(max_length=250, verbose_name='статус', choices=CHOICES)
    # Статус строка: 'Завершена','Создана','Запущена'
    receiver = models.ForeignKey(Message, on_delete=models.CASCADE)
    # Сообщение (внешний ключ на модель «Сообщение»).
    recipients = models.CharField("Recipient", related_name="last_name")
    # Получатели («многие ко многим», связь с моделью «Получатель»).


class Mailing(models.Model):
    created_at = models.DateTimeField(verbose_name='дата создания')
    status = models.CharField(max_length=250, verbose_name='статус')
    # Статус строка: 'Завершена','Создана','Запущена'
    aswer = models.TextField(max_length=250)
    # Ответ почтового сервера (текст).

    recipients = models.CharField("Recipient", related_name="last_name")
    # Рассылка (внешний ключ на модель «Рассылка»).
