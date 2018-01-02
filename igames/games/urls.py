from django.conf.urls import url

import views

urlpatterns = [
	url(r'^info/$', views.info),
	url(r'^search/$', views.search),
	url(r'^rank/$', views.rank),
]
