# review_classifier/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_rating, name='predict_rating'),
]
