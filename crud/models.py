from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    nro_doc = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname
