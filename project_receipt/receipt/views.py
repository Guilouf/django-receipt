from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy

from receipt import models


class ReceiptList(ListView):
    model = models.Receipt


class ReceiptCreate(CreateView):
    success_url = reverse_lazy('receipt_list')  # or get_absolute_url() if detail
    model = models.Receipt
    fields = '__all__'


class ReceiptUpdate(UpdateView):
    success_url = reverse_lazy('receipt_list')
    model = models.Receipt
    fields = '__all__'


class EstablishmentList(ListView):
    model = models.Establishment


class EstablishmentCreate(CreateView):
    success_url = reverse_lazy('establishment_list')
    model = models.Establishment
    fields = '__all__'


class EstablishmentUpdate(UpdateView):
    success_url = reverse_lazy('establishment_list')
    model = models.Establishment
    fields = '__all__'


class EstablishmentDetail(DetailView):
    model = models.Establishment


class CompanyList(ListView):
    model = models.Company


class CompanyCreate(CreateView):
    success_url = reverse_lazy('company_list')
    model = models.Company
    fields = '__all__'


class CompanyUpdate(UpdateView):
    success_url = reverse_lazy('company_list')
    model = models.Company
    fields = '__all__'


class CompanyDetail(DetailView):
    model = models.Company
