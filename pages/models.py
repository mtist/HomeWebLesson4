from django.db import models


class Page(models.Model):
    title = models.CharField('Заголовок', max_length=32)
    slug = models.SlugField(max_length=32)
    content = models.TextField('Контент')

    def __str__(self):
        return self.title
