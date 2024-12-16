from django import forms
from .models import User, Message, NewsLetter, Mailing
from django.core.exceptions import ValidationError


forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа',
             'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите имя'  # Текст подсказки внутри поля
        })
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите email'})
        # self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Комментарий'})

    def clean_name(self):
        last_name = self.cleaned_data.get('name')
        if any(word in last_name.lower() for word in forbidden):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return last_name


class MessageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['topic', 'letter']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите имя'  # Текст подсказки внутри поля
        })
        self.fields['letter'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите имя'  # Текст подсказки внутри поля
        })
