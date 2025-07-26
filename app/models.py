from django.db import models
# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Color(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    type_obj=models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type_obj')
    category_obj = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_obj')
    Color_obj=models.ManyToManyField(Color,related_name='color_obj')

    is_gold_plated=models.BooleanField(default=False)

    name = models.CharField(max_length=200)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    image5 = models.ImageField(upload_to='products/', blank=True, null=True)

    stock = models.PositiveIntegerField(default=0)

    tag=models.CharField(max_length=100,null=True,blank=True)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class CartItem(models.Model):

    session_id = models.CharField(max_length=100) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_obj')
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        unique_together= ('session_id', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    def total_price(self):
        return self.quantity*self.product.price


class Address(models.Model):

    session_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    landmark = models.CharField(max_length=100, blank=True)

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}, {self.city}"