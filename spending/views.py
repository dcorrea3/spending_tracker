from django.http import HttpResponse
from django.shortcuts import render

def view_all_spending(request):
	return HttpResponse("this is the view spending page")




