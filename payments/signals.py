# Автоматизация задач Celery
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payout
from .tasks import process_payout
@receiver(post_save, sender=Payout)
def update_payout_status(sender, instance, created, **kwargs):
	if created:
# Запускаем задачу process_payout при создании нового платежа
		process_payout.delay(instance.id)