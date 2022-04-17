from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from moja_strona.models import Product, Order, Opinion
from moja_strona.forms import OrderForm, OpinionForm
#
# class ProductListView(ListView):
#     model = Product

def index(request):
    return render(request,"moja_strona/index.html")

def work(request):
    queryset = Product.objects.all()
    product = {
        "item" : queryset
    }
    return render(request, "moja_strona/all works.html", product)

def opinion(request):
    queryset = Opinion.objects.all()
    opinion = {
        "items": queryset
    }
    return render(request,"moja_strona/opinion.html", opinion)


def product_info(request, id_product):
    info = Product.objects.get(id=id_product)
    result = {
        "name" : info.name,
        "description": info.description,
        "price" : info.price
    }
    return render(request, "moja_strona/info.html", result)

def order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        email = request.POST.get('email')
        # form = OrderForm()
        return redirect(f'/your_order/{email}/')
    result = {
        'form': form
    }
    return render(request, "moja_strona/orders.html", result)

def your_order(request,email):
    queryset = Order.objects.filter(email=email)
    result = {
        'items' : queryset
    }
    return render(request, "moja_strona/your_order.html", result)

def delete_order(request,id):
    obj = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/../')
    context = {
        'items': obj
    }
    return render(request, 'moja_strona/delete_order.html', context)

def create_opinion(request):
    form = OpinionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/opinion/')
    opinion = {
        'form': form
    }
    return render(request, 'moja_strona/create_opinion.html', opinion)


