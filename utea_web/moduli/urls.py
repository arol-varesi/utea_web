from django.urls import path
from .views import SigleView, SiglaNewView, SiglaEditView, SiglaDeleteView

urlpatterns = [
    path('sigle/', SigleView.as_view(), name='sigle'),
    path('sigle/new/', SiglaNewView.as_view(), name='sigla-new'),
    path('sigle/<int:pk>', SiglaEditView.as_view(), name='sigla-edit'),
    path('sigle/<int:pk>/delete/', SiglaDeleteView.as_view(), name='sigla-delete'),
]
