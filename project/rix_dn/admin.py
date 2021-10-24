from django.contrib import admin
from .models import *


class CarePlanAdmin(admin.ModelAdmin):
	model = CarePlan
	list_display = ("date", "topic", "patient")


class CarePlanInline(admin.StackedInline):
	model = CarePlan
	extra = 1

class PatientAdmin(admin.ModelAdmin):
	model = Patient
	inlines = [
		CarePlanInline
	]

# Register your models here.
admin.site.register(Topic)
admin.site.register(Resource)
admin.site.register(Measure)
admin.site.register(Goal)
admin.site.register(Patient, PatientAdmin)
admin.site.register(CarePlan, CarePlanAdmin)