from django.urls import path
from .views import SigleView, SiglaAddView

urlpatterns = [
    path('sigle/', SigleView.as_view(), name='sigle'),
    path('sigle/new/', SiglaAddView.as_view(), name='sigle_add')
]
