from django.shortcuts import render,redirect
from resumeApp.models import ResumeModel,ResumeEducationModel,ResumeWorkModel

def home(request):
    resumedata=ResumeModel.objects.all()
    educationdata=ResumeEducationModel.objects.all()
    workdata=ResumeWorkModel.objects.all()
    
    resume={
        'resumedata':resumedata,
        'educationdata':educationdata,
        'workdata':workdata,
    }
    return render(request,'home.html',resume)

def addresume(request):
    if request.method=="POST":
        profile_picture=request.FILES.get('profile_picture')
        full_name=request.POST.get('full_name')
        address=request.POST.get('address')
        phone_number=request.POST.get('phone_number')
        email_address=request.POST.get('email_address')
        career_objective=request.POST.get('career_objective')
        hard_Skills=request.POST.get('hard_Skills')
        soft_Skills=request.POST.get('soft_Skills')
        certifications=request.POST.get('certifications')
        projects=request.POST.get('projects')
        references=request.POST.get('references')
        degree=request.POST.get('degree')
        institution=request.POST.get('institution')
        graduation_year=request.POST.get('graduation_year')
        company=request.POST.get('company')
        position=request.POST.get('position')
        start_dates=request.POST.get('start_dates')
        end_dates=request.POST.get('end_dates')
        
        resume=ResumeModel(
            Profile_picture=profile_picture,
            Full_name=full_name,
            Address=address,
            Phone_number=phone_number,
            Email_address=email_address,
            Career_objective=career_objective,
            Hard_Skills=hard_Skills,
            Soft_Skills=soft_Skills,
            Certifications=certifications,
            Projects=projects,
            References=references,
        )
        education=ResumeEducationModel(
            Degree=degree,
            Institution=institution,
            Graduation_year=graduation_year,
        )
        work=ResumeWorkModel(
            Company=company,
            Position=position,
            Start_dates=start_dates,
            End_dates=end_dates,
            
        )
        resume.save()
        education.save()
        work.save()
        
        return redirect('home')
        
    return render(request,'addresume.html')

def deleteresume(request,myid):
    resumedata=ResumeModel.objects.get(id=myid)
    educationdata=ResumeEducationModel.objects.get(id=myid)
    workdata=ResumeWorkModel.objects.get(id=myid)
    
    resumedata.delete()
    educationdata.delete()
    workdata.delete()
    return redirect('home')

def editresume(request,myid):
    resumedata=ResumeModel.objects.get(id=myid)
    educationdata=ResumeEducationModel.objects.get(id=myid)
    workdata=ResumeWorkModel.objects.get(id=myid)
    
    resume={
        'resumedata':resumedata,
        'educationdata':educationdata,
        'workdata':workdata,
    }
    return render(request,'editresume.html',resume)

def updateresume(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        profile_picture=request.FILES.get('profile_picture')
        full_name=request.POST.get('full_name')
        address=request.POST.get('address')
        phone_number=request.POST.get('phone_number')
        email_address=request.POST.get('email_address')
        career_objective=request.POST.get('career_objective')
        hard_Skills=request.POST.get('hard_Skills')
        soft_Skills=request.POST.get('soft_Skills')
        certifications=request.POST.get('certifications')
        projects=request.POST.get('projects')
        references=request.POST.get('references')
        degree=request.POST.get('degree')
        institution=request.POST.get('institution')
        graduation_year=request.POST.get('graduation_year')
        company=request.POST.get('company')
        position=request.POST.get('position')
        start_dates=request.POST.get('start_dates')
        end_dates=request.POST.get('end_dates')
        
        if profile_picture:
            resume=ResumeModel(
                id=myid,
                Profile_picture=profile_picture,
                Full_name=full_name,
                Address=address,
                Phone_number=phone_number,
                Email_address=email_address,
                Career_objective=career_objective,
                Hard_Skills=hard_Skills,
                Soft_Skills=soft_Skills,
                Certifications=certifications,
                Projects=projects,
                References=references,
            )
            education=ResumeEducationModel(
                id=myid,
                Degree=degree,
                Institution=institution,
                Graduation_year=graduation_year,
            )
            work=ResumeWorkModel(
                id=myid,
                Company=company,
                Position=position,
                Start_dates=start_dates,
                End_dates=end_dates,
                
            )
        else:
            resumebyid=ResumeModel.objects.get(id=myid)
            resume=ResumeModel(
                id=myid,
                Profile_picture=resumebyid.Profile_picture,
                Full_name=full_name,
                Address=address,
                Phone_number=phone_number,
                Email_address=email_address,
                Career_objective=career_objective,
                Hard_Skills=hard_Skills,
                Soft_Skills=soft_Skills,
                Certifications=certifications,
                Projects=projects,
                References=references,
            )
            education=ResumeEducationModel(
                id=myid,
                Degree=degree,
                Institution=institution,
                Graduation_year=graduation_year,
            )
            work=ResumeWorkModel(
                id=myid,
                Company=company,
                Position=position,
                Start_dates=start_dates,
                End_dates=end_dates,
                
            )
        resume.save()
        education.save()
        work.save()
    return redirect('home')

def viewresume(request,myid):
    resumedata=ResumeModel.objects.get(id=myid)
    educationdata=ResumeEducationModel.objects.get(id=myid)
    workdata=ResumeWorkModel.objects.get(id=myid)
    
    resume={
        'resumedata':resumedata,
        'educationdata':educationdata,
        'workdata':workdata,
    }
    return render(request,'viewresume.html',resume)