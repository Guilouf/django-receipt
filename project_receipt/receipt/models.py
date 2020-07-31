from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Receipt(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    shop = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'{self.amount}-{self.shop}-{self.date}'
