from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('ai/chat/', views.ai_chat, name='ai_chat'),
]
