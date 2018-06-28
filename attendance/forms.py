from django import forms
from attendance.models import Session

class ImageForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = [
        	"image", 
    	]