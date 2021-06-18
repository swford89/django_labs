from django.urls import path
from . import views


app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.detail_pk, name='detail_pk'),
    path('<str:slug>', views.detail_slug, name='detail_slug')
]