from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse

from receipt import models, forms


class ReceiptList(ListView):
    model = models.Receipt
    paginate_by = 50


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


class EstablishmentList(ListView):
    model = models.Establishment
    paginate_by = 50


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


class CompanyList(ListView):
    model = models.Company
    paginate_by = 50

    def setup(self, request, *args, **kwargs):
        # get param key name
        self.company_name_key = 'company_name'
        # get param value
        self.company_name_search_keyword = request.GET.get(self.company_name_key)
        super().setup(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(object_list=None, **kwargs)
        # form input name
        context_data['company_name_key'] = self.company_name_key

        if self.company_name_search_keyword:
            # to keep search string in input box across pagination
            context_data['company_name_keyword'] = self.company_name_search_keyword
            # to be appended to url get params
            context_data['search_params'] = f'&{self.company_name_key}={self.company_name_search_keyword}'
        return context_data

    def get_queryset(self):
        """Filter companies which have corresponding string in their names"""
        qs = super().get_queryset()
        return qs.filter(name__icontains=self.company_name_search_keyword)\
            if self.company_name_search_keyword else qs


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
