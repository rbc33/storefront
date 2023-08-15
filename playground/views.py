from django.shortcuts import render
from django.db.models import Q, F
from store.models import *

    ## django ORM examples
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)
    # queryset = Product.objects.filter(description__isnull=True)
    # queryset = Product.objects.filter(last_update__date=2021)
    # queryset = Product.objects.filter(title__icontains='coffee')
    # queryset = Product.objects.filter(collection__id__range=(1, 2, 3))
    # queryset = Product.objects.filter(collection__id=1)
    # queryset = Product.objects.filter(unit_price__range=(20, 30))
    # queryset = Product.objects.filter(unit_price__gte=20)
    # queryset = Product.objects.filter(pk=0)
    # queryset = Product.objects.filter(pk=0).exists()
    # product = Product.objects.filter(pk=0).first()
    # product = Product.objects.get(pk=0)
    ## Q objects   (query)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__gte=20))  
    # queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__gte=20))  
    ## F objets (field) ex. SELECT * FROM 'store_product' WHERE `store_product`.`inventory` = (`store_product`.`collection_id`)
    # queryset = Product.objects.filter(inventory=F('collection__id'))
    ## Sorting data
    # queryset = Product.objects.order_by('title')
    ## SELECT ••• FROM `store_product` ORDER BY `store_product`.`unit_price` ASC, `store_product`.`title` DESC
    # queryset = Product.objects.order_by('unit_price', '-title')
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # queryset = Product.objects.filter(collect__id=1).order_by('unit_price')
    # queryset = Product.objects.order_by('unit_price')[:3]


def say_hello(request):
    queryset = Product.objects.order_by('unit_price')[:3]
    return render(request, 'hello.html', {'name': 'moshi', 'products': list(queryset)})

if __name__ == '__main__' :
    say_hello()