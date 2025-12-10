# Определяем задачу Celery
from celery import shared_task
from .models import Payout
@shared_task
def process_payout(payout_id):
	payout = Payout.objects.get(id=payout_id)
# Имитация длительной обработки
	import time
	time.sleep(10)
	payout.status = 'completed'
	payout.save()