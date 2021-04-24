from django.contrib import admin

from h4hPatients.models import *

# Register your models here.
class staffModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Staff, staffModelAdmin)


class symptomModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Symptom, symptomModelAdmin)


class patientModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, patientModelAdmin)


class bookingModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Booking, bookingModelAdmin)


class theatreModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Theatre, theatreModelAdmin)


class clinicModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Clinic, clinicModelAdmin)


class notificationModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notification, notificationModelAdmin)

