from django.urls import path

from library.views import BookListAPIView, CategoryListAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('books/', BookListAPIView.as_view()),
]
