from django.core.management.base import NoArgsCommand
from YerelSecimler.models import Sandik

from bs4 import BeautifulSoup

import requests

class Command(NoArgsCommand):
    help = 'Gets Sandik data from sts.chp.org.tr'

    def handle_noargs(self, **options):

        start = 306129 # hardcoded for Izmir
        end   = 316425 # exclusive
        
        # connect to sts.chp.org
        for i in range(start, end):
            try: 
                r = requests.get('http://sts.chp.org.tr/SonucDetay.aspx?sid=%d' % i)
                if r.status_code == 200: 
                    self.get_data(r.text)
            except: 
                pass


        
    def get_data(self, sandik_html):

        soup = BeautifulSoup(sandik_html)

        try: 
            # get il,ilce,okul,sandik no data
            il_ismi, ilce_ismi, sandik_no = [ x.strip() for x in soup.find('span', {'id': 'TabContainer_TabPanel1_lblOzetIlIlce1'}).text.split('/') ]
            okul_ismi                     = soup.find('span', {'id': 'TabContainer_TabPanel1_lblOzetSandikAlani1'}).text.strip()
            secmen_sayisi                 = soup.find('input', {'id': 'TabContainer_TabPanel1_tbOzetKayitliSecmenSayisi1'})['value'].strip()
            toplam_oy                     = soup.find('input', {'id': 'TabContainer_TabPanel1_tbOzetKullanilanToplamOy1'})['value'].strip()
            gecerli_oy                    = soup.find('input', {'id': 'TabContainer_TabPanel1_tbOzetGecerliOySayisi1'})['value'].strip()
        except:
            return

        print 'Getting data from %s, %s, %s\nSandik no: %s' % (il_ismi, ilce_ismi, okul_ismi, sandik_no)  
        
        # find votes of the parties
        try: 
            akp = soup.find('input', {'id': 'TabContainer_TabPanel1_rptPartiler_1_1_tbPartiOy_1_1_6'})['value']
        except:
            akp = 0
        try:    
            chp = soup.find('input', {'id': 'TabContainer_TabPanel1_rptPartiler_1_2_tbPartiOy_1_2_6'})['value']
        except:
            chp = 0
        try:
            mhp = soup.find('input', {'id': 'TabContainer_TabPanel1_rptPartiler_1_2_tbPartiOy_1_2_8'})['value']
        except:
            mhp = 0
        try:
            bdp = soup.find('input', {'id': 'TabContainer_TabPanel1_rptPartiler_1_2_tbPartiOy_1_2_5'})['value']
        except:
            bdp = 0

        # save to database
        sandik = Sandik(no      = sandik_no, 
                        il      = il_ismi,
                        ilce    = ilce_ismi,
                        okul    = okul_ismi,
                        secmen  = secmen_sayisi,
                        toplam  = toplam_oy,
                        gecerli = gecerli_oy,
                        akp     = akp, 
                        chp     = chp, 
                        mhp     = mhp, 
                        bdp     = bdp).save()