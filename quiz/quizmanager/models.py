from django.db import models
from users.models import User


class Exam(models.Model):
    exam_name=models.CharField(max_length=20,unique=True)
    created_on=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='exams'


class Section(models.Model):
    section_name=models.CharField(max_length=20,unique=True)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='sections'


class Topic(models.Model):
    topic_name=models.CharField(max_length=20,unique=True)
    section=models.ForeignKey(Section,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='topics'


class Questions(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    question=models.TextField()
    photo = models.CharField(max_length=20) # file name uniquely saved
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)

    class Meta:
        db_table='questions'
