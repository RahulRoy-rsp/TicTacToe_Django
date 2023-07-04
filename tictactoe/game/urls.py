from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('home.html', views.home, name='home'),
    path('vsComp.html', views.vsComp, name='vsComp'),
    path('oneVsone.html', views.oneVsone, name='oneVsone'),
]
