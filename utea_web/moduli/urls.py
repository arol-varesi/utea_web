from django.urls import path
from .views import SigleView, Sigle2View, SigleViewEdit, SiglaNewView, SiglaEditView, SiglaDeleteView, ExampleEditView
from moduli import views

app_name = 'moduli'
urlpatterns = [
    path('sigla/new', views.new_sigla, name='new-sigla'),
    path('sigle/', SigleViewEdit.as_view(), name='sigle-list-edit'),
    # path('sigle/', SigleView.as_view(), name='sigle'),
    # path('sigle/new/', SiglaNewView.as_view(), name='sigla-new'),
    # path('sigle/<int:pk>', SiglaEditView.as_view(), name='sigla-edit'),
    path('sigle/<int:pk>/delete/', SiglaDeleteView.as_view(), name='sigla-delete'),
    # path('sigle2/', Sigle2View.as_view(), name='sigle-test2'),
]
