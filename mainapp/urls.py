from django.urls import path
from . import views


urlpatterns = [
    path('programs/', views.ProgramListView.as_view()),
    path('programs/<int:pk>/', views.ProgramDetailView.as_view()),
    path('news/', views.NewsListView.as_view()),
    path('news/<int:pk>/', views.NewsDetailView.as_view()),
    path('instructions/', views.InstructionListView.as_view()),
    path('instructions/<int:pk>/', views.InstructionDetailView.as_view()),
]
