from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product, Category, Client, Sale, ProductCategory

# Create your views here.
def index(request):
    return render(request, 'index.html')


def outofstock(request):
    form = ProductForm()
    filtered_products = Product.objects.filter(quantity=0, category__is_active=True).all()
    extra_context = {'products': filtered_products, 'form': form}
    if request.method == 'POST':
        product_form = ProductForm(request.POST, files = request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.image = product_form.cleaned_data['image']
            product.user = request.user
            product.save()

            return redirect('index')

    return render(request, 'outofstock.html', context = extra_context)