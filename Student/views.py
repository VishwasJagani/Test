from django.shortcuts import render
from .models import *
from django.db.models import *

# Create your views here.

def student_view(request):

    a = Student.objects.all()

    return render(request , 'Student/view.html' ,{"a":a})

def detail(request,id):
    sum = 0
    a = Mark.objects.filter(student_id=id)

    b = Student.objects.filter(id=id).get()
    
    c = Mark.objects.filter(student_id = id).aggregate(Sum('mark'))

    rank = Student.objects.annotate(mark = Sum('studentmarks__mark')).order_by('-mark')
    # print(rank)
    crank = -1
    i = 1
    for r in rank:
        if id == r.id:
            crank = i
            break
        i += 1

    return render(request, 'Student/detail.html',{"a":a , "b":b , "c":c , "rank":crank})