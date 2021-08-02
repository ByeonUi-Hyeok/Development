from django.urls import path
from . import views

app_name= 'animal'

urlpatterns = [
    path('', views.index, name='index'),
    path('2/', views.companion, name='companion'),
    path('3/', views.ownerless, name='ownerless'),
    path('2/status/', views.status, name='status'),
    path('2/others/', views.status, name='others'),
]