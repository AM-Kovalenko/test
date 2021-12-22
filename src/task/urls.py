from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contracts/<int:contract_id>/products', get_products_by_contract, name='man')

]