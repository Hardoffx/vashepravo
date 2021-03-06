# Generated by Django 3.2.5 on 2021-08-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Ваш Email')),
                ('title', models.CharField(max_length=200, verbose_name='Предмет обращения')),
                ('message', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contactnumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
            ],
        ),
    ]
