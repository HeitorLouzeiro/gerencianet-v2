from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bank-billet/', views.bank_billet, name='bank-billet'),
    path('carnet/', views.carnet, name='carnet'),
    path('credit-card/', views.credit_card, name='credit-card'),
]
