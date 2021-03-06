from django.urls import path
from django.views.generic import TemplateView
from .views import HomepageView, AboutView

urlpatterns = [
    path('', HomepageView.as_view(), name="homepage"),
    path('about/', AboutView.as_view(), name="about")
]
