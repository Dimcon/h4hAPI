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
from .serializers import PatientSerializer


class PatientView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    url_name = 'patient-list'


class PatientDetailView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    url_name = 'patient-detail'
