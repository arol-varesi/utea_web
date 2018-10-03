from django.urls import path
from .views import SigleView

urlpatterns = [
    path('sigle/', SigleView.as_view(), name="sigle"),
]
