from rest_framework.decorators import api_view
from rest_framework.response import Response
from productcrud.models import Product
from .serializers import ProductSerializer

# GET All Products
@api_view(["GET"])
def get_products(request):

    products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)

# GET Product by ID
@api_view(["GET"])
def get_product(request, id):

    product = Product.objects.get(id=id)

    serializer = ProductSerializer(product)

    return Response(serializer.data)

# Add Product
@api_view(["POST"])
def add_product(request):

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Update Product
@api_view(["PUT"])
def update_product(request, id):

    product = Product.objects.get(id=id)

    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Delete Product
@api_view(["DELETE"])
def delete_product(request, id):

    product = Product.objects.get(id=id)

    product.delete()

    return Response({
        "message": "Product deleted"
    })