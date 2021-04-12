from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
     path('curriculo/', views.curriculo, name='curriculo'),
]