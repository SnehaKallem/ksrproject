from django.db import models

# Create your models here.

class coursedata(models.Model):
    course_no=models.IntegerField()
    course_name=models.CharField(max_length=30)
    timings=models.TimeField()
    starting_date=models.DateField(max_length=20)
    duration=models.CharField(max_length=30)
    fees=models.IntegerField()
    trainer_name=models.CharField(max_length=30)


class feedback_data(models.Model):
    name=models.CharField(max_length=20)
    ratings=models.IntegerField()
    comments=models.CharField(max_length=30)


class user_course_data(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    mobile=models.IntegerField()
    course=models.CharField(max_length=20)