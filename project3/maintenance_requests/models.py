from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Maintenance_Request(models.Model):
    issue = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default="Pending")
    image = models.ImageField(upload_to='uploads/', blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["status"]

    def __str__(self):
        return f"{self.id}, {self.issue}, {self.status}"

def add_request(issue, image):
    request = Maintenance_Request()
    request.issue = issue
    request.image = image
    request.status = "Pending"
    request.save()
    return request

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    date_check_in = models.DateTimeField()
    date_check_out = models.DateTimeField()
    apartment = models.IntegerField()

    class Meta:
        ordering = ["apartment"]

    def __str__(self):
        return f"{self.id}, {self.name}, {self.apartment}"
    
def add_tenant(name, email, phone, apartment, date_in, date_out):
    tenant = Tenant(name=name, email=email, phone=phone, apartment=apartment, date_check_in=date_in, date_check_out=date_out)
    tenant.save()
    return tenant