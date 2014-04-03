from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'YerelSecimler.views.index'),
	url(r'^ilceler/', 'YerelSecimler.views.get_ilceler'),
	url(r'^okullar/', 'YerelSecimler.views.get_okullar'),
	url(r'^sandiklar/', 'YerelSecimler.views.get_sandiklar'),
	url(r'^sandiklar_ozet/', 'YerelSecimler.views.get_sandiklar_ozet'),
	url(r'^sorgu/', 'YerelSecimler.views.get_sorgu')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
