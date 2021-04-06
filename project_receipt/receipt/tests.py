from django.test import TestCase

from receipt.models import Receipt, Establishment, Company


class AmountsTestCase(TestCase):
    fixtures = ['receipt_test_fixture']

    def test_total_receipt_amount(self):
        """Check total amount of all existing tickets"""
        self.assertEqual(Receipt.objects.all().total(), '66.05')

    def test_establishment_total(self):
        """Check correct answer for total in each establishment"""
        answers = ['50.35', '5.35', '10.35']
        self.assertEqual(len(answers), Establishment.objects.count())
        for establishment, answer in zip(Establishment.objects.all().order_by('id'),
                                         answers):
            with self.subTest(establishment=establishment):
                self.assertEqual(establishment.get_total, answer)

    def test_company_total(self):
        """Check correct answer for total in each company"""
        answers = ['55.70', '10.35']
        self.assertEqual(len(answers), Company.objects.count())
        for company, answer in zip(Company.objects.all().order_by('id'),
                                   answers):
            with self.subTest(company=company):
                self.assertEqual(company.get_total, answer)
