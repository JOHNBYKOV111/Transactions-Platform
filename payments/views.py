# Представления для выплат
# API для получения и создания выплат с автозапуском Celery при создании
# Данные для охвата тестов
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Payout
from .serializers import PayoutSerializer
from .tasks import process_payout
class PayoutViewSet(viewsets.ModelViewSet):
	queryset = Payout.objects.all()
	serializer_class = PayoutSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		process_payout.delay(serializer.instance.id)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def index(request):
	return render(request, 'index.html')
