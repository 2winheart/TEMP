from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Board_main, name='Board_list'),
	url(r'^Board/(?P<pk>[0-9]+)/$', views.Board_detail, name='Board_detail'),
	url(r'^Board/create/$', views.Board_create, name='Board_create'),
	url(r'^Board/(?P<pk>[0-9]+)/edit/$', views.Board_edit, name='Board_edit'),
	url(r'^Board/(?P<pk>[0-9]+)/delete/$', views.Board_delete, name="Board_delete"),
]
