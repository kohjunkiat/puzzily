from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import StudentSignUpForm, TutorSignUpForm
from .models import User

# Create your views here.
# def signup(request):
# 	if request.method == 'POST':
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			return redirect('home')
# 	else:
# 		form = UserCreationForm()		
# 	return render(request, 'signups.html', {'form': form})

def signup(request):
	return render(request, 'signups.html')

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class TutorSignUpView(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tutor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

# student = Student.objects.get(user=self)
# student.profilepic = form.cleaned_data['profilepic']
# student.save()