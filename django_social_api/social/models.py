from django.core.exceptions import RequestDataTooBig
from django.db import models
from django.db.models import Count

class SocialUser(models.Model):
    name = models.CharField('Имя', max_length=255)
    login = models.CharField('Логин', max_length=255, unique=True)
    password = models.CharField('Пароль', max_length=255)
    last_login = models.TimeField(
        verbose_name='Время последнего логина', auto_now_add=True)
    last_request = models.TimeField(
        verbose_name='Время последнего запроса', auto_now=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login


class Post(models.Model):
    user = models.ForeignKey(
        SocialUser, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='user')
    image = models.ImageField(verbose_name='Картинка поста')
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', default='')


class Like(models.Model):
    user = models.ForeignKey(
        SocialUser, verbose_name='Пользователь', null=True, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(
        Post, verbose_name='Публикация', null=True, on_delete=models.CASCADE, related_name='post_like')
    added_date = models.DateField('Дата лайка', auto_now_add=True)
    liked = models.BooleanField(verbose_name='Лайкнули?', default=True)
    def __str__(self):
        return self.user.login + ' -> ' + self.post.name + ' ->' + str(self.added_date)
