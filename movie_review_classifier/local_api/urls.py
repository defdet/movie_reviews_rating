# local_api/urls.py

from django.urls import path
from .views import predict_rating

urlpatterns = [
    path('predict_rating/', predict_rating, name='predict_rating'),
]
