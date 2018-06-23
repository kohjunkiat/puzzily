from django.db import models

# Create your models here.
class Tutorial(models.Model):
	module = models.CharField(max_length=30)
	group = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.group

	def get_students_count(self):
		return Student.objects.filter(tutorial=self).count()

	def get_sessions_count(self):
		return Session.objects.filter(tutorial=self).count()

class Student(models.Model):
	nusid = models.CharField(max_length=30, unique=True)
	tutorial = models.ManyToManyField(Tutorial)

	def __str__(self):
		return self.nusid

class Session(models.Model):
	date = models.DateTimeField()
	tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)

	def __str__(self):
		return self.tutorial.module + ', ' + self.tutorial.group + ', ' + str(self.date)
		 # + ', ' + str(self.time)
