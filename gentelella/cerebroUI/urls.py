from django.conf.urls import url
from cerebroUI import views

urlpatterns = [
	# The home page
    url(r'^$', views.index, name='index'),

    url(r'^.*\.html', views.gentella_html, name='gentella')
 ]
