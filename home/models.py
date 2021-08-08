from django.db import models



class Infobox(models.Model):
    icon = models.CharField(max_length=50, verbose_name='Иконка блока')
    title = models.CharField(max_length=50, verbose_name='Заголовок блока')
    content = models.CharField(max_length=150, verbose_name='Содержание блока')

    class Meta:
        verbose_name = 'Настройки верхнего блок-бара'
        verbose_name_plural = 'Настройки верхнего блока-бара'

    def __str__(self):
        return self.title


class AchievementBlock(models.Model):
    icon = models.CharField(max_length=50, verbose_name='Иконка блока')
    amount = models.CharField(max_length=50, verbose_name='Количество (указать цифру)')
    text = models.CharField(max_length=150, verbose_name='Содержание блока')

    class Meta:
        verbose_name = 'Настройки блока достижения'
        verbose_name_plural = 'Настройки блока достижения'

    def __str__(self):
        return self.text


class UploadVideo(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название', default='Видео на главной')
    preview = models.ImageField(upload_to='videoimage', verbose_name='Превью для видео')
    video = models.FileField(upload_to='videoimage', verbose_name='Выбери видео')

    class Meta:
        verbose_name = 'Загрузка видео на главную'
        verbose_name_plural = 'Загрузка видео на главную'

    def __str__(self):
        return self.name


class PracticeAreas(models.Model):
    icon = models.CharField(max_length=30, verbose_name='Иконка блока')
    title = models.CharField(max_length=30, verbose_name='Заголовок блока')
    createid = models.CharField(max_length=25, verbose_name='Присвой id блоку числом от 1 до ...')



    class Meta:
        verbose_name = 'Настройка блока Области практики'
        verbose_name_plural = 'Настройка блока Области практики'

    def __str__(self):
        return self.title


class LawyerCard(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя, Фамилия - юриста')
    lawyer_classification = models.CharField(max_length=30, verbose_name='В какой области практикует юрист?')
    image = models.ImageField(upload_to='lawyerimage', verbose_name='Фото в карточке юриста')
    text = models.TextField(max_length=190, verbose_name='Текст с зади карточки 190-символов')

    class Meta:
        verbose_name = 'Настройка карточки юриста'
        verbose_name_plural = 'Настройка карточек юриста'

    def __str__(self):
        return self.name


class VashePravoImg(models.Model):
    icon = models.CharField(max_length=30, verbose_name='Иконка блока')
    title = models.CharField(max_length=30, verbose_name='Заголовок блока')
    text = models.CharField(max_length=25, verbose_name='Содержание блока')
    image = models.ImageField(upload_to='vpimages', verbose_name='Картинка на фон блока')

    class Meta:
        verbose_name = 'Настройка блока слева от формы.беспл.конс:'
        verbose_name_plural = 'Настройка блока слева от формы.беспл.конс:'

    def __str__(self):
        return self.title


class Reviews(models.Model):
    image = models.ImageField(upload_to='revievsimages', verbose_name='Фото написавшего отзыв')
    text = models.CharField(max_length=120, verbose_name='Текст отзыва')
    name = models.CharField(max_length=20, verbose_name='Имя писавшего отзыв')

    class Meta:
        verbose_name = 'Написание отзывов от клиентов'
        verbose_name_plural = 'Написание отзывов от клиента'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя фото для отображения в Админке')
    image = models.ImageField(upload_to='gallery', verbose_name='Фото в галерею')

    class Meta:
        verbose_name = 'Добавление фото в галерею'
        verbose_name_plural = 'Добавление фото в галерею'

    def __str__(self):
        return self.name


class FooterNumber(models.Model):
    number = models.CharField(max_length=20, verbose_name='Введите номер телефона')

    class Meta:
        verbose_name = 'Настройка номеров в Футере'
        verbose_name_plural = 'Настройка номера в Футере'

    def __str__(self):
        return self.number


class Email(models.Model):
    create_email = models.CharField(max_length=30, verbose_name='Введите Email')

    class Meta:
        verbose_name = 'Настройка Email в футере'
        verbose_name_plural = 'Настройка Email в футере'

    def __str__(self):
        return self.create_email


class VkLink(models.Model):
    create_vk_link = models.CharField(max_length=150, verbose_name='Введите ссылку на "VK" включая "http://...."')
    name_vk = models.CharField(max_length=30, verbose_name='Назовите ссылку, так она будет отображаться на сайте:')

    class Meta:
        verbose_name = 'Настройка ссылки на "VK" в футере'
        verbose_name_plural = 'Настройка ссылки на "VK" в футере'

    def __str__(self):
        return self.create_vk_link


class WorkHours(models.Model):
    name_adm = models.CharField(max_length=35, verbose_name='Имя для отображения в админке, можно не менять',
                                   default='Рабочие дни и часы в неделе')
    work_days_1 = models.CharField(max_length=35, verbose_name='Рабочии дни с Пн по Пт',
                                   default='Понедельник - пятница:')
    work_tim_1 = models.CharField(max_length=35, verbose_name='Напишите рабочии часы, менять только цыфры',
                                  default='с 10:00 до 18:00')

    work_days_2 = models.CharField(max_length=35, verbose_name='Рабочии дни в Сб - Вс', default='Суббота:')
    work_time_2 = models.CharField(max_length=35, verbose_name='Напишите рабочии часы, менять только цыфры',
                                   default='с 10:00 до 15:00')
    week_days = models.CharField(max_length=35, verbose_name='Какие дни выходные?',
                                   default='Все воскресные дни.')
    holidays = models.CharField(max_length=35, verbose_name='Выхдные в какие праздники?',
                                   default='Все официальные праздники.')

    class Meta:
        verbose_name = 'Настройка Рабочих дней и часов в неделе'
        verbose_name_plural = 'Настройка Рабочих дней и часов в неделе'

    def __str__(self):
        return self.name_adm


class HaveQuestions(models.Model):
    address = models.CharField(max_length=150, verbose_name='Введите Адрес организации')

    class Meta:
        verbose_name = 'Настройка Адресов в футере'
        verbose_name_plural = 'Настройка Адреса в футере'

    def __str__(self):
        return self.address


class BackgroundHome(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя фото для отображения в админке',
                            default='Background на Главной')
    image = models.ImageField(upload_to='backgroundHome_images', verbose_name='Дабавьте фото')

    class Meta:
        verbose_name = 'Background Фото на Главной'
        verbose_name_plural = 'Background Фото на Главной'

    def __str__(self):
        return self.name
