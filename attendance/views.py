from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views import generic
from .models import Tutorial, Student, Session
from .forms import UploadImageForm

from somewhere import handle_uploaded_file

# Create your views here.
@login_required
def home(request):
	tutorials = Tutorial.objects.order_by('module', 'group')
	return render(request, 'home.html', {'tutorials': tutorials})

def attlist(request, group):
	students = Student.objects.filter(tutorial__group=group).order_by('nusid')
	sessions = Session.objects.filter(tutorial__group=group).order_by('date')
	return render(request, 'attlist.html', {'students': students, 'sessions' : sessions})

def search(request):
	if request.GET.get('query', None):
		tutorials = Tutorial.objects.filter(module__icontains=request.GET.get('query', None))
	else:
		tutorials = Tutorial.objects.order_by('module', 'group')
	return render(request, 'home.html', {'tutorials': tutorials})

# def UploadImage(request):
#     if request.method == 'POST':
#         form = UploadImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#     else:
#         form = UploadImageForm()
#     return render(request, 'upload.html', {'form': form})
