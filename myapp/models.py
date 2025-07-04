from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname =models.CharField(max_length=100)
    lastname =models.CharField(max_length=100)
    email = models.EmailField()
    contact =models.CharField(max_length=20)
    medicalHistory =models.TextField()
    dob = models.DateField()

    def __str__(self):
        return self.firstname + " " + self.lastname


class Doctors (models.Model):
    fullname =models.CharField(max_length=100)
    doctorid = models.IntegerField()
    age =models.IntegerField()
    department =models.CharField()

    def __str__(self):
        return self.fullname

#Ward Model-Name,capacity,department,floor

class Ward (models.Model):
    Name =models.CharField(max_length=100)
    Capacity =models.CharField()
    Department =models.CharField(max_length=100)
    Floor =models.IntegerField()
    def __str__(self):
        return self.Name

class Appointment (models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField()
    phone =models.CharField(max_length=20)
    datetime = models.DateTimeField()
    department =models.CharField(max_length=100)
    doctor =models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name

class Contact (models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField()
    subject =models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name
