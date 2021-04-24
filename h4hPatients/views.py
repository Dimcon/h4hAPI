from django.shortcuts import render


import json

import jwt
# from django.conf import Settings
from rest_framework import generics
from rest_framework import status, mixins
from django.shortcuts import get_object_or_404 as _get_object_or_404
from django.shortcuts import get_list_or_404 as _get_list_or_404
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response

from django.core.exceptions import ValidationError

from django.http import Http404

from .models import *

# Create your views here.
from .serializers import *


class PatientView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    url_name = 'patient-list'


class PatientDetailView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    url_name = 'patient-detail'


class StaffView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    url_name = 'staff-list'


class StaffDetailView(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    url_name = 'staff-detail'


class SymptomView(generics.ListCreateAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    url_name = 'Symptom-list'


class SymptomDetailView(generics.RetrieveAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    url_name = 'Symptom-detail'


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    url_name = 'Booking-list'


class BookingDetailView(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    url_name = 'Booking-detail'


class TheatreView(generics.ListCreateAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer
    url_name = 'Theatre-list'


class TheatreDetailView(generics.RetrieveAPIView):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer
    url_name = 'Theatre-detail'


class ClinicView(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    url_name = 'Clinic-list'


class ClinicDetailView(generics.RetrieveAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    url_name = 'Clinic-detail'


class NotificationView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    url_name = 'Notification-list'


class NotificationDetailView(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    url_name = 'Notification-detail'

