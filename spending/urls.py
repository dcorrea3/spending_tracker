from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.view_all_spending, name ='view_all_spending' ),
    path('spending/',views.SpendingView.as_view(), name='spending'),
    path('vendors/', views.VendorsView.as_view(),name = 'vendors'),
    path('add_spend/',views.add_spend)
]