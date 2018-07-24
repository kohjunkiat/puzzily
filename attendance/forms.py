from django import forms
from django.db import transaction
from attendance.models import Session, Tutorial, Student

class ImageForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = [
        	"image", 
    	]

class TutorialForm(forms.ModelForm):
	student = forms.ModelMultipleChoiceField(
	        queryset=Student.objects.all(),
        	widget=forms.CheckboxSelectMultiple,
		)
	class Meta:
		model = Tutorial
		fields = [
			"module",
			"group",
			"student",
		]

class SessionForm(forms.ModelForm):
	class Meta:
		model = Session
		fields = [
			"date",
			"tutorial",
		]