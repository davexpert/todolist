from django.urls import path, include
from .import views

urlpatterns = [
    path('tasks/<int:id>/', views.TaskAPIView.as_view()),

]