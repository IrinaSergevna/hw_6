from django.shortcuts import render
from .models import Product


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    print("Последние товары:", latest_products)
    return render(request, "home.html", {'latest_products': latest_products})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"{name} ({email}): {message}")
    return render(request, "contact.html")




