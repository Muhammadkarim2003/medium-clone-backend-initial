from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticlesView

router = DefaultRouter()
router.register(r'', ArticlesView)  # Asosiy yo‘nalishda ro‘yxatga olish

urlpatterns = [
    path('articles/', include(router.urls)),  # /articles/ ga to‘g‘ri keladi
]
