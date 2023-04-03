import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.forms import ProductAdd
from products.models import Product

logger = logging.getLogger(__name__)


def index(request):
    products = Product.objects.all()

    title = request.GET.get("title")
    if title is not None:
        products = products.filter(title__icontains=title)

    purchases__count = request.GET.get("purchases__count")
    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    return render(request, "index.html", {"products": products})





def ProductAdd(request):
    if request.method == "POST":
        form = ProductAddForm(request.POST)
        if form.is_valid():
            Product.objects.create(title=form.cleaned_data["title"],
                                   price=form.cleaned_data["price"],
                                   color=form.cleaned_data["color"],
                                   description=form.cleaned_data["description"])
            return redirect("index")
    else:
        form = ProductAddForm()
    return render(request,'product_add.html', {"form": form})