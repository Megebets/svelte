from django.urls import path
from .views import SaveProfileView

urlpatterns = [
    path('save-profile/', SaveProfileView.as_view(), name='save_profile'),
]
