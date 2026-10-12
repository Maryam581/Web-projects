from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    
    path('test/', views.RestTest, name='test'),
    path('test/', views.RestTest, name='test'),
    path('', include(router.urls)),
]
	