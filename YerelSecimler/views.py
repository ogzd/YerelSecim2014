import simplejson as json

from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

from YerelSecimler.models import Sandik

# common methods
def get_iller_raw():
	s = set([r['il'] for r in Sandik.objects.values('il')])
	return list(sorted(s))

def get_ilceler_raw(il):
	s = set(r['ilce'] for r in Sandik.objects.filter(il = il).values('ilce'))
	return list(sorted(s))

def get_okullar_raw(il, ilce):
	s = set(r['okul'] for r in Sandik.objects.filter(il = il, ilce = ilce).values('okul'))
	return list(sorted(s))

def get_ozet_raw(il, ilce, okul):
	sandiks = Sandik.objects.filter(il = il, ilce = ilce, okul = okul).values()
	return { 'toplam_secmen':  sum([sandik['secmen'] for sandik in sandiks]),
		  	'toplam_katilan': sum([sandik['toplam'] for sandik in sandiks]),
		  	'toplam_gecerli': sum([sandik['gecerli'] for sandik in sandiks]),
		  	'toplam_akp':		sum([sandik['akp'] for sandik in sandiks]),
		  	'toplam_chp':		sum([sandik['chp'] for sandik in sandiks]),
		  	'toplam_mhp':     sum([sandik['mhp'] for sandik in sandiks]),
		  	'toplam_bdp':		sum([sandik['bdp'] for sandik in sandiks]) }

def get_sandik_raw(il, ilce, okul):
	return Sandik.objects.filter(il   = il, 
								 ilce = ilce, 
								 okul = okul).order_by('no')

def index(request):
	return render(request, 'main.html', {'iller' : get_iller_raw()})

def get_ilceler(request):
	return HttpResponse(json.dumps(get_ilceler_raw(request.GET['il'])), content_type = 'application/json')

def get_okullar(request):
	return HttpResponse(json.dumps(get_okullar_raw(request.GET['il'], request.GET['ilce'])), content_type = 'application/json') 

def get_sandiklar(request):
	il   = request.GET['il']
	ilce = request.GET['ilce']
	okul = request.GET['okul']
	print il
	print ilce
	print okul

	return HttpResponse(serializers.serialize('json', get_sandik_raw(il, ilce, okul)), content_type = 'application/json')

def get_sandiklar_ozet(request):
	return HttpResponse(json.dumps(get_ozet_raw(request.GET['il'], request.GET['ilce'], request.GET['okul'])), content_type = 'application/json')

# you can only get here from facebook links.
def get_sorgu(request):
	il 	 = request.GET['il']
	ilce = request.GET['ilce']
	okul = request.GET['okul']

	print 'Coming from Facebook.'
	print il
	print ilce
	print okul

	return render(request, 'mirror.html', {
		'iller': 		 get_iller_raw(),
		'ilceler':		 get_ilceler_raw(il),
		'okullar': 		 get_okullar_raw(il, ilce),
		'selected_il': 	 il,
		'selected_ilce': ilce,
		'selected_okul': okul
		})




