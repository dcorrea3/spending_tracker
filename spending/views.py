from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import UpdateView

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

def edit_spend(request, spending_id):
	instance = get_object_or_404(Spending, id = spending_id)
	form = AddSpendingForm(request.POST or None,instance=instance)
	if request.method == 'POST':
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
		form = AddSpendingForm(instance=instance)
		#print(form)
	return render(request, 'spending/edit_spend.html',{'form':form})

def delete_spend(request,spending_id):
	instance = get_object_or_404(Spending,id=spending_id)
	instance.delete()
	return HttpResponseRedirect('/spending/')

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

def edit_vendor(request, vendor_id):
	instance = get_object_or_404(Vendors, id=vendor_id)
	form = AddVendorsForm(request.POST or None,instance=instance)
	if request.method == "POST":
		if form.is_valid():
			vendor = form.save(commit=False)
			vendor.vendor_name = request.POST.get('vendor_name')
			vendor.save()
		return HttpResponseRedirect('/vendors/')
	else:
		form = AddVendorsForm(instance=instance)
	return render(request, 'spending/edit_vendor.html',{'form':form})


def delete_vendor(request, vendor_id):
	instance = get_object_or_404(Vendors, id=vendor_id)
	instance.delete()
	return HttpResponseRedirect('/vendors/')




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


def edit_category(request, category_id):
	instance = get_object_or_404(SpendCategory,pk=category_id)
	form = AddCategoryForm(request.POST or None, instance=instance)
		
	if request.method == "POST":
		if form.is_valid():
			cat = form.save(commit=False)
			cat.category_name = request.POST.get('category_name')
			cat.save()
		return HttpResponseRedirect('/categories/')
	else:
		form = AddCategoryForm(instance=instance)
	return render(request, 'spending/edit_category.html', {'form':form})

def delete_category(request, category_id):
	instance = get_object_or_404(SpendCategory,id=category_id)
	instance.delete()
	return HttpResponseRedirect('/categories/')

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