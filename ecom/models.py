from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Ulanyjy ady")
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True,
                                    verbose_name="Suraty")
    address = models.CharField(max_length=40, verbose_name="Salgysy")
    mobile = models.CharField(max_length=20, null=False, verbose_name="Ykjam el telefony")

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    name = models.CharField(max_length=40, verbose_name="Önümiň ady")
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True, verbose_name="Önümiň suraty")
    price = models.PositiveIntegerField(verbose_name="Önümiň bahasy")
    description = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}-{self.product_image}-{self.price}-{self.description}'


class Orders(models.Model):
    STATUS = (
        ('Pending', 'Garaşylýar'),
        ('Order Confirmed', 'Sargyt kabul edildi'),
        ('Out for Delivery', 'Ýolda'),
        ('Delivered', 'Gowşuryldy'),
    )
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, verbose_name="Ulanyjy")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, verbose_name="Önüm")
    email = models.CharField(max_length=50, null=True, verbose_name="E-mail salgy")
    address = models.CharField(max_length=500, null=True, verbose_name="Ulayjynyň salgysy")
    mobile = models.CharField(max_length=20, null=True, verbose_name="Ykjam el telefony")
    order_date = models.DateField(auto_now_add=True, null=True, verbose_name="Sargydyň wagty")
    status = models.CharField(max_length=50, null=True, choices=STATUS, )

    def __str__(self):
        return self.product

class Feedback(models.Model):
    name = models.CharField(max_length=40, verbose_name="Ady")
    feedback = models.CharField(max_length=500, verbose_name="Garaýyş")
    date = models.DateField(auto_now_add=True, null=True, verbose_name="Wagty")

    def __str__(self):
        return self.name
