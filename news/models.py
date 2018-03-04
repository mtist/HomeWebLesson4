from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=32)
    slug = models.SlugField(max_length=32)
    content = RichTextUploadingField('Контент')

    def __str__(self):
        return self.title
