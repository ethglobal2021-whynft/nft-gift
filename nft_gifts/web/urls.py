from django.urls import path

from .views import checking_page, index, receiving

urlpatterns = [
    path('', index, name='index'),
    path('receiving', receiving, name='receiving'),
    path('checking_page', checking_page, name='checking_page')
]
