from django.db import models
from django.urls import reverse


class Tag(models.Model):
    class TagCategory(models.IntegerChoices):
        RECEIPT = 0, 'receipt'
        COMPANY = 1, 'company'
        BOTH = 2, 'both'

    name = models.CharField(max_length=200)
    category = models.PositiveSmallIntegerField(choices=TagCategory.choices)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={"pk": self.pk})


class Company(models.Model):
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True,
                                  limit_choices_to={'category__in': [Tag.TagCategory.COMPANY, Tag.TagCategory.BOTH]}
                                  )

    class Meta:
        ordering = ('-id',)  # newer first

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={"pk": self.pk})

    @property
    def get_total(self):
        """Sum of all receipt amount for an establishment, rounded to 2 places because sqlite does not
        support Decimal internally"""
        return f"{self.establishment_set.aggregate(sum=models.Sum('receipt__amount'))['sum']:0.2f}"


class Establishment(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    city = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('-id',)  # newer first

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('establishment_detail', kwargs={"pk": self.pk})

    @property
    def get_total(self):
        return self.receipt_set.total()


class ReceiptQueryset(models.QuerySet):
    def total(self):
        return f"{self.aggregate(sum=models.Sum('amount'))['sum']:0.2f}"


class Receipt(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True,
                                  limit_choices_to={'category__in': [Tag.TagCategory.RECEIPT, Tag.TagCategory.BOTH]}
                                  )
    comment = models.TextField(blank=True, null=True)

    liters = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # for gas stations

    objects = ReceiptQueryset.as_manager()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.amount}-{self.establishment}-{self.date}'
