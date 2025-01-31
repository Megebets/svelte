from django.urls import path
from . import views
urlpatterns = [
    path('api/main-page/', views.main_page_data, name='main_page_data'),
]
