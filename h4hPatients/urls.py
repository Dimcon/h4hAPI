
from django.urls import path

from h4hPatients import views

urlpatterns = {
    path('patients', views.PatientView.as_view(),
         name=views.PatientView.url_name),
    path('patients/<slug:pk>', views.PatientDetailView.as_view(), name=views.PatientDetailView.url_name),
}