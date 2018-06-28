from django.db import models

# Create your models here.
class Tutorial(models.Model):
	module = models.CharField(max_length=30)
	group = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.module + self.group

	def get_students_count(self):
		return Student.objects.filter(tutorial=self).count()

	def get_sessions_count(self):
		return Session.objects.filter(tutorial=self).count()

class Student(models.Model):
	nusid = models.CharField(max_length=30, unique=True)
	tutorial = models.ManyToManyField(Tutorial)
	profilepic = models.ImageField(upload_to='profile', default='default.png')

	def __str__(self):
		return self.nusid

	def get_attendance(self):
		try:
			attendance = Attendance.objects.get(student=self)
			if attendance.attended == True:
				return 1
			else:
				return 0
		except Attendance.DoesNotExist:
			return 0

class Session(models.Model):
	date = models.DateTimeField()
	tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='session_image', default='default.png')

	def __str__(self):
		return self.tutorial.module + ', ' + self.tutorial.group + ', ' + str(self.date)

class Attendance(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	session = models.ForeignKey(Session, on_delete=models.CASCADE)
	attended = models.BooleanField(default=False)