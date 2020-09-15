from django.urls import path
from .views import HomeView
app_name = 'Store'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]