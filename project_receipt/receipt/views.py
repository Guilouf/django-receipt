from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from receipt import models, forms


class ReceiptList(ListView):
    model = models.Receipt


class ReceiptCreate(CreateView):
    success_url = reverse_lazy('receipt_list')  # or get_absolute_url() if detail
    model = models.Receipt
    form_class = forms.ReceiptForm


class ReceiptUpdate(UpdateView):
    success_url = reverse_lazy('receipt_list')
    model = models.Receipt
    form_class = forms.ReceiptForm

