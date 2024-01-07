from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include("users.urls")),
    path('model/<str:api_key>/', include("ai_models.urls")),
]
