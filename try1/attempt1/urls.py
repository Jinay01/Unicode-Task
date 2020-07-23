from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('form', views.binaryform, name='form'),
    path('result', views.binary, name='result'),
    path('apiform', views.apiform, name='apiform'),
    path('api', views.api, name='api'),
]
