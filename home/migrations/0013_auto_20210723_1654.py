# Generated by Django 3.2.5 on 2021-07-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery', verbose_name='Фото в галерею')),
            ],
            options={
                'verbose_name': 'Добавление фото в галерею',
                'verbose_name_plural': 'Добавление фото в галерею',
            },
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Написание отзывов от клиентов', 'verbose_name_plural': 'Написание отзывов от клиента'},
        ),
    ]