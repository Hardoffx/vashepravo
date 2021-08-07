from django.db import models


class Contactnumber(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number


class ContactModel(models.Model):
    name = models.CharField('Ваше имя', max_length=150)
    email = models.EmailField('Ваш Email')
    title = models.CharField('Предмет обращения', max_length=200)
    message = models.TextField('Сообщение', max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'