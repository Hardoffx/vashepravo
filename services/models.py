from django.db import models


class ServicesDescription(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название услуги')
    content = models.TextField(verbose_name='Описание услуги')

    def get_summary(self):
        return self.content[:70]

    class Meta:
        verbose_name = 'Создание-Редактирование услуг'
        verbose_name_plural = 'Создание-Редактирование услуг'

    def __str__(self):
        return self.title


class BackgroundServices(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя фото для отображения в админке',
                            default='Background на странице Услуг')
    image = models.ImageField(upload_to='backgroundHome_images', verbose_name='Дабавьте фото')

    class Meta:
        verbose_name = 'Background Фото на странице Услуг'
        verbose_name_plural = 'Background Фото на странице Услуг'

    def __str__(self):
        return self.name
