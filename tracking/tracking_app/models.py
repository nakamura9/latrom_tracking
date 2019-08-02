from django.db import models
from django.urls import reverse

class Customer(models.Model):
    ROLE_CHOICES = [
        (0, 'End User'),
        (1, 'Distributor')
    ]

    parent_customer = models.ForeignKey('tracking_app.customer', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True)
    name_of_customer = models.CharField(max_length=255)
    login_account = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    roles = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=0)
    contacts = models.CharField(max_length=255, blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    address = models.CharField(max_length=255, blank=True, default="")

    def get_absolute_url(self):
        return reverse("tracking:customer-detail", kwargs={"pk": self.pk})
    
    @property
    def role_string(self):
        return dict(self.ROLE_CHOICES)[self.roles]

    @property
    def total_devices(self):
        return 5#TODO fix

    @property
    def purchased(self):
        return 3#TODO fix

    def __str__(self):
        return self.name_of_customer


class Device(models.Model):
    customer = models.ForeignKey('tracking_app.customer', 
        null=True, 
        on_delete=models.SET_NULL)
    id_number = models.IntegerField()
    creation_date = models.DateField(auto_now=True)
    type=models.CharField(max_length=16)
    activation_time = models.DateField(null=True, blank=True)
    expired_time = models.TimeField(null=True, blank=True)
    expired_date = models.DateField(null=True, blank=True)
    target_name = models.CharField(max_length=255,blank=True, default="")
    filter_lbs = models.BooleanField()
    sim_card_no = models.CharField(max_length=255,blank=True, default="")
    license_plate_no = models.CharField(max_length=255,blank=True, default="")
    phone_no = models.CharField(max_length=255,blank=True, default="")
    fuel_per_100km = models.CharField(max_length=255,blank=True, default="")
    contacts_no = models.CharField(max_length=255,blank=True, default="")
    remark = models.TextField(blank=True, default="")
    overspeed_km_hr = models.FloatField(default=80.0)
    icon=models.CharField(max_length=32, choices=[
        ('car', 'car'),
        ('truck', 'truck'),
        ('bus', 'bus'),
        ('bike', 'bike'),
        ('boat', 'boat'),
        ('person', 'person'),
        ('lock', 'lock'),
    ], default='car')

    @property
    def name(self):
        return f"{self.type}-{self.id_number}"

    def __str__(self):
        return self.name