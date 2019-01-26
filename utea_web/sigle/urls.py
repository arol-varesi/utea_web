from django.urls import path
from .views import SigleView, SiglaNewView, SiglaEditView, SiglaDeleteView
# from sigle import views

app_name = 'sigle'
urlpatterns = [
#    path('sigla/new', views.new_sigla, name='new-sigla'),
    path('new', SiglaNewView.as_view(), name='sigla-new'),
    path('', SigleView.as_view(), name='sigle-list'),
    path('<int:pk>', SiglaEditView.as_view(), name='sigla-edit'),
    path('<int:pk>/delete/', SiglaDeleteView.as_view(), name='sigla-delete'),
]
