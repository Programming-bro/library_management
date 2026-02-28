from django.urls import path
from users import views

urlpatterns = [
    path('', views.MemberViewSet.as_view(), name='member-list'),
    path('<int:pk>/', views.MemberViewSet.as_view(),
         name='view-specific-member')
]