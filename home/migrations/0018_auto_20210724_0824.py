# Generated by Django 3.2.5 on 2021-07-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210724_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='create_email',
            field=models.CharField(max_length=30, verbose_name='Введите Email'),
        ),
        migrations.AlterField(
            model_name='vklink',
            name='create_vk_link',
            field=models.CharField(max_length=150, verbose_name='Введите ссылку на "VK" включая "http://...."'),
        ),
        migrations.AlterField(
            model_name='vklink',
            name='name_vk',
            field=models.CharField(max_length=30, verbose_name='Назовите ссылку, так она будет отображаться на сайте:'),
        ),
    ]