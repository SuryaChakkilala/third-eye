from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from accounts.models import CustomUser
import datetime

# Create your models here.
class Medicine(models.Model):
    
    name = models.TextField(default='_')
    price = models.FloatField(validators=[MinValueValidator(1)])
    stock = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(default='-')
    times_ordered = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.id

class CartItem(models.Model):
    item = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.item.price * self.quantity

    def __str__(self):
        return self.product

class Order(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Order Total')
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    postcode = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=250, blank=True)
    user_id = models.CharField(max_length=400, default='.')
    delivered = models.BooleanField(default=False) 

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    item = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=500, default='.')
    date_added = models.DateField(auto_now_add=True)

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.item

class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_appointments')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctor_appointments')
    time = models.CharField(max_length=1000)
    date_of_appointment = models.DateField(validators=[MinValueValidator(datetime.date.today)])
    date_time_booking = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=2000)
    approved = models.BooleanField(default=False)
    suggestion = models.TextField(blank=True, null=True)
    prescription = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.user.username + ' - ' + self.time

    @property
    def fileURL(self):
        try:
            url = self.prescription.url
        except:
            url=''
        return url