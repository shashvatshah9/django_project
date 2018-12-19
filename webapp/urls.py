from django.conf.urls import patterns, include, url

urlpatterns = patterns('', 
	url(r'^hello/', 'webapp.views.welcome', name='hello'),
	url(r'^about/', 'webapp.views.about', name='about'),)
