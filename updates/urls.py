from django.urls import path
from . import views

urlpatterns = [
     path('api/projects/<str:round>/', views.ProjectByRoundApiView.as_view()),
   path('api/code/<str:project_code>/', views.ProjectByCodeApiView.as_view()),]
