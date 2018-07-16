from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.view_all_spending, name ='view_all_spending' ),
    #path('', views.index, name='index'),
]