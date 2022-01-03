from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
  
class CategoryAPIView(APIView):
    def post(self, request):
        return Response("POST")

    def put(self, request):
        return Response("update")

    def delete(self, request):
        return Response("delete")

    def get(self, request):
        return Response("get")

    def patch(self, request):
        return Response("patch")