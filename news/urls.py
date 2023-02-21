from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('hello', views.hello, name='hello'),
]
