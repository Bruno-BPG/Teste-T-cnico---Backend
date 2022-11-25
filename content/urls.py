from django.urls import path

from .views import fazerUpload

urlpatterns = [
    path('', fazerUpload.as_view()),
]
