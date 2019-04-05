from django.contrib import admin
from .models import Telecaller, Enquiry, Admission

# Register your models here.
admin.site.register(Telecaller)
admin.site.register(Enquiry)
admin.site.register(Admission)