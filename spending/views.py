from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from .models import Spending, Vendors, SpendCategory,AddSpendingForm, AddVendorsForm
from .models import AddCategoryForm
#from .forms import AddSpendingForm

from datetime import datetime

def add_spend(request):
	if request.method == 'POST':

		form = AddSpendingForm(request.POST)
		if form.is_valid():
			spend = form.save(commit=False)

			spend.spend_vendor = Vendors.objects.get(pk= request.POST.get('spend_vendor'))
			spend.spend_date = datetime.now()
			spend.spend_desc = request.POST.get('spend_desc')
			spend.spend_amt = request.POST.get('spend_amt')
			spend.spend_cat = SpendCategory.objects.get(pk=request.POST.get('spend_cat'))
			spend.save()
		return HttpResponseRedirect('/spending/')

	else:
		form = AddSpendingForm()
	return render(request, 'spending/add_spend.html',{'form':form})


def add_vendor(request):
	if request.method == "POST":
		form = AddVendorsForm(request.POST)
		if form.is_valid():
			vendor = form.save(commit=False)
			vendor.vendor_name = request.POST.get('vendor_name')
			vendor.save()
		return HttpResponseRedirect('/vendors/')
	else:
		form = AddVendorsForm()
	return render(request, 'spending/add_vendor.html',{'form':form})

def add_category(request):
	if request.method == "POST":
		form = AddCategoryForm(request.POST)
		if form.is_valid():
			cat = form.save(commit=False)
			cat.category_name = request.POST.get('category_name')
			cat.save()
		return HttpResponseRedirect('/categories/')
	else:
		form = AddCategoryForm()
	return render(request, 'spending/add_category.html', {'form':form})

def view_all_spending(request):

	return HttpResponse('This is the landing page')


class SpendingView(generic.ListView):
		template_name = 'spending/index.html'
		context_object_name = 'all_spending_list'

		def get_queryset(self):
			return Spending.objects.order_by('spend_date')


class CategoriesView(generic.ListView):
		template_name = 'spending/spend_categories.html'
		context_object_name = 'all_categories_list'

		def get_queryset(self):
			return SpendCategory.objects.order_by('category_name')
 
class VendorsView(generic.ListView):
		template_name = 'spending/vendors.html'
		context_object_name = 'all_vendors_list'

		def get_queryset(self):
			return Vendors.objects.order_by('vendor_name')