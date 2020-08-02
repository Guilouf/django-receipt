from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy

from receipt import models


class ReceiptList(ListView):
    model = models.Receipt


class ReceiptCreate(CreateView):
    success_url = reverse_lazy('receipt_list')
    model = models.Receipt
    fields = '__all__'


class ReceiptUpdate(UpdateView):
    success_url = reverse_lazy('receipt_list')
    model = models.Receipt
    fields = '__all__'


class EstablishmentList(ListView):
    model = models.Establishment


class EstablishmentCreate(CreateView):
    model = models.Establishment
    fields = '__all__'


class EstablishmentUpdate(UpdateView):
    model = models.Establishment
    fields = '__all__'


class EstablishmentDetail(DetailView):
    model = models.Establishment


class CompanyList(ListView):
    model = models.Company


class CompanyCreate(CreateView):
    model = models.Company
    fields = '__all__'


class CompanyUpdate(UpdateView):
    model = models.Company
    fields = '__all__'


class CompanyDetail(DetailView):
    model = models.Company


class TagList(ListView):
    model = models.Tag


class TagCreate(CreateView):
    model = models.Tag
    fields = '__all__'


class TagUpdate(UpdateView):
    model = models.Tag
    fields = '__all__'


class TagDetail(DetailView):
    model = models.Tag
