# movie_review_classifier/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review_classifier/', include('review_classifier.urls')),
    path('local_api/', include('local_api.urls')),
]
