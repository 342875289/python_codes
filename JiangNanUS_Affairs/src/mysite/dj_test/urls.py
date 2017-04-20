from django.conf.urls import url

from . import views
from .views import NameFormView

app_name = 'dj_test'
urlpatterns = [
    url(r'^$', views.test_index),
    url(r'^your/$', views.get_name,name='forms'),
    url(r'^name/$', NameFormView.as_view(),name='name'),
    url(r'^person/$', views.get_person,name='formss'),
]
