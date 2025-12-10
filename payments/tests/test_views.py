# Интеграционные тесты API PayoutViewSet + index view (APIClient + БД + Celery)
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from payments.models import Payout
from payments.tasks import process_payout

class PayoutViewTest(TestCase):
	def setUp(self):
			self.client = APIClient()

	def test_create_payout(self):
			response = self.client.post('/api/payouts/', {
					'amount': 100.00,
					'currency': 'USD',
					'recipient_details': {
							'name': 'John Doe',
							'account_number': '1234567890'
					},
					'comment': 'Test payment'
			}, format='json')
			self.assertEqual(response.status_code, status.HTTP_201_CREATED)
			self.assertIn('id', response.data)
			payout = Payout.objects.get(id=response.data['id'])
			self.assertEqual(payout.status, 'pending')

	def test_create_payout_celery_called(self):
			response = self.client.post('/api/payouts/', {
					'amount': 200.00,
					'currency': 'EUR',
					'recipient_details': {'name': 'Celery', 'account_number': '999'},
					'comment': 'Celery test'
			}, format='json')
			self.assertEqual(response.status_code, status.HTTP_201_CREATED)
			payout = Payout.objects.get(id=response.data['id'])
			self.assertEqual(payout.status, 'pending')

	def test_index_view(self):
			response = self.client.get('/')
			self.assertEqual(response.status_code, 200)
