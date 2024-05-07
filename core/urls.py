from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

from .views import myaccount ,edit_myaccount
app_name ='core'

urlpatterns =[
    path('', views.index,name = 'index'),
    path('contact/',views.contact,name='contact'),
    path('signup/', views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name ='core/login.html',authentication_form=LoginForm), name='login'),
    #path('login/',views.login_view, name='login'),
    path('myaccount/', myaccount , name='myaccount'),
    path('edit_myaccount/', edit_myaccount , name='edit_myaccount'),
    path('logout/', views.logout_view,name='logout'),
    path('otp/', views.otp_view,name='otp'),
]