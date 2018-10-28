from django.urls import path
from .views import SigleView, SiglaNewView, SiglaEditView, SiglaDeleteView
from moduli import views

app_name = 'moduli'
urlpatterns = [
#    path('sigla/new', views.new_sigla, name='new-sigla'),
    path('sigla/new', SiglaNewView.as_view(), name='sigla-new'),
    path('sigle/', SigleView.as_view(), name='sigle-list'),
    path('sigle/<int:pk>', SiglaEditView.as_view(), name='sigla-edit'),
    path('sigle/<int:pk>/delete/', SiglaDeleteView.as_view(), name='sigla-delete'),
]
