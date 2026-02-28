from django.urls import path
from borrow import views

urlpatterns = [
    path('', views.BorrowViewSet.as_view(), name='borrow-list'),
    path('<int:pk>/', views.BorrowViewSet.as_view(),
         name='view-specific-borrow')
]