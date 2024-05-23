from django.db import models
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Bo'lim")

    objects = models.Manager()

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=Category, related_name='books', verbose_name="Bo'lim")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    sub_title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Kitob chiqarilgan yil")
    author = models.CharField(max_length=255, verbose_name="Avtor")
    book_link = models.CharField(max_length=255, verbose_name="Kitob manzili", null=True, blank=True)
    book_file = models.FileField(upload_to='books/', null=True, blank=True, verbose_name='Kitob fayli',
                                 validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    isbn = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqt")
    update_time = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']
