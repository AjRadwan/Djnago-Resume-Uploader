from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('<int:pk>', views.Candidate.as_view(), name='candidate')
 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )