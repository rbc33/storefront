from django.shortcuts import render
from django.db import transaction, connection
from django.contrib.contenttypes.models import ContentType
from store.models import *

    # # django ORM examples
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
    # # Q objects   (query)
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__gte=20))  
    # queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__gte=20))  
    # # F objets (field) ex. SELECT * FROM 'store_product' WHERE `store_product`.`inventory` = (`store_product`.`collection_id`)
    # queryset = Product.objects.filter(inventory=F('collection__id'))
    # # Sorting data
    # queryset = Product.objects.order_by('title')
    # # SELECT ••• FROM `store_product` ORDER BY `store_product`.`unit_price` ASC, `store_product`.`title` DESC
    # queryset = Product.objects.order_by('unit_price', '-title')
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # queryset = Product.objects.filter(collect__id=1).order_by('unit_price')
    # # Sorting
    # queryset = Product.objects.order_by('unit_price')[:3]
    # queryset = Product.objects.all()[5:3]
    # # Selecting Fields to query
    # queryset = Product.objects.values('id', 'title')
    # queryset = Product.objects.values('id', 'title', 'collection__title') reurns a dictionaty
    # queryset = Product.objects.values_list('id', 'title', 'collection__title') returns a tuple of the values
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title') Select products that have been ordered and sort them by title
    # # select_related (1) a product has 1 collection
    # queryset = Product.objects.select_related('collection__someOtherField').all()
    # # prefetch_related (n)obj a product may have many promotions
    # queryset = Product.objects.prefetch_related('promotions').all()
    # # Combined select_related and prefetch_related
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # # select last 5 orders with customers and items (products)
    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # # Agregatting Objects
    # queryset = Product.objects.filter(collection__id=3).aggregate(avg_price=Avg('unit_price'),min_price=Min('unit_price'),max_price=Max('unit_price'))
    # # Annotating Objects
    # queryset = Customer.objects.annotate(is_new=F('id')+ 1)
    # # db.Functions
    # queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    # # queryset = Customer.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
    # # Grouping data
    # queryset = Customer.objects.annotate(orders_count=Count('order'))
    # # Expresion Wrapper
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(discounted_price=discounted_price)
    # queryset = Customer.object.annotate(total_spent=F('order__orderitem__unit_price')*F('order__orderitem_quantity'))
    # queryset = Product.objects.annotate(total_sold=F('orderitem__quantity') * F('orderitem__unit_price')).order_by('-total_sold')[:5]
    # # adding method to tag.model for content_type relationships
    # TaggedItem.objects.get_tags_for(Product, 1)
    # # Creating objects (last line equal to the 4 previous but if you rename an instance, doesnt change automatically bc it's part of an argument)
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    # collection = Collection.objects.create(title='Video Games', featured_product_id=1)
    # # Deleteting collection
    # collection = Collection(pk=1)
    # collection.delete()
    # queryset = Collection.objects.filter(id__gt=5).delete()
    # # Create cart
    # cart = Cart()
    # cart.save()
    # item1 = CartItem()
    # item1.cart= cart
    # item1.quantity = 1
    # item1.product_id = 1
    # item1.save()
    # # update quantity of item
    # item1 = CartItem.objects.get(pk=1)
    # item1.quantity = 2
    # item.save()
    # # Delete cart
    # cart = Cart(pk=1)
    # cart.delete()   # last 2 lines = to next line
    # cart = Cart.objects.filter(pk=1).delete()
# # Decorator @transaction.atomic() ensure each line and if one fails doesnt call the funcition
# @transaction.atomic()
# def say_hello(request):
#     order = Order()
#     order.customer_id = 1
#     order.save()

#     item = OrderItem()
#     item.order = order
#     item.product_id = 1
#     item.quantity = 1
#     item.unit_price = 10
#     item.save()

#     return render(request, 'hello.html', {'name': 'moshi', 'item1': item})

# # Deleted all that shitty entries:
# def say_hello(request):

#     # code to execute before the content manager <transaction.atomic()>

#     with transaction.atomic():
#         order = Order()
#         items_deleted = OrderItem.objects.filter(pk__lte=6, order__lte=1).delete()
    # return render(request, 'hello.html', {'name': 'moshi', 'item1': items_deleted })
    # # RAW SQL 
    # queryset = Product.objects.raw('SELECT id, title FROM store_product')
    # # example with a cursor object w/o a wrapper
    # cursor = connection.cursor()
    # cursor.execute('')
    # cursor.close()
    # #cursor with a wrapper
    # with connection.cursor() as cursor:
    #     cursor.execute('')
    # #cursor with a wrapper
    # with connection.cursor() as cursor:
    #     cursor.callproc('get_customers', [1, 2, 'a'])

def say_hello(request):
    return render(request, 'hello.html', {'name': 'moshi', 'item1': 'list(queryset)' })


if __name__ == '__main__' :
    say_hello()