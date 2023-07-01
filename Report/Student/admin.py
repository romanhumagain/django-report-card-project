from django.contrib import admin
from Student.models import Department, Student, StudentId, Subject, SubjectMarks, TotalMark

# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentId)
admin.site.register(Subject)
admin.site.register(SubjectMarks)
admin.site.register(TotalMark)