from django.db import models

# Create your models here.

class Department(models.Model):
  department = models.CharField(max_length=100)
  
  def __str__(self):
    return self.department
  
  class Meta:
    ordering = ['department']
    
class StudentId(models.Model):
  student_id = models.CharField(max_length=100)
  
  def __str__(self):
    return self.student_id
  

class Subject(models.Model):
  name = models.CharField(max_length=100)

  
  def __str__(self):
    return self.name

class Student(models.Model):
  department = models.ForeignKey(Department , related_name='depart', on_delete=models.CASCADE)
  student_id = models.OneToOneField(StudentId , related_name='studentid', on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  address = models.CharField(max_length=100)
  contact = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class SubjectMarks(models.Model):
  student = models.ForeignKey(Student , related_name='studentmarks' , on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  marks = models.IntegerField()
  
  def __str__(self):
    return f'{self.student.name} {self.subject.name}'
  
  class Meta:
    unique_together = ['student' , 'subject']

class TotalMark(models.Model):
  student_id = models.OneToOneField(StudentId , on_delete=models.CASCADE)
  total_marks = models.IntegerField()
  rank = models.IntegerField(null=True)
  
  

  

