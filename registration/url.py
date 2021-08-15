from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name = 'register'),
    path('verify/', views.verify, name = 'verify' ),
    path('login/', views.login, name='login'),
    path('inspect_login/', views.inspect_login,name = 'inspect_login'),
    path('home/<str:username>/',views.home, name = 'home'),
    path('logout/',views.logout, name = 'logout'),
    path('home/<str:username>/polling/',views.polling, name = 'polling')
]