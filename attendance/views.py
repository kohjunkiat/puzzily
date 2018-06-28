from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views import generic
from django.views.generic.list import ListView

from .forms import ImageForm
from .models import Tutorial, Student, Session, Attendance


class TutorialListView(ListView):
    model = Tutorial
    context_object_name = 'tutorials'
    template_name = 'home.html'

# Create your views here.
@login_required
def sessions(request, group):
	sessions = Session.objects.filter(tutorial__group=group).order_by('date')
	return render(request, 'sessions.html', {
		'sessions' : sessions, 
		'group' : group
	})

def attlist(request, group, date):
	form = ImageForm()
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			i = Session.objects.get(date=date)
			i.image = form.cleaned_data['image']
			i.save()
	students = Student.objects.filter(tutorial__group=group).order_by('nusid')
	sessions = Session.objects.filter(tutorial__group=group, date=date)
	attendances = Attendance.objects.filter(session__date=date, session__tutorial__group=group)

	return render(request, 'attlist.html', {
		'students' : students,
		'sessions' : sessions,
		'attendances' : attendances,
		'group' : group,
		'date' : date,
		"form" : form
	})

def search(request):
	if request.GET.get('query', None):
		tutorials = Tutorial.objects.filter(module__icontains=request.GET.get('query', None))
	else:
		tutorials = Tutorial.objects.order_by('module', 'group')
	return render(request, 'home.html', {'tutorials': tutorials})

def upload(request):
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			i = Session.objects.get(date=date)
			i.image = form.cleaned_data['image']
			i.save()
			return redirect('home')
	else:
		form = ImageForm()
	return render(request, 'attlist.html', {
		'form': form
		})