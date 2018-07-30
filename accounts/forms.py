from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from attendance.models import Student
from .models import User

class StudentSignUpForm(UserCreationForm):
    profilepic = forms.ImageField(
        required=True,
        label="Profile Picture"
    )

    nusid = forms.CharField(
        label="NUS ID",
        max_length=30, 
    )

    name = forms.CharField(
        label="Full Name",
        max_length=30, 
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("nusid", "name", "username", "password1", "password2", "profilepic")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.name = self.cleaned_data['name']
        student.nusid = self.cleaned_data['nusid']
        student.profilepic = self.cleaned_data['profilepic']
        student.save()
        return user

class TutorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        if commit:
            user.save()
        return user