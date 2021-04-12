from django.test import TestCase
from django.urls import reverse

from receipt.models import Receipt, Establishment, Company, Tag
from receipt.forms import ReceiptForm


class AmountsTestCase(TestCase):
    fixtures = ['receipt_test_fixture']

    def test_total_receipt_amount(self):
        """Check total amount of all existing tickets"""
        self.assertEqual(Receipt.objects.all().total(), '66.05')

    def test_establishment_total(self):
        """Check correct answer for total in each establishment"""
        answers = ['50.35', '5.35', '10.35', '0.00']
        self.assertEqual(len(answers), Establishment.objects.count())
        for establishment, answer in zip(Establishment.objects.all().order_by('id'),
                                         answers):
            with self.subTest(establishment=establishment):
                self.assertEqual(establishment.get_total, answer)

    def test_company_total(self):
        """Check correct answer for total in each company"""
        answers = ['55.70', '10.35', '0.00']
        self.assertEqual(len(answers), Company.objects.count())
        for company, answer in zip(Company.objects.all().order_by('id'),
                                   answers):
            with self.subTest(company=company):
                self.assertEqual(company.get_total, answer)


class ViewTestCase(TestCase):
    fixtures = ['basic_establishment']

    def setUp(self) -> None:
        self.establishment = Establishment.objects.first()
        self.company = Company.objects.first()

    def test_create_linked_receipt_from_establishment(self):
        """Ensure that receipt is automatically linked with the correct
        establishment"""
        url = reverse('establishment_add_receipt', args=[self.establishment.id])
        self.assertEqual(self.establishment.receipt_set.count(), 0)

        data = {'amount': 20.35,
                'date': '2021-04-06T15:02'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.establishment.receipt_set.count(), 1)

    def test_create_linked_establishment_from_company(self):
        """Ensure that establishment is automatically linked with the correct
        company"""
        url = reverse('company_add_establishment', args=[self.company.id])
        self.assertEqual(self.company.establishment_set.count(), 1)

        data = {'name': 'Aldi in Dijon'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.company.establishment_set.count(), 2)


class FormsTestCase(TestCase):
    fixtures = ['basic_establishment']

    def setUp(self) -> None:
        self.establishment = Establishment.objects.first()

        self.tag_receipt = Tag.objects.create(category=Tag.TagCategory.RECEIPT)
        self.tag_company = Tag.objects.create(category=Tag.TagCategory.COMPANY)
        self.tag_both = Tag.objects.create(category=Tag.TagCategory.BOTH)

    def test_receipt_form(self):
        receipt_form_data = {'amount': 20.35,
                             'date': '2021-04-06T15:02',
                             'establishment': self.establishment.id
                             }

        # Allowed tags
        form_data = {**receipt_form_data,
                     'tags': [self.tag_receipt.id, self.tag_both.id]
                     }
        form = ReceiptForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Not allowed tags
        form_data = {**receipt_form_data,
                     'tags': [self.tag_company.id]
                     }
        form = ReceiptForm(data=form_data)
        self.assertFalse(form.is_valid())
