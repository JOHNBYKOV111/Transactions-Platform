# Определение конфигурации
# Регистрация приложения 'payments', инициализация сигналов
# Подключение обработчиков событий из payments.signals
from django.apps import AppConfig
class PaymentsConfig(AppConfig):
	name = 'payments'

	def ready(self):
		import payments.signals