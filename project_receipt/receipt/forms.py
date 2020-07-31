from django import forms

from receipt import models


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = models.Receipt
        fields = '__all__'
