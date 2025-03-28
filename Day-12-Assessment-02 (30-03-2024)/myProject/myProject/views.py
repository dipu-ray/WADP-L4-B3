from  django.shortcuts import render,redirect
from recruiterapp.models import recruiterModel
def recruiter(request):
    recruiter=recruiterModel.objects.all()
    myDict={
        'recruiter':recruiter
    }
    return render(request,'recruiter.html',myDict)

def addrecruiter(request):
    if request.method=='POST':
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        job_title=request.POST.get('job_title')
        linkedin_profile=request.POST.get('linkedin_profile')
        university=request.POST.get('university')
        degree=request.POST.get('degree')
        languages=request.POST.get('languages')
        years_of_experience=request.POST.get('years_of_experience')

        recruiter=recruiterModel(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            address=address,
            job_title=job_title,
            linkedin_profile=linkedin_profile,
            university=university,
            degree=degree,
            languages=languages,
            years_of_experience=years_of_experience,
        )
        recruiter.save()
        return redirect('recruiter')
    return render(request,'addrecruiter.html')

def deleterecruiter(request,myid):
    recruiter=recruiterModel.objects.get(id=myid)
    recruiter.delete()
    return redirect('recruiter')

def editrecruiter(request,myid):
    recruiter=recruiterModel.objects.filter(id=myid)
    myDict={
        'recruiter':recruiter
    }
    return render(request,'editrecruiter.html',myDict)

def updaterecruiter(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        job_title=request.POST.get('job_title')
        linkedin_profile=request.POST.get('linkedin_profile')
        university=request.POST.get('university')
        degree=request.POST.get('degree')
        languages=request.POST.get('languages')
        years_of_experience=request.POST.get('years_of_experience')

        recruiter=recruiterModel(
            id=myid,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            address=address,
            job_title=job_title,
            linkedin_profile=linkedin_profile,
            university=university,
            degree=degree,
            languages=languages,
            years_of_experience=years_of_experience,
        )
        recruiter.save()
        return redirect('recruiter')
def viewrecruiter(request,myid):
    recruiter=recruiterModel.objects.filter(id=myid)
    myDict={
        'recruiter':recruiter
    }
    return render(request,'viewrecruiter.html',myDict)