from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField

class Sandik(models.Model):
	il      = models.TextField()
	ilce    = models.TextField()
	okul    = models.TextField()
	no 		= models.IntegerField()
	akp 	= models.IntegerField(default = 0)
	chp 	= models.IntegerField(default = 0)
	mhp 	= models.IntegerField(default = 0)
	bdp 	= models.IntegerField(default = 0)
	gecerli = models.IntegerField(default = 0)
	toplam 	= models.IntegerField(default = 0)
	secmen  = models.IntegerField(default = 0)
