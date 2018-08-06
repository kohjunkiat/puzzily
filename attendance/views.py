from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views import generic
from django.views.generic.list import ListView

from .forms import ImageForm, TutorialForm, SessionForm
from .models import Tutorial, Student, Session, Attendance

import boto3

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
	form = ImageForm(request.POST or None, request.FILES or None)
	session = Session.objects.get(tutorial__group=group, date=date)
	tutorial = Tutorial.objects.get(group=group)
	students = tutorial.student.all()
	
	if request.method == 'POST':
		if form.is_valid():
			i = Session.objects.get(tutorial__group=group, date=date)
			i.image = form.cleaned_data['image']
			i.uploaded = True
			i.save()
			for student in students:
				a = Attendance(student=student, session=session, attended=False)
				a.save()
				
	attendances = Attendance.objects.filter(session=session)
	session = Session.objects.get(tutorial__group=group, date=date)
	tutorial = Tutorial.objects.get(group=group)
	students = tutorial.student.all()

	return render(request, 'attlist.html', {
		'session' : session,
		'students' : students,
		'attendances' : attendances,
		"form" : form
	})

def search(request):
	if request.GET.get('query', None):
		tutorials = Tutorial.objects.filter(module__icontains=request.GET.get('query', None))
	else:
		tutorials = Tutorial.objects.order_by('module', 'group')
	return render(request, 'home.html', {'tutorials': tutorials})

def AddTutorial(request):
	form = TutorialForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			form.save_m2m()
			return redirect('home')
	else:
		form = TutorialForm()
	return render(request, 'tutorial_form.html', {
			"form" : form
		})

def AddSession(request):
	form = SessionForm(request.POST or None, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			session = Session.objects.get(tutorial=form.cleaned_data['tutorial'], date=form.cleaned_data['date'])
			group = session.tutorial.group
			return redirect('sessions', group=group)
	else:
		form = SessionForm()
	return render(request, 'session_form.html', {
			"form" : form
		})

