from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.view_all_spending, name ='view_all_spending' ),
    path('spending/',views.SpendingView.as_view(), name='spending'),
    path('add_spend/',views.add_spend),
	path('edit_spend/<int:spending_id>/', views.edit_spend),
	path('delete_spend/<int:spending_id>', views.delete_spend),
    path('vendors/', views.VendorsView.as_view(),name = 'vendors'),
    path('add_vendor/',views.add_vendor),
    path('edit_vendor/<int:vendor_id>/', views.edit_vendor),
    path('delete_vendor/<int:vendor_id>/', views.delete_vendor),
    path('add_category/',views.add_category),
    path('edit_category/<int:category_id>/', views.edit_category),
    path('delete_category/<int:category_id>',views.delete_category),    
    path('categories/',views.CategoriesView.as_view(), name='categories'),

]