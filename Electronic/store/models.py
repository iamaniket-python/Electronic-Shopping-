from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
FILTER_PRICE=((
        ('1000-2000','1000-2000'),
        ('2000-3000','2000-3000'),
        ('3000-4000','3000-4000'),
        ('4000-5000','4000-5000'),
        ('5000-6000','5000-6000'),
        ('6000-7000','6000-7000'),
        ('7000-8000','7000-8000'),
        ('8000-9000','8000-9000'),
        ('9000-10000','9000-10000'),
        ('10000-11000','10000-11000'),
        ('11000-12000','11000-12000'),
        ('12000-13000','12000-13000'),
        ('13000-14000','13000-14000'),
        ('14000-15000','14000-15000'),
        ('15000-16000','15000-16000'),
        ('16000-17000','16000-17000'),
        ('17000-18000','17000-18000'),
        ('18000-19000','18000-19000'),
        ('19000-20000','19000-20000'),
    ))
class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Color(models.Model):
    name = models.CharField(max_length=100)
    code=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Filter_price(models.Model):
    
    price =models.CharField(choices=FILTER_PRICE,max_length=60)

    def __str__(self):
        return self.price

class Product(models.Model):
    CONDITION=(
        ('New','New'),
        ('Old','Old'),
        )
    
    STOCK=(
        ('In Stock','In Stock'),
        ('Out of Stock','Out of Stock'),
    )
     
    STATUS=(
        ('Publish','Publish'),
        ('Draft','Draft'),
    )
    unique_id =models.CharField(unique=True,max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='image/product_image')
    name = models.CharField(max_length=200)
    price =models.IntegerField()
    condition = models.CharField(choices=CONDITION,max_length=100)
    information = models.TextField(null=True)
    description = models.TextField(null=True)
    stock =models.CharField(choices=STOCK,max_length=100)
    status=models.CharField(choices=STATUS,max_length=200)
    created_date=models.DateTimeField(default=timezone.now,)



    Category =models.ForeignKey(Categories,on_delete=models.CASCADE)
    Brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    Color=models.ForeignKey(Color,on_delete=models.CASCADE)
    Filter_price=models.ForeignKey(Filter_price,on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%y%m%d24')+ str(self.id)
        return super().save(*args, **kwargs)
    

    def __str__(self):
        
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to='image/product_image')
    product =models.ForeignKey(Product,on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject=models.CharField(max_length=300)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class Order(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    postcode=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField(max_length=200)
    additional_info=models.TextField()
    amount=models.CharField(max_length=200)
    payment_id=models.CharField(default=False,null=True,max_length=200)
    paid=models.BooleanField(default=False,null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.User.username
    

class Orderitem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image/product_image')
    quantity=models.IntegerField()
    price=models.CharField(max_length=200)
    total=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.username
    
