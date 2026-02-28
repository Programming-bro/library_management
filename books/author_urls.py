from django.urls import path
from books import views

urlpatterns = [
    path('', views.AuthorViewSet.as_view(), name='author-list'),
    path('<int:id>/', views.AuthorViewSet.as_view(), name='view-specific-author'),
]