
# Register your models here.
from django.contrib import admin
from .models import AgencyModel, FacilityModel


class FacilityInline(admin.StackedInline):
    model = FacilityModel
    extra = 0  # Number of empty forms to display


class AgencyAdmin(admin.ModelAdmin):
    inlines = [FacilityInline]


admin.site.register(AgencyModel, AgencyAdmin)