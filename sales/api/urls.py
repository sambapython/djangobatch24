from django.urls import path, include
from api.views import CategoryAPIView
urlpatterns = [
    path("category/<int:pk>/", CategoryAPIView.as_view()),
    path("category/", CategoryAPIView.as_view()),# GET
    
]