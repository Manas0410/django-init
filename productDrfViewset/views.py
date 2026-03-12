from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from productcrud.models import Product
from productDrfManual.serializers import ProductSerializer
from rest_framework.response import Response

class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer


    # max price api
    @action(detail=False, methods=["get"])
    def max_price(self, request):

        product = Product.objects.order_by("-price").first()

        serializer = ProductSerializer(product)

        return Response(serializer.data)
    
    

# | API                   | Method         |
# | --------------------- | -------------- |
# | GET /products         | get all        |
# | GET /products/{id}    | get single     |
# | POST /products        | create         |
# | PUT /products/{id}    | update         |
# | PATCH /products/{id}  | partial update |
# | DELETE /products/{id} | delete         |
