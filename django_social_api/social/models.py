from django.core.exceptions import RequestDataTooBig
from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=255)
    login = models.CharField('Логин', max_length=255, unique=True)
    password = models.CharField('Пароль', max_length=255)
    last_login = models.TimeField(
        verbose_name='Время последнего логина', auto_now=True)
    last_request = models.TimeField(
        verbose_name='Время последнего запроса', auto_now=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login


class Post(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Картинка поста')
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', default='')


class Like(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Пользователь', null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, verbose_name='Публикация', null=True, on_delete=models.CASCADE)
    added_date = models.DateField('Дата лайка', auto_now_add=True)

    def __str__(self):
        return self.user + ' -> ' + self.post + ' ->' + self.added_date
