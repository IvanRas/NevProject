from django.db import models

# Create your models here.


class User(models.Model):
    last_name = models.CharField(max_length=250, verbose_name='Ф.И.О.', help_text='Введите получателя')
    email = models.EmailField(max_length=250, verbose_name='Email ', help_text='Введите Email', unique=True)
    comment = models.TextField(max_length=250, verbose_name='комментарий', help_text='Введите комментарий')
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'


class Message(models.Model):
    topic = models.TextField(max_length=100, verbose_name='тема', help_text='Введите тему')
    letter = models.TextField(verbose_name='сообщение', help_text='Введите сообщение')

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class NewsLetter(models.Model):
    STATUS_CHOICES = [
        ('Создана', 'Создана'),
        ('Запущена', 'Запущена'),
        ('Завершена', 'Завершена')
    ]

    first_sent_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Создана')
    # Статус строка: 'Завершена','Создана','Запущена'
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    # Сообщение (внешний ключ на модель «Сообщение»).
    recipients = models.ManyToManyField(User)
    # Получатели («многие ко многим», связь с моделью «Получатель»).
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.message.subject} - {self.status}"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        permissions = [
            ("can_activ_user", "Can activ user"),
            ("can_activ_newsletter", "Can activ newsletter"),
        ]


class Mailing(models.Model):
    STATUS_CHOICES = [
        ('Успешно', 'Успешно'),
        ('Не успешно', 'Не успешно')
    ]
    attempt_time = models.DateTimeField(verbose_name='дата создания')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # Статус строка: 'Завершена','Создана','Запущена'
    server_response = models.TextField(blank=True)
    # Ответ почтового сервера (текст).
    mailing = models.ForeignKey(NewsLetter, on_delete=models.CASCADE, related_name='send_attempts')
    # Рассылка (внешний ключ на модель «Рассылка»).

    def __str__(self):
        return f"Attempt: {self.attempt_time} - {self.status}"
