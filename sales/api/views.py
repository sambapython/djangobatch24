from django.core.checks import messages
from django.shortcuts import render
from product.models import Category, Product

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import CategorySerializer, CategoryGetSerializer, ProductSerializer
from rest_framework import status 
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import viewsets

class ProductModelViewSet(viewsets.ModelViewSet):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
        

class TokenView(APIView):
    authentication_classes=[]
    permission_classes=[]
    def post(self, request):
        user = authenticate(**request.data)
        if user:
            existed = Token.objects.filter(user=user).first()
            if existed:
                existed.delete()
            t=Token(user=user)
            t.save()
            return Response(t.key)
        else:
            return Response("Invalid login",status=status.HTTP_401_UNAUTHORIZED)

class CategoryAPIView(APIView):
    def post(self, request):
        # cat_inst = Category(**request.data)
        # cat_inst.save()
        # data = cat_inst.data()
        resp = {}
        ser = CategorySerializer(data=request.data)
        message = ""
        if ser.is_valid():
            ser.save()
            data = ser.data
            status_code = status.HTTP_201_CREATED
            message = "Category created successfully"
        else:
            data = ser.errors
            status_code = status.HTTP_400_BAD_REQUEST
            message = "Error"
        resp.update({"data":data,"message":message})
        return Response(resp, status=status_code)

    def put(self, request, pk):
        resp = {}
        data={}
        try:
            cat_inst=Category.objects.get(pk=pk)
            ser = CategorySerializer(instance=cat_inst, data=request.data)
            if ser.is_valid():
                ser.save()
                message = "Updated successfully"
                status_code= status.HTTP_200_OK
                data = ser.data
            else:
                data=ser.errors
                message = "Error"
                status_code= status.HTTP_400_BAD_REQUEST

        except Exception as err:
            message = "%s"%err
            status_code= status.HTTP_400_BAD_REQUEST
            data = {}
        resp.update({"message": message, "data":data})
        return Response(resp, status=status_code)

    def delete(self, request, pk):
        resp = {}
        data={}
        try:
            cat_inst=Category.objects.get(pk=pk)
            cat_inst.hide=True
            cat_inst.save()
            message="deleted successfully"
            status_code= status.HTTP_200_OK
        except Exception as err:
            message = "%s"%err
            status_code= status.HTTP_400_BAD_REQUEST
            data = {}
        resp.update({"message": message, "data":data})
        return Response(resp, status=status_code)

    def get(self, request, pk=None):
        if pk:
            #data = Category.objects.get(pk=pk, hide=False)
            data = Category.objects.filter(pk=pk, hide=False)
        else:
            data = Category.objects.filter(hide=False)
            #data = [{"name":i.name, "discount":i.discount} for i in data]
        ser = CategoryGetSerializer(data, many=True)
        return Response(ser.data)


    def patch(self, request):
        return Response("patch")