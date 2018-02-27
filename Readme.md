# ДЗ №4

## Django

**Перед началом обязательно форкнуть и склонировать к себе свой форк.** 

### Подготовка

Все то же что и всегда.

    git clone

затем открываем проект в pycharm и подключаем к venv.

### Подключить ckeditor к проекту

Репозиторий пакета https://github.com/django-ckeditor/django-ckeditor.

ckeditor позволяет подключить к проекту wysiwyg редактор.

#### Установка и настройка ckeditor

устанавливаем пакет:

    pip install django-ckeditor


Добавляем в конец settings.py следующие конфиги:

```python
STATIC_ROOT = os.path.join(BASE_DIR, '../static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
CKEDITOR_UPLOAD_PATH = '/uploads/'
```

также в settings.py в конец INSTALLED_APPS нужно добавить 'ckeditor' и 'ckeditor_uploader'


urls.py должен быть таким:

```python
from django.contrib import admin
from django.urls import path, include
from pages.views import home, pages
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', home, name='home'),
    path('<slug:slug>', pages, name='pages'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
в urls.py мы подключили media для локального сервара и подключили к урлам сам ckeditor


теперь поменяем тип поля content для модили Page.
для это переходим в pages/models.py
импортируем новый тип поля из ckeditor, добавляем эту строку там где импорты

```python
from ckeditor_uploader.fields import RichTextUploadingField
```

и используем этот тип поля поменяв поля для content:

```python
content = RichTextUploadingField('Контент')
```

теперь так как мы изменили модель, необходимо создать миграции и применить их.

    makemigrations
    migrate

Запускаем проект и смотрим работает ли все в админке.

Также добавьте еще пару страниц в pages через админку используя удобный ckeditor(например услуги)

### Доп задание. Создать app news - т.е. добавляем новости к сайту

принцип такой же как и в pages

сначала должны запустить manage команду:

    startapp news

потом в появившемся news заходим в models.py и добавляем модель Article

    class Article(models.Model):

и дальше так же как и в pages добавляем поля. Можно использовать теже поля что и в pages,
поменяв им названия

