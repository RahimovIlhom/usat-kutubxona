from rest_framework import serializers

from library.models import Book, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category')

    class Meta:
        model = Book
        fields = ['id', 'category', 'title', 'year', 'author', 'book_link', 'isbn', 'create_time', 'update_time']

    def get_category(self, obj):
        return CategorySerializer(obj.category).data


class BooksRelatedToCategoriesSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField('get_books')

    class Meta:
        model = Category
        fields = ['id', 'name', 'books']

    def get_books(self, obj):
        books = Book.objects.filter(category__id=obj.id)
        return BookSerializer(books, many=True).data
