from django.contrib import admin
from .models import Tutorial, Student, Session, Attendance

# Register your models here.
admin.site.register(Tutorial)
admin.site.register(Student)
admin.site.register(Session)
admin.site.register(Attendance)