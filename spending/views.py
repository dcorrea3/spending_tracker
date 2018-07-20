from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from .models import Spending, Vendors, SpendCategory,AddSpendingForm
#from .forms import AddSpendingForm

from datetime import datetime

def add_spend(request):
	if request.method == 'POST':

		form = AddSpendingForm(request.POST)
		if form.is_valid():
			spend = form.save(commit=False)
			print(request.spend_vendor)
			spend.spend_vendor = Vendors.objects.get(pk= request.spend_vendor)
			spend.spend_date = datetime.datetime.now()
			spend.spend_desc = request.spend_desc
			spend.spend_amt = request.spend_amt
			spend.spend_cat = SpendCategory.objects.get(pk=request.spend_cat)
			spend.save()
		return HttpResponseRedirect('/spending/')

	else:
		form = AddSpendingForm()
	return render(request, 'spending/add_spend.html',{'form':form})


def view_all_spending(request):

	return HttpResponse('This is the landing page')


class SpendingView(generic.ListView):
		template_name = 'spending/index.html'
		context_object_name = 'all_spending_list'

		def get_queryset(self):
			return Spending.objects.order_by('spend_date')
 
class VendorsView(generic.ListView):
		template_name = 'spending/vendors.html'
		context_object_name = 'all_vendors_list'

		def get_queryset(self):
			return Vendors.objects.order_by('vendor_name')