# Формеруем модели для обработки заявок
from django.db import models
class Payout(models.Model):
	STATUS_CHOICES = [
		('pending', 'Ожидает обработки'),
		('processing', 'Обрабатывается'),
		('completed', 'Завершена'),
		('failed', 'Ошибка'),
	]

	amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
	currency = models.CharField(max_length=3, verbose_name="Валюта")
	recipient_details = models.JSONField(verbose_name="Реквизиты получателя")
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
	comment = models.TextField(null=True, blank=True, verbose_name="Комментарий")

	def __str__(self):
		return f"Платеж №{self.id}, сумма: {self.amount} {self.currency}"

	class Meta:
		verbose_name = "Заявка на выплату"
		verbose_name_plural = "Заявки на выплату"