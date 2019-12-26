
from django.conf.urls import url,include
from django.contrib import admin
from account import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',user_views.home,name='23'),
    url(r'^account/',include('account.urls')),
    url(r'^register/', user_views.register, name='register'),
    url(r'^login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='account/login.html'),name='logout'),
]
