# Регистрируем ViewSet в URL
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.views import PayoutViewSet
# Создаем роутер
router = DefaultRouter()
router.register(r'payouts', PayoutViewSet)
# Маршруты
urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include(router.urls)),
	path('', include('payments.urls')),
]