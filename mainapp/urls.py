from django.urls import path
from . import views


urlpatterns = [
    path('programs/', views.ProgramListView.as_view()),
    path('programs/<int:pk>/', views.ProgramDetailView.as_view()),
]
