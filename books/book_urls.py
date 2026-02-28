from django.urls import path
from books import views

urlpatterns = [
    path('', views.BookViewSet.as_view(), name='book-list'),
    path('<int:id>/', views.BookViewSet.as_view(), name='view-specific-book'),
]