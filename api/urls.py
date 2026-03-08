from django.urls import path, include
from books.views import BookViewSet, CategoryViewSet, AuthorViewSet
from borrow.views import BorrowViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet, basename='autorhs')
router.register('borrows', BorrowViewSet, basename='borrows')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]