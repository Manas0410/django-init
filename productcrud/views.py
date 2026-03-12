from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
import json

# Create your views here.

# get all prods
def get_products(request):
    products = Product.objects.all()

    data = []

    for p in products:
        data.append({
            "id": p.id,
            "name": p.name,
            "price": float(p.price),
            "description": p.description,
            "stock": p.stock
        })

    return JsonResponse(data, safe=False)


# get prods by id
def get_product(request, id):

    product = Product.objects.get(id=id)

    data = {
        "id": product.id,
        "name": product.name,
        "price": float(product.price),
        "description": product.description,
        "stock": product.stock
    }

    return JsonResponse(data)

# API 3 — Add Product
def add_product(request):

    body = json.loads(request.body)

    product = Product.objects.create(
        name=body.get("name"),
        price=body.get("price"),
        description=body.get("description"),
        stock=body.get("stock")
    )

    return JsonResponse({
        "message": "Product created",
        "id": product.id
    })


# API 4 — Update Product
def update_product(request, id):

    body = json.loads(request.body)

    product = Product.objects.get(id=id)

    product.name = body.get("name")
    product.price = body.get("price")
    product.description = body.get("description")
    product.stock = body.get("stock")

    product.save()

    return JsonResponse({
        "message": "Product updated"
    })

# API 5 — Delete Product
def delete_product(request, id):

    product = Product.objects.get(id=id)

    product.delete()

    return JsonResponse({
        "message": "Product deleted"
    })