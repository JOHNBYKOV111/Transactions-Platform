# Unit-тест задачи process_payout.
from django.test import TestCase
from payments.tasks import process_payout
from payments.models import Payout
class ProcessPayoutTaskTest(TestCase):
	def test_process_payout(self):
			payout = Payout.objects.create(
					amount=100.00,
					currency='USD',
					recipient_details={
							'name': 'John Doe',
							'account_number': '1234567890'
					},
					comment='Test payment'
			)
			process_payout(payout.id)
			payout.refresh_from_db()
			self.assertEqual(payout.status, 'completed')