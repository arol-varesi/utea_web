from django.urls import path
from .views import SigleView, SiglaNewView, SiglaEditView, SiglaDeleteView, TipoCreatePopup #, SigleViewTest, SiglaNewViewTest, sigla_new_test, sigla_edit_test
# from sigle import views

app_name = 'sigle'
urlpatterns = [
#    path('sigla/new', views.new_sigla, name='new-sigla'),
#    path('test', SigleViewTest.as_view(), name='sigle-test'),
#    path('testnew', sigla_new_test, name='sigla-new-test'),
#    path('test/<int:pk>', sigla_edit_test, name='sigla-edit-test'),

    path('', SigleView.as_view(), name='sigle-list'),
    path('new', SiglaNewView.as_view(), name='sigla-new'),
    path('<int:pk>', SiglaEditView.as_view(), name='sigla-edit'),
    path('<int:pk>/delete/', SiglaDeleteView.as_view(), name='sigla-delete'),

    path('tipo/new', TipoCreatePopup, name='tipo-new-popup'),
]
