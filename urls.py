from django.urls import path
from pullgerMultisessionManager_FRONT import views

urlpatterns = [
    path('about/', views.about),
]