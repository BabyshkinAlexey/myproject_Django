from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product, Order
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage
from .forms import ProductFormWidget, ProductChoiceForm
import logging
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProductFormWidget, ProductChoiceForm


def index(request):
    return render(request, 'myapp4/index.html')



def client_order(request, client_id):
    client = Client.objects.get(pk=client_id)

    orders_last_7_days = client.order_set.filter(order_date__gte=timezone.now() - timedelta(days=7))
    orders_last_30_days = client.order_set.filter(order_date__gte=timezone.now() - timedelta(days=30))
    orders_last_365_days = client.order_set.filter(order_date__gte=timezone.now() - timedelta(days=365))
    
    all_products = Product.objects.all()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save()
            
            return redirect('client_order', client_id=client.id)
    else:
        product_form = ProductForm()

    context = {
        'client': client,
        'orders_last_7_days': orders_last_7_days,
        'orders_last_30_days': orders_last_30_days,
        'orders_last_365_days': orders_last_365_days,
        'all_products': all_products,
        'product_form': product_form,
    }

    return render(request, 'myapp4/client_order.html', context)

# logger = logging.getLogger(__name__)
# def product_update_form(request, product_id):

#     if request.method == 'POST':
#         form = ProductFormWidget(request.POST, request.FILES)
#         if form.is_valid():
#             logger.info(f'Получили {form.cleaned_data=}.')
#             name = form.cleaned_data.get('name')
#             price = form.cleaned_data.get('price')
#             description = form.cleaned_data.get('description')
#             number = form.cleaned_data.get('number')

#             image = request.FILES['image']
#             fs = FileSystemStorage()
#             fs.save(image.name, image)



#             product = Product.objects.filter(pk=product_id).first()
#             product.name = name
#             product.price = price
#             product.description = description
#             product.quantity = number
#             product.image = image.name

#             product.save()

#     else:
#         form = ProductFormWidget()
#     return render(request, 'myapp4/product_update.html', {'form': form})

# def product_update_id_form(request):
#     if request.method == 'POST':
#         form = ProductChoiceForm(request.POST)
#         if form.is_valid():
#             logger.info(f'Получили {form.cleaned_data=}.')
#             prod_id = form.cleaned_data.get('product_id') # получил id продукта - номер из выпадающего списка
#             response = redirect(f'/homework4/product_update/{prod_id}')
#             return response
#     else:
#         form = ProductChoiceForm()
#     return render(request, 'myapp4/product_update_id.html', {'form': form})