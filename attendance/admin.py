from django.contrib import admin
from .models import Tutorial, Student, Session

# Register your models here.
admin.site.register(Tutorial)
admin.site.register(Student)
admin.site.register(Session)