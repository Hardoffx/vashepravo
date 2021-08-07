# Generated by Django 3.2.5 on 2021-07-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_achievementblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Видео на главной', max_length=30)),
                ('preview', models.ImageField(upload_to='static/videoimage', verbose_name='Превью для видео')),
                ('video', models.FileField(upload_to='static/videoimage', verbose_name='Выбери видео')),
            ],
        ),
        migrations.AlterModelOptions(
            name='infobox',
            options={'verbose_name': 'Настройки верхнего блок-бара', 'verbose_name_plural': 'Настройки верхнего блока-бара'},
        ),
        migrations.AlterField(
            model_name='achievementblock',
            name='amount',
            field=models.CharField(max_length=50, verbose_name='Количество (указать цифру)'),
        ),
        migrations.AlterField(
            model_name='achievementblock',
            name='icon',
            field=models.CharField(max_length=50, verbose_name='Иконка блока'),
        ),
        migrations.AlterField(
            model_name='achievementblock',
            name='text',
            field=models.CharField(max_length=150, verbose_name='Содержание блока'),
        ),
        migrations.AlterField(
            model_name='infobox',
            name='content',
            field=models.CharField(max_length=150, verbose_name='Содержание блока'),
        ),
        migrations.AlterField(
            model_name='infobox',
            name='icon',
            field=models.CharField(max_length=50, verbose_name='Иконка блока'),
        ),
        migrations.AlterField(
            model_name='infobox',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок блока'),
        ),
    ]