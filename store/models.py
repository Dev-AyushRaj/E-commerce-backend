from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #product_set


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete= models.SET_NULL, null= True, related_name= '+')

class Product(models.Model):
    titles = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits= 6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete= models.PROTECT)
    promotion = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'

    MEMBERSHIP_CHOICES =[
        (MEMBERSHIP_BRONZE,"BRONZE"),
        (MEMBERSHIP_SILVER,"SILVER"),
        (MEMBERSHIP_GOLD,"GOLD")
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254,unique= True)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(max_length=1, choices = MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['last_name','first_name'])
        ]


class Order(models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_FAILED = "F"
    PAYMENT_STATUS_COMPLETED = "C"
    PAYMENT_STAUS_CHOICES=[
        (PAYMENT_STATUS_PENDING,"Pending"),
        (PAYMENT_STATUS_COMPLETED,"Completed"),
        (PAYMENT_STATUS_FAILED,"Failed")
    ] 
    placed_at = models.DateTimeField(auto_now_add= True)
    payement_staus = models.CharField(max_length=1, choices = PAYMENT_STAUS_CHOICES, default = PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key= True)



class Cart(models.Model):
    cart = models.DateTimeField(auto_now_add= True)


class Cart_items(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

