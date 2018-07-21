from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
app_name='eshop'

urlpatterns=[
    #/eshop
    path(r"", views.IndexView.as_view(), name='index'),
      #/eshop/profile/edit_profile
    path(r"profile/edit_profile",views.edit_profile, name='edit_profile'),
    #/eshop/profile/change_password
    path(r"profile/change_password",views.change_password, name='change_password'),
    #/eshop/profile
    path(r"profile",views.profile, name='profile'),
       #/eshop/login and logout
    path(r"login",auth_views.login, {'template_name':'eshop/login.html'},name='login'),
    path(r"logout",auth_views.logout, {'template_name':'eshop/logout.html'},name='logout'),
]
