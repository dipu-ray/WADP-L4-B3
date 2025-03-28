from django.shortcuts import render,redirect
from studentapp.models import studentModel

def student(request):
    student=studentModel.objects.all()
    myDict={
        'student':student
    }
    return render(request,'student.html',myDict)

def addstudent(request):
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=studentModel(
            Name=name,
            Department=department,
            City=city,
        )
        student.save()
        return redirect('student')
    return render(request,'addstudent.html')

def deletestudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    student.delete()
    return redirect('student')

def editstudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    myDict={
        'student':student
    }
    return render(request,'editstudent.html',myDict)
    
def updatestudent(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=studentModel(
            id=myid,
            Name=name,
            Department=department,
            City=city,
        )
        student.save()
        return redirect('student')