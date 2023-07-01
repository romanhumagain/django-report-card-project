from django.shortcuts import render
from django.db.models import Sum , Q
from . models import *
# Create your views here.

def get_students(request):
    students = Student.objects.all()
    
    for student in students:
        total_marks = SubjectMarks.objects.filter(student=student).aggregate(totalMarks=Sum('marks'))
        existing_total_marks = TotalMark.objects.filter(student_id=student.student_id).exists()

        if not existing_total_marks:
            TotalMark.objects.create(student_id=student.student_id, total_marks=total_marks['totalMarks'])
            
    total_marks = TotalMark.objects.order_by('-total_marks')
    
    previous_total_mark = None
    previous_rank = 0
    
    for total_marks in total_marks:
        if total_marks.total_marks != previous_total_mark:
            rank = previous_rank +1
            previous_rank = rank
            
            total_marks.rank = rank
            total_marks.save()
            previous_total_mark = total_marks.total_marks
        
    search = request.GET.get('search')
    
    if search:
        students = students.filter(Q(name__icontains = search) |
                                   Q(department__department__icontains=search) |
                                   Q(student_id__student_id__icontains = search))
    
    
    context = {'querySet': students}

    return render(request, 'student.html', context)


def see_marks(request , std_id):
   querySet = SubjectMarks.objects.filter(student__student_id__student_id = std_id)
   totalMark = TotalMark.objects.filter(student_id__student_id = std_id )
   
   context = {'data':{'querySet':querySet , 'total_marks':totalMark}}
   
   return render(request , 'marks.html' , context )
  
  
  