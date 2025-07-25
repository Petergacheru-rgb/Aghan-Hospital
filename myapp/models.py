from django.db import models

# Create your models here.
class Patient1(models.Model):
    firstname =models.CharField(max_length=100)
    lastname =models.CharField(max_length=100)
    email = models.EmailField()
    contact =models.CharField(max_length=20)
    medicalHistory =models.TextField()
    dob = models.DateField()

    def __str__(self):
        return self.firstname + " " + self.lastname


class Doctors1(models.Model):
    fullname =models.CharField(max_length=100)
    doctorid = models.IntegerField()
    age =models.IntegerField()
    department =models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

#Ward Model-Name,capacity,department,floor

class Ward1(models.Model):
    Name =models.CharField(max_length=100)
    Capacity =models.CharField(max_length=100)
    Department =models.CharField(max_length=100)
    Floor =models.IntegerField()
    def __str__(self):
        return self.Name

class Appointment(models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField()
    phone =models.CharField(max_length=20)
    datetime = models.DateTimeField()
    department =models.CharField(max_length=100)
    doctor =models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name

class Contact1(models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField()
    subject =models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name


class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"