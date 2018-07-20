from django import forms

from spending.models import Vendors,SpendCategory,Spending


	 
	#spend_vendor = forms.ForeignKey(Vendors, on_delete= models.SET_NULL, null=True) #automatically create non extant vendors
	#spend_cat = forms.ForeignKey(SpendCategory,null=True, on_delete = models.SET_NULL) # automatically create non extant categories


class CategoryForm(forms.Form):
	category_name = forms.CharField(max_length=200)
	

class VendorsForm(forms.Form):
	vendor_name = forms.CharField(max_length=200)
	


class AddSpendingForm(forms.Form):
	#spend_date = forms.DateField()
	spend_desc = forms.CharField(max_length=200)
	spend_amt = forms.FloatField()
	spend_vendor = forms.ModelMultipleChoiceField(queryset=Vendors.objects.all())
	spend_cat = forms.ModelMultipleChoiceField(queryset=SpendCategory.objects.all())
