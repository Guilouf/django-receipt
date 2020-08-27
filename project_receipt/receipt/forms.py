from django import forms

from receipt import models


class ReceiptForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M')
    )

    class Meta:
        model = models.Receipt
        fields = '__all__'


class EstablishmentReceiptForm(ReceiptForm):
    class Meta:
        model = models.Receipt
        exclude = ('establishment',)


class CompanyEstablishmentForm(forms.ModelForm):

    class Meta:
        model = models.Establishment
        exclude = ('company',)
