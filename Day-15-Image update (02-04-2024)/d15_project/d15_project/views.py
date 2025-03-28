from django.shortcuts import render,redirect
from studentapp.models import studentModel,markModel,teacherModel,subjectModel,universityModel

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
        studentImage=request.FILES.get('studentImage')
        
        student=studentModel(
            Name=name,
            Department=department,
            City=city,
            StudentImage=studentImage,
        )
        
        student.save()
        return redirect('student')
    return render(request,'addstudent.html')

def mark(request):
    mark=markModel.objects.all()
    myDict={
        'mark':mark
    }
    return render(request,'mark.html',myDict)

def addmark(request):
    if request.method=='POST':
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        mark=request.POST.get('mark')
        
        mark=markModel(
           Name=name,
           Roll=roll,
           Mark=mark,
        )
        mark.save()
        return redirect('mark')
    return render(request,'addmark.html')

def teacher(request):
    teacher=teacherModel.objects.all()
    myDict={
        'teacher':teacher
    }
    return render(request,'teacher.html',myDict)

def addteacher(request):
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        teacherImage=request.FILES.get('teacherImage')
        
        teacher=teacherModel(
            Name=name,
            Department=department,
            City=city,
            TeacherImage=teacherImage
        )
        teacher.save()
        return redirect('teacher')
    return render(request,'addteacher.html')

def subject(request):
    subject=subjectModel.objects.all()
    myDict={
        'subject':subject
    }
    return render(request,'subject.html',myDict)

def addsubject(request):
    if request.method=='POST':
        name=request.POST.get('name')
        category=request.POST.get('category')
        mark=request.POST.get('mark')
        
        subject=subjectModel(
            Name=name,
            Category=category,
            Mark=mark,
        )
        subject.save()
        return redirect('subject')
    return render(request,'addsubject.html')

def university(request):
    university=universityModel.objects.all()
    myDict={
        'university':university
    }
    return render(request,'university.html',myDict)

def adduniversity(request):
    if request.method=='POST':
        rank=request.POST.get('rank')
        name=request.POST.get('name')
        location=request.POST.get('location')
        
        university=universityModel(
            Rank=rank,
            Name=name,
            Location=location,
        )
        
        university.save()
        return redirect('university')
    return render(request,'adduniversity.html')

def deleteMark(request,myid):
    mark=markModel.objects.get(id=myid)
    mark.delete()
    return redirect('mark')

def deleteStudent(request,myid):
    student=studentModel.objects.get(id=myid)
    student.delete()
    return redirect('student')

def deleteSubject(request,myid):
    subject=subjectModel.objects.get(id=myid)
    subject.delete()
    return redirect('subject')

def deleteTeacher(request,myid):
    teacher=teacherModel.objects.get(id=myid)
    teacher.delete()
    return redirect('teacher')

def deleteUniversity(request,myid):
    university=universityModel.objects.get(id=myid)
    university.delete()
    return redirect('university')

def viewstudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    myDict={
        'student':student
    }
    return render(request,'viewstudent.html',myDict)

def viewteacher(request,myid):
    teacher=teacherModel.objects.filter(id=myid)
    myDict={
        'teacher':teacher
    }
    return render(request,'viewteacher.html',myDict)

def viewmark(request,myid):
    mark=markModel.objects.filter(id=myid)
    myDict={
        'mark':mark
    }
    return render(request,'viewmark.html',myDict)

def viewsubject(request,myid):
    subject=subjectModel.objects.filter(id=myid)
    myDict={
        'subject':subject
    }
    return render(request,'viewsubject.html',myDict)

def viewuniversity(request,myid):
    university=universityModel.objects.filter(id=myid)
    myDict={
        'university':university
    }
    return render(request,'viewuniversity.html',myDict)

def alltable(request):
    student=studentModel.objects.all()
    mark=markModel.objects.all()
    teacher=teacherModel.objects.all()
    subject=subjectModel.objects.all()
    university=universityModel.objects.all()
    myDict={
        'student':student,
        'mark':mark,
        'teacher':teacher,
        'subject':subject,
        'university':university,
    }
    return render(request,'alltable.html',myDict)

def editstudent(request,myid):
    student=studentModel.objects.get(id=myid)
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
        studentImage=request.FILES.get('studentImage')
        print(f"This is image: {studentImage}")
        if studentImage:
            student=studentModel(
                id=myid,
                Name=name,
                Department=department,
                City=city,
                StudentImage=studentImage,
            )
        else:
            studentbyid=studentModel.objects.get(id=myid)
            student=studentModel(
                id=myid,
                Name=name,
                Department=department,
                City=city,
                StudentImage=studentbyid.StudentImage
            )
        student.save()
        return redirect('student')

def editteacher(request,myid):
    teacher=teacherModel.objects.filter(id=myid)
    teacherDict={
        'teacher':teacher
    }
    return render(request,'editteacher.html',teacherDict)

def updateteacher(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')

        teacher=teacherModel(
            id=myid,
            Name=name,
            Department=department,
            City=city,
        )
        teacher.save()
        return redirect('teacher')
    
