from django.contrib import admin
from .models import principal, faculty, student

class principaldata(admin.ModelAdmin):
    list_display=['id', 'firstname', 'lastname', 'username', 'password', 'experience', 'salary', 'attendance']
admin.site.register(principal, principaldata)

class facultydata(admin.ModelAdmin):
    list_display=['id', 'firstname', 'lastname', 'username', 'password', 'experience', 'salary', 'subject', 'attendance']
admin.site.register(faculty, facultydata)

class stundentdata(admin.ModelAdmin):
    list_display=['id', 'firstname', 'lastname', 'email', 'contact', 'city', 'attendance', 'feespending', 'remarks']
admin.site.register(student, stundentdata)
