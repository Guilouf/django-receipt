from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse

from django_filters.views import FilterView

from receipt import models, forms, filters


class ReceiptList(FilterView):
    model = models.Receipt
    paginate_by = 50
    template_name = 'receipt/receipt_list.html'
    filterset_class = filters.ReceiptFilter


class ReceiptCreate(CreateView):
    success_url = reverse_lazy('receipt_list')
    model = models.Receipt
    form_class = forms.ReceiptForm


class ReceiptFromEstablishmentCreate(CreateView):
    success_url = reverse_lazy('receipt_list')
    model = models.Receipt
    form_class = forms.EstablishmentReceiptForm

    def form_valid(self, form):
        """Links the new receipt to an existing establishment"""
        form.instance.establishment = models.Establishment.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class ReceiptUpdate(UpdateView):
    success_url = reverse_lazy('receipt_list')
    model = models.Receipt
    form_class = forms.ReceiptForm


class EstablishmentList(FilterView):
    model = models.Establishment
    paginate_by = 50
    template_name = 'receipt/establishment_list.html'
    filterset_class = filters.EstablishmentFilter


class EstablishmentCreate(CreateView):
    model = models.Establishment
    fields = '__all__'


class EstablishmentFromCompanyCreate(CreateView):
    model = models.Establishment
    form_class = forms.CompanyEstablishmentForm

    def form_valid(self, form):
        """Links the new establishment to an existing company"""
        form.instance.company = models.Company.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class EstablishmentUpdate(UpdateView):
    model = models.Establishment
    fields = '__all__'


class EstablishmentDetail(DetailView):
    model = models.Establishment


class CompanyList(FilterView):
    model = models.Company
    paginate_by = 50
    template_name = 'receipt/company_list.html'
    filterset_class = filters.CompanyFilter


class CompanyCreate(CreateView):
    model = models.Company
    fields = '__all__'

    def get_success_url(self):
        """Auto create an establishment for the new company, and redirect to its update page"""
        establishment = models.Establishment.objects.create(name=self.object.name, company=self.object)
        return reverse('establishment_update', kwargs={"pk": establishment.id})


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
