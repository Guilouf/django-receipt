from django.urls import path

from receipt import views

urlpatterns = [
    path('receipt/', views.ReceiptList.as_view(), name='receipt_list'),
    path('receipt/create', views.ReceiptCreate.as_view(), name='receipt_create'),
    path('receipt/<int:pk>/edit', views.ReceiptUpdate.as_view(), name='receipt_update'),
]
