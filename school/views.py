from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.


def home(request):
    student_data = Student.objects.all()

    # student_data = Student.objects.filter(marks=60)
    
    # student_data = Student.objects.exclude(marks=60)
    
    # student_data = Student.objects.order_by('-marks')
    
    # student_data = Student.objects.order_by('id').reverse()[:5]
    
    # student_data = Student.objects.values('name','city')
    
    # student_data = Student.objects.using('default')
    
    # student_data = Student.objects.dates('pass_date','month')
    
    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # student_data = qs2.union(qs1, all=True)

    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # student_data = qs2.intersection(qs1)

    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # student_data = qs1.difference(qs2)

    ###########  and/or operator

    # student_data = Student.objects.filter(id=8, roll=108)

    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=107)




    print('Return:',student_data)
    print()
    print('SQL Query:', student_data.query)

    return render(request, 'school/home.html', {'students':student_data})