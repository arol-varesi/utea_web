# moduli/urls.py
from django.urls import path
from .views import SiglaList, SiglaAddView, SiglaDetail

urlpatterns = [
    path('sigle/', SiglaList.as_view(), name='sigla_list'),
    path('sigla/<int:pk>/', SiglaDetail.as_view(), name="sigla_detail"),
    path('sigle/new/', SiglaAddView.as_view(), name='sigle_add')
]
