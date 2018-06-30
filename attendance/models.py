from django.db import models
import boto3

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

class Session(models.Model):
	date = models.DateTimeField()
	tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='session_image', default='default.png')
	uploaded = models.BooleanField(default=False)

	def __str__(self):
		return self.tutorial.module + ', ' + self.tutorial.group + ', ' + str(self.date)

class Attendance(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	session = models.ForeignKey(Session, on_delete=models.CASCADE)
	attended = models.BooleanField(default=False)

	def rekog(self):
		rekognition = boto3.client("rekognition")
		response = rekognition.compare_faces(
		    SourceImage={
				"S3Object": {
					"Bucket": 'puzzily',
					"Name": 'do.jpg',
				}
			},
			TargetImage={
				"S3Object": {
					"Bucket": 'puzzily',
					"Name": 'try.jpg',
				}
			},
		)
		sim = response['FaceMatches']['Similarity']
		if sim > 0.5:
			self.attended = True
			self.save(update_fields=['attended'])
			return
		else:
			self.attended = False
			self.save(update_fields=['attended'])
			return