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
    path('nodjango', views.no_django_form, name='nodjango'),
    path('no_django_result/<int:num1>/<int:num2>',
         views.no_django_result, name='no_django_result'),
]
