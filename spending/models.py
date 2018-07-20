from django.db import models

from django.forms import ModelForm

class SpendCategory(models.Model):
	def __str__(self):
		return self.category_name
	category_name = models.CharField(max_length= 200)

class Vendors(models.Model):
	def __str__(self):
		return self.vendor_name

	vendor_name = models.CharField(max_length=200)
	

class Spending(models.Model):

	spend_date = models.DateTimeField('spend date')
	spend_desc = models.CharField(max_length = 200)
	spend_amt = models.FloatField()
	spend_vendor = models.ForeignKey(Vendors, on_delete= models.SET_NULL, null=True) #automatically create non extant vendors
	spend_cat = models.ForeignKey(SpendCategory,null=True, on_delete = models.SET_NULL) # automatically create non extant categories



class AddVendorsForm(ModelForm):
	class Meta:
		model = Vendors
		fields = ['vendor_name']

class AddCategoryForm(ModelForm):
	class Meta:
		model = SpendCategory
		fields = ['category_name']


class AddSpendingForm(ModelForm):
	class Meta:
		model = Spending
		fields = ['spend_cat','spend_vendor','spend_desc','spend_amt' ]

	 