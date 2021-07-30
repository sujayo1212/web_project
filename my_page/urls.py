from django.urls import path

from . import views

app_name='my_page'
urlpatterns = [
    path('', views.my_page, name='my_page'),
]