from django.urls import path
from . import views


app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.detail_slug, name='detail_slug')
]