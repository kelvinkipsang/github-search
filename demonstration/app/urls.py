
from django.conf.urls import url

from app import views

urlpatterns = [
  url(r'^$', views.profile, name='profile'),
  url(r'^test/$', views.test, name='test'),
  url(r'^profile/$', views.profile, name='profile'),
]