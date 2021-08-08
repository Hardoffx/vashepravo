from django.db import models



class ContactModel(models.Model):
    name = models.CharField('Ваше имя', max_length=150)
    email = models.EmailField('Ваш Email')
    title = models.CharField('Предмет обращения', max_length=200)
    message = models.TextField('Сообщение', max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявки на Безпплатную Консультацию'
        verbose_name_plural = 'Заявки на Безпплатныи  Консультации'

    def __str__(self):
        return f'{self.name} - {self.email}'


class WebSite(models.Model):
    name_web_site = models.CharField(max_length=100, verbose_name='Введите Доменное имя данного сайта')

    class Meta:
        verbose_name = 'Доменное имя данного сайта'
        verbose_name_plural = 'Доменные имена данного сайта'


    def __str__(self):
        return self.name_web_site
