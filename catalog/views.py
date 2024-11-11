from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Contact
from django.core.paginator import Paginator
from .forms import ProductForm


def home(request):
    products = Product.objects.all()
    latest_products = Product.objects.order_by('-created_at')[:5]

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': products,
        'latest_products': latest_products,
        'page_obj': page_obj,
    }
    return render(request, 'home.html', context)

def contact(request):
    contacts = Contact.objects.all()
    print("Контактные данные:", contacts)
    return render(request, 'contact.html', {'contacts': contacts})

def index(request):
    return render(request, 'base.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})