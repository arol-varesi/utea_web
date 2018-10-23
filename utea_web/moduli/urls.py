from django.urls import path
from .views import SigleView, Sigle2View, SigleViewEdit, SiglaNewView, SiglaEditView, SiglaDeleteView, ExampleEditView

app_name = 'moduli'
urlpatterns = [
    path('sigle/', SigleView.as_view(), name='sigle'),
    path('sigle/new/', SiglaNewView.as_view(), name='sigla-new'),
    path('sigle/<int:pk>', SiglaEditView.as_view(), name='sigla-edit'),
    path('sigle/<int:pk>/delete/', SiglaDeleteView.as_view(), name='sigla-delete'),
    path('sigle2/', Sigle2View.as_view(), name='sigle-test2'),
    path('sigle_editable/', SigleViewEdit.as_view(), name='sigle-list-edit'),
    path('example/<int:pk>', ExampleEditView.as_view(), name='example-edit'),
]
