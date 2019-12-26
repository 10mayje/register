from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^song/',views.new,name='new'),

    url(r'^create/', views.create, name='create'),

]