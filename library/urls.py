from django.urls import path

from library.views import BookListAPIView, CategoryListAPIView, BooksRelatedToCategoriesListApiView

urlpatterns = [
    # path('categories/', CategoryListAPIView.as_view()),
    # path('books/', BookListAPIView.as_view()),
    path('book-list/', BooksRelatedToCategoriesListApiView.as_view()),
]
