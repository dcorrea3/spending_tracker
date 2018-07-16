from django.contrib import admin

from .models import Vendors,SpendCategory,Spending
# Register your models here.

admin.site.register(Vendors)
admin.site.register(SpendCategory)
admin.site.register(Spending)
	