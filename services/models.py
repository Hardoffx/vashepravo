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

