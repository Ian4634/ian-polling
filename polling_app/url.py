from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('<str:username>/create_poll/', views.create_poll, name='create_poll'),
    path('<str:username>/create_poll/add/', views.add, name='add'),
    path('poll/<str:poll_name>/', views.poll, name='poll'),
    path('commit/', views.commit, name='commit'),
    path('home/inspection/<str:poll_name>/',
         views.inspection, name='inspection'),
    path('thank-filling/', views.thank_filling, name='thank-filling')

]
