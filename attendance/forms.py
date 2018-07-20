from django import forms
from attendance.models import Session, Tutorial

class ImageForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = [
        	"image", 
    	]

class TutorialForm(forms.ModelForm):
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