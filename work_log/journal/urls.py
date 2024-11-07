from django.urls import include, path
from . import views

app_name = 'journal'

urlpatterns = [
    path('', views.test, name='test'),
    path('create/', views.JournalCreate.as_view(), name='test2'),
    path('auth/', include('django.contrib.auth.urls')),
]