from django.core.management.base import NoArgsCommand
from YerelSecimler.models import Sandik

class Command(NoArgsCommand):

	def handle_noargs(self, **options):

		ils = set([r['il'] for r in Sandik.objects.values('il')])
		for il in ils:
			sandiks = Sandik.objects.filter(il = il).values()
			total = sum([sandik['gecerli'] for sandik in sandiks])
			chp   = sum([sandik['chp'] for sandik in sandiks])
			akp   = sum([sandik['akp'] for sandik in sandiks])
		
			print u'%s:' % il
			print u'AKP: %s / %s' % (akp, total)
			print u'CHP: %s / %s' % (chp, total)