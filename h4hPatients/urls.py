
from django.urls import path

from h4hPatients import views

urlpatterns = [
    path('patients', views.PatientView.as_view(),
         name=views.PatientView.url_name),
    path('patients/<slug:pk>', views.PatientDetailView.as_view(), name=views.PatientDetailView.url_name),

    path('staff', views.StaffView.as_view(),
         name=views.StaffView.url_name),
    path('staff/<slug:pk>', views.StaffDetailView.as_view(),
         name=views.StaffDetailView.url_name),

    path('symptom', views.SymptomView.as_view(),
         name=views.SymptomView.url_name),
    path('symptoms/<slug:pk>', views.SymptomDetailView.as_view(),
         name=views.SymptomDetailView.url_name),

    path('bookings', views.BookingView.as_view(),
         name=views.BookingView.url_name),
    path('bookings/<slug:pk>', views.BookingDetailView.as_view(),
         name=views.BookingDetailView.url_name),

    path('theatres', views.TheatreView.as_view(),
         name=views.TheatreView.url_name),
    path('theatres/<slug:pk>', views.TheatreDetailView.as_view(),
         name=views.TheatreDetailView.url_name),

    path('clinics', views.ClinicView.as_view(),
         name=views.ClinicView.url_name),
    path('clinics/<slug:pk>', views.ClinicDetailView.as_view(),
         name=views.ClinicDetailView.url_name),

    path('notifications', views.NotificationView.as_view(),
         name=views.NotificationView.url_name),
    path('notifications/<slug:pk>', views.NotificationDetailView.as_view(),
         name=views.NotificationDetailView.url_name),

]