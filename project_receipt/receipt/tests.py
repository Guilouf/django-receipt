from django.test import TestCase

from receipt.models import Receipt


class AmountsTestCase(TestCase):
    fixtures = ['receipt_test_fixture']

    def test_total_receipt_amount(self):
        """Check total amount of all existing tickets"""
        self.assertEqual(Receipt.objects.all().total(), '55.70')
