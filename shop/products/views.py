import logging

from django.shortcuts import render

from products.models import Product

logger = logging.getLogger(__name__)


def index(request):
    request.GET.get("title")
    purchases__count = request.GET.get("purchases__count")

    products = Product.objects.all()

    title = request.GET.get("title")
    if title is not None:
        products = products.filter(title__icontains=title)

    purchases__count = request.GET.get("purchases__count")
    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    response = render(request, "index.html", {"products": products})
    return response

