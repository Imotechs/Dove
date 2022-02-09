from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'webs-home'),
    path('about/', views.about, name = 'webs-about'),

]