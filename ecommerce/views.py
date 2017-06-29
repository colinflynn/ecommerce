from django.http import HttpResponse
from django.shortcuts import render

from retail_stores.models import RetailStore

def index(request):
	retail_store_list = RetailStore.objects.all()
	context = {'retail_store_list':retail_store_list}
	return render(request, 'home/home.html', context)