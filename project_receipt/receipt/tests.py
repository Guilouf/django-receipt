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

    def setUp(self) -> None:
        self.establishment = Establishment.objects.first()

        self.tag_receipt = Tag.objects.create(category=Tag.TagCategory.RECEIPT)
        self.tag_company = Tag.objects.create(category=Tag.TagCategory.COMPANY)
        self.tag_both = Tag.objects.create(category=Tag.TagCategory.BOTH)

        self.receipt_urls = [
            reverse('receipt_create'),
            reverse('receipt_update', args=[self.establishment.id]),
            reverse('establishment_add_receipt', args=[self.establishment.id])
        ]

        self.receipt_form_data = {'amount': 20.35,
                                  'date': '2021-04-06T15:02',
                                  'establishment': self.establishment.id}

    def test_receipt_allowed_tags(self):
        for url in self.receipt_urls:
            with self.subTest(url=url):
                # allowed tags
                data = {**self.receipt_form_data,
                        'tags': [self.tag_receipt.id, self.tag_both.id]
                        }
                response = self.client.post(url, data)
                self.assertEqual(response.status_code, 302)  # redirect

                # not allowed tags
                data = {**self.receipt_form_data,
                        'tags': [self.tag_company.id]
                        }
                response = self.client.post(url, data)
                # todo validation error
                print(list(response.context['messages']))
                self.assertNotEqual(response.status_code, 302)  # redirect


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
