# Wire up our API here
from django.urls import path
from rest_api import views

urlpatterns = [
    path('weather/', views.WeatherListView.as_view()),
    path('weather/<int:id>/', views.WeatherView.as_view())
]
