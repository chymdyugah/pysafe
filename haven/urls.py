from django.conf.urls import url
from haven import views

app_name = "haven"

urlpatterns = [
	url(r'^login/$', views.Login.as_view(), name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^register/$', views.Register.as_view(), name='register'),
	url(r'^$', views.Index.as_view(), name='index'),
	url(r'^ajx/$', views.Ajx.as_view(), name='ajx'),
]
