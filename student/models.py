from django.db import models
from django.contrib.auth.models import User
import datetime

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Student/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name

# New Model for Storing Exam Recordings
class ExamRecording(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='exam_recordings/')
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"Recording by {self.student.username} on {self.timestamp}"
