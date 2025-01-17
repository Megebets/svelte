from django.urls import path
from . import main_page_data

urlpatterns = [
    path('api/main-page/', main_page_data, name='main_page_data'),
]
