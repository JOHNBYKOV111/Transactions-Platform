# Unit-тесты модели Payout.
from django.test import TestCase
from payments.models import Payout
class PayoutModelTest(TestCase):
	def test_create_payout(self):
		payout = Payout.objects.create(
				amount=100.00,
				currency='USD',
				recipient_details={
						'name': 'John Doe',
						'account_number': '1234567890'
				},
				comment='Test payment'
		)
		self.assertEqual(payout.amount, 100.00)
		self.assertEqual(payout.currency, 'USD')
		self.assertEqual(payout.status, 'pending')

	def test_str_representation(self):
		payout = Payout.objects.create(
				amount=100.00,
				currency='USD',
				recipient_details={
						'name': 'John Doe',
						'account_number': '1234567890'
				},
				comment='Test payment'
		)
		expected_str = f"Платеж №{payout.id}, сумма: {payout.amount} {payout.currency}"
		self.assertEqual(str(payout), expected_str)