from django.db import models


class AuthorModelViewSet(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.IntegerField()


class BookModelViewSet(models.Model):
    pass


class BiographyModelViewSet(models.Model):
    pass


class ArticlesModelViewSet(models.Model):
    pass