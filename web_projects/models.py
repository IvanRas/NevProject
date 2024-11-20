from django.db import models

# Create your models here.


class Recipient(models.Model):
    last_name = models.CharField(max_length=250, verbose_name='Ф.И.О.', help_text='Введите получателя')
    email = models.CharField(max_length=250, verbose_name='Email ', help_text='Введите получателя') # один к одному
    # связана с именем
    comment = models.TextField(max_length=250, verbose_name='комментарий', help_text='Введите комментарий')

    def __str__(self):
        return f'{self.last_name}'

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'


class Message(models.Model):
    topic = models.TextField(max_length=100, verbose_name='комментарий', help_text='Введите комментарий')
    letter = models.TextField(max_length=100, verbose_name='комментарий', help_text='Введите комментарий')

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Newsletter(models.Model):
    created_at = models.DateTimeField(verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    status = models.TextField(max_length=250, verbose_name='статус') # Статус строка: 'Завершена','Создана','Запущена'
    # Сообщение (внешний ключ на модель «Сообщение»).
    # Получатели («многие ко многим», связь с моделью «Получатель»).

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Mailing(models.Model):
    created_at = models.DateTimeField(verbose_name='дата создания')
    status = models.TextField(max_length=250, verbose_name='статус')
    # Ответ почтового сервера (текст).
    # Рассылка (внешний ключ на модель «Рассылка»).

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'