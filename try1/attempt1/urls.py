from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('form', views.binaryform, name='form'),
    path('result/<int:numb1>/<int:numb2>', views.binary, name='result'),
    path('apiform', views.apiform, name='apiform'),
    path('api', views.api, name='api'),
    path('userfinder', views.userfinder, name='userfinder'),
    path('repofinder', views.repofinder, name='repofinder'),
    path('followersfinder', views.followersfinder, name='followersfinder'),
    path('followingfinder', views.followingfinder, name='followingfinder'),
    path('top', views.top, name='top'),

]
