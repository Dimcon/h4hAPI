import uuid as uuid
from django.db import models

# Create your models here.



class Staff(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=uuid.uuid4,
        editable=False
    )
    role = models.CharField(max_length=256)
    firstname = models.CharField(max_length=256)
    lastnames = models.CharField(max_length=256)
    id_number = models.CharField(max_length=128)
    dateOfBirth = models.DateField()
    contactNumber = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    deletedOn = models.DateTimeField(null=True, blank=True)

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
    dateOfBirth = models.DateField()
    contactNumber = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    deletedOn = models.DateTimeField(null=True, blank=True)
    createdBy = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)


class Symptom(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=uuid.uuid4,
        editable=False
    )
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    name = models.CharField(null=True, max_length=256, blank=True)
    description = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    deletedOn = models.DateTimeField(null=True, blank=True)
    createdBy = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)


class Booking(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=uuid.uuid4,
        editable=False
    )
    foreignKeyType = models.CharField(max_length=256)
    foreignKey = models.CharField(max_length=256)
    startTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
    comments = models.TextField(blank=True)
    cancellationReason = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    deletedOn = models.DateTimeField(null=True, blank=True)
    createdBy = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)


class Theatre(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    hospitalWing = models.CharField(max_length=256, blank=True)
    Category = models.CharField(max_length=256, blank=True)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    deletedOn = models.DateTimeField(null=True, blank=True)
    createdBy = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)


class Clinic(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    hospitalWing = models.CharField(max_length=256, blank=True)
    Category = models.CharField(max_length=256, blank=True)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    deletedOn = models.DateTimeField(null=True, blank=True)
    createdBy = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)


class Notification(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=uuid.uuid4,
        editable=False
    )
    foreignKeyType = models.CharField(max_length=256)
    foreignKey = models.CharField(max_length=256)
    shortText = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    deletedOn = models.DateTimeField(null=True, blank=True)
    createdBy = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
