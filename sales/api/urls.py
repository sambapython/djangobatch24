from django.urls import path, include
from api.views import CategoryAPIView, TokenView, ProductModelViewSet
urlpatterns = [
    path("category/<int:pk>/", CategoryAPIView.as_view()),
    path("category/", CategoryAPIView.as_view()),# GET
    path("token/", TokenView.as_view()),
    path("product/<int:pk>/", ProductModelViewSet.as_view({
        "get":"retrieve",
        "put":"update",
        "delete":"destroy",
        #"patch":"patch_update",
    })),#get,put,delete,patch
    path("product/", ProductModelViewSet.as_view({
        "post":"create",
        "get":"list"
    }))#get,post
    
]