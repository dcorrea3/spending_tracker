from django.db import models

class SpendCategory(models.Model):
	category_name = models.CharField(max_length= 200)

class Vendors(models.Model):
	vendor_name = models.CharField(max_length=200)
	

class Spending(models.Model):
	spend_date = models.DateTimeField('spend date')
	spend_desc = models.CharField(max_length = 200)
	spend_amt = models.FloatField()
	spend_vendor = models.ForeignKey(Vendors, on_delete= models.SET_NULL, null=True) #automatically create non extant vendors
	spend_cat = models.ForeignKey(SpendCategory,null=True, on_delete = models.SET_NULL) # automatically create non extant categories

