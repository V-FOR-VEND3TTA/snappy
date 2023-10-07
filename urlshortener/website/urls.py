from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    # the url we go to when the "shorten" button has been clicked
    path('create', views.index, name='create')
]
