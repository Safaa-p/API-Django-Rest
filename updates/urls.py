from django.urls import path
from . import views

urlpatterns = [
    path('api', views.ProjectApiView.as_view()),
     path('api/projects/<str:round>/', views.ProjectApiView.as_view()),
]
