import simplejson as json

from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

from YerelSecimler.models import Sandik

def index(request):
	s = set([r['il'] for r in Sandik.objects.values('il')])
	return render(request, 'main.html', {'iller' : s})

def get_ilceler(request):
	il = request.GET['il']
	s = set(r['ilce'] for r in Sandik.objects.filter(il = il).values('ilce'))
	return HttpResponse(json.dumps(list(sorted(s))), content_type = 'application/json')

def get_okullar(request):
	il   = request.GET['il']
	ilce = request.GET['ilce']
	s = set(r['okul'] for r in Sandik.objects.filter(il = il).filter(ilce = ilce).values('okul'))
	return HttpResponse(json.dumps(list(sorted(s))), content_type = 'application/json') 

def get_sandiklar(request):
	il   = request.GET['il']
	ilce = request.GET['ilce']
	okul = request.GET['okul']
	print il
	print ilce
	print okul

	sandiks = Sandik.objects.filter(il = il).filter(ilce = ilce).filter(okul = okul).order_by('no')

	return HttpResponse(serializers.serialize('json', sandiks), content_type = 'application/json')



