from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




from .models import Category, File, Product
from .serializers import CategorySerializer, FileSerializer, ProductSerializer


class CategoryListView(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True, context={'request':request})
        return Response(serializer.data)


class CategoryDetailView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, context={'request':request})
        return Response(serializer.data)



class ProductListView(APIView):

    def get(self, request):
        products  = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request':request})
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context={'request':request})
        return Response(serializer.data)
    

class FileListView(APIView):

    def get(self, request, product_id):
        file = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(file, many=True, context={'request':request})
        return Response(serializer.data)


class FileDetialView(APIView):

       def get(self, request, product_id ,pk):
        try:
            file =File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(file, context={'request':request})
        return Response(serializer.data)
    



