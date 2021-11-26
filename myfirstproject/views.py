from django.http import HttpResponse
from django.shortcuts import render


def about(request):
	return HttpResponse('Visis ebaut pech')


def home(req):
	return render(req, 'home.html', {'greatting': 'Hello!'})