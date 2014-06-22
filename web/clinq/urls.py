from django.conf.urls import patterns, url

from clinq import views

urlpatterns = patterns('',
	url(r'^$', views.Home, name='Home'),
    url(r'^list_albums$', views.list_albums, name='list_albums'),
    url(r'^list_artists$', views.list_artists, name='list_albums')
)


