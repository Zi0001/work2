from django.urls import include, path
from django.contrib.auth import views
from . import views

app_name = 'journal'

urlpatterns = [
    path('', views.test, name='test'),
    path('auth/', include('django.contrib.auth.urls')),
    path('edit/<int:pk>/', views.Edit.as_view(), name='edit'),
    path('create/', views.JournalCreate.as_view(), name='test2'),
]

