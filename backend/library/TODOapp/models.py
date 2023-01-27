from django.db import models


class User(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя пользователя')
    surname = models.CharField(max_length=25, verbose_name='Фамилия пользователя')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Project(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя проекта')
    url = models.URLField(max_length=255, verbose_name='Ссылка на репозиторий')
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class TODO(models.Model):
    text = models.TextField(verbose_name='Текст заметки')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, verbose_name='Заметка к проекту')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заметки')
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='Дата редактирования')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    status = models.BooleanField(default=True, verbose_name='Статус заметки')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
