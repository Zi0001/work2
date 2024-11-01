from django.urls import path
from . import views

app_name = 'journal'

urlpatterns = [
    path('', views.test, name='test'),
    path('create/', views.JournalCreate.as_view(), name='test2')
]