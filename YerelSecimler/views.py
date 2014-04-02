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

def get_sandiklar_ozet(request):
	il 	 = request.GET['il']
	ilce = request.GET['ilce']
	okul = request.GET['okul']
	
	sandiks = Sandik.objects.filter(il = il).filter(ilce = ilce).filter(okul = okul).values()

	r = { 
		  'toplam_secmen':  sum([sandik['secmen'] for sandik in sandiks]),
		  'toplam_katilan': sum([sandik['toplam'] for sandik in sandiks]),
		  'toplam_gecerli': sum([sandik['gecerli'] for sandik in sandiks]),
		  'toplam_akp':		sum([sandik['akp'] for sandik in sandiks]),
		  'toplam_chp':		sum([sandik['chp'] for sandik in sandiks]),
		  'toplam_mhp':     sum([sandik['mhp'] for sandik in sandiks]),
		  'toplam_bdp':		sum([sandik['bdp'] for sandik in sandiks]) 
		}

	return HttpResponse(json.dumps(r), content_type = 'application/json')





