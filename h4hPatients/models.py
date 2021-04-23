import uuid as uuid
from django.db import models

# Create your models here.


class Patient(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=uuid.uuid4,
        editable=False
    )
    firstname = models.CharField(max_length=256)
    lastnames = models.CharField(max_length=256)
    id_number = models.CharField(max_length=128)
    contactNumber = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)


class Doctor(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=uuid.uuid4,
        editable=False
    )

