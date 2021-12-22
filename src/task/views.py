from django.shortcuts import render
from .models import CreditApplication, Product, Manufacturer, Contract

def index(request, *args, **kwargs):
    # posts = Women.objects.all()
    # cats = Category.objects.all()
    context = {
        'contracts': Contract.objects.all()
    }
    return render(request, 'test/index.html', context=context)


def get_products_by_contract(request, contract_id, *args, **kwargs):
    manufacturers = Manufacturer.objects.filter(
        products__credit_applications__contract=contract_id
    )
    # manufacturers_1 = CreditApplication.objects.filter(contract=contract_id).values_list('product_list__manufacturer', flat=True)

    context = {

        'title': 'Главная страница',
        'manufacturers': manufacturers,

    }
    return render(request, 'test/manufacturers.html', context=context)
