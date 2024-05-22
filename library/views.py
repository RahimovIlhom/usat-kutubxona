from rest_framework.generics import ListAPIView

from library.models import Book, Category
from library.serializers import BookSerializer, CategorySerializer, BooksRelatedToCategoriesSerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BooksRelatedToCategoriesListApiView(ListAPIView):
    serializer_class = BooksRelatedToCategoriesSerializer
    queryset = Category.objects.all()
