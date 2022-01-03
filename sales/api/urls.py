from django.urls import path, include
from api.views import CategoryAPIView
urlpatterns = [
    path("category/", CategoryAPIView.as_view())# GET
    
]