from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book_list$', views.book_list, name='book_list'),
    url(r'^login$', views.userlogin, name='userlogin'),
    url(r'^logout$', views.userlogout, name='userlogout'),
    url(r'^download$', views.download, name='download'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^key$', views.getkey, name='getkey'),
    url(r'^purchase$', views.purchase, name='purchase'),
    url(r'^getcode$', views.getcode, name='getcode'),
    url(r'^usecode$', views.usecode, name='usecode'),
]