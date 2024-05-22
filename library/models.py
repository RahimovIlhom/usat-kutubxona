from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kategoriya")

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=Category, related_name='books', verbose_name="Kategoriya")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    sub_title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Sarlavha osti")
    author = models.CharField(max_length=255, verbose_name="Avtor")
    book_link = models.CharField(max_length=255, verbose_name="Kitob manzili")
    isbn = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqt")
    update_time = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    objects = models.Manager()

    def __str__(self):
        return self.title
