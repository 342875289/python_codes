from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book_list/$', views.book_list, name='book_list'),
    url(r'^book_list/(?P<book_id>[0-9]+)$', views.book_detail, name='book_detail'),
    #url(r'^login/(?P<username>[\w]+)/(?P<password>[\w]+)/$', views.userlogin, name='userlogin'),
    url(r'^login$', views.userlogin, name='userlogin'),
    url(r'^tt/$', views.tt, name='tt'),
    url(r'^logout/$', views.userlogout, name='userlogout'),
    url(r'^download$', views.download, name='download'),
    url(r'^purchase$', views.purchase, name='purchase'),
]