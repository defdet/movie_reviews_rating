# review_classifier/urls.py

from django.urls import path
from . import views
from .views import predict_rating

urlpatterns = [
    path('', views.predict_rating, name='predict_rating'),
    path('predict_rating/', predict_rating, name='predict_rating'),
]
