from django.shortcuts import render
from products.models import (
    Category,
    ProductGroup,
    DesignCategory,
    ProductDesignGroup,
    Size,
    Color,
    Product,
    Design,
    Images,
)

# Create your views here.


def index(request):
    all_products = Product.objects.all().order_by('price', 'name')
    products = Product.objects.all().order_by('sec_code').distinct('sec_code')
    product_sizes = Size.objects.all().order_by('relative_size')
    product_images = []
    for product in products:
        images = Images.objects.filter(product=product.id)[0]
        product_images.append(images)

    context = {
        'all_products': all_products,
        'products': products,
        'product_images': product_images,
        'product_sizes': product_sizes,
    } 

    return render(request, 'home/index.html', context)
