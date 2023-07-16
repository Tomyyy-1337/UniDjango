from django.contrib import admin
from .models import *
# Register your models here.

class Student_Admin(admin.ModelAdmin):
	list_display = ('matnr', 'name',)
	filter_horizontal = ('hoert',)
admin.site.register(Student, Student_Admin)

class Professor_Admin(admin.ModelAdmin):
	list_display = ('name', 'persnr', )
admin.site.register(Professor, Professor_Admin)

class Vorlesung_Admin(admin.ModelAdmin):
	list_display = ('vorlnr', 'titel', 'dozent',)
	list_filter = ('dozent',)
	list_editable = ('dozent',)
admin.site.register(Vorlesung, Vorlesung_Admin)

class Pruefung_Admin(admin.ModelAdmin):
        list_display = ('student', 'vorlesung', 'note', 'datum',)
        list_filter = ('student',)
admin.site.register(Pruefung, Pruefung_Admin)
