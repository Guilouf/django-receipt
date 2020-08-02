from django.urls import path

from receipt import views

urlpatterns = [
    path('receipt/', views.ReceiptList.as_view(), name='receipt_list'),
    path('receipt/create', views.ReceiptCreate.as_view(), name='receipt_create'),
    path('receipt/<int:pk>/edit', views.ReceiptUpdate.as_view(), name='receipt_update'),
    path('establishment/', views.EstablishmentList.as_view(), name='establishment_list'),
    path('establishment/create', views.EstablishmentCreate.as_view(), name='establishment_create'),
    path('establishment/<int:pk>/edit', views.EstablishmentUpdate.as_view(), name='establishment_update'),
    path('establishment/<int:pk>', views.EstablishmentDetail.as_view(), name='establishment_detail'),
    path('company/', views.CompanyList.as_view(), name='company_list'),
    path('company/create', views.CompanyCreate.as_view(), name='company_create'),
    path('company/<int:pk>/edit', views.CompanyUpdate.as_view(), name='company_update'),
    path('company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
]
