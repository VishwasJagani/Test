from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Mark(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE , related_name="studentmarks")
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self):
        return f'{self.student.name} - {self.subject.name}'
    