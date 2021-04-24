from rest_framework import serializers

from h4hPatients import models


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = '__all__'


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Symptom
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theatre
        fields = '__all__'

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clinic
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'
