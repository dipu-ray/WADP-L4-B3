from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.http import FileResponse
from pyhtml2pdf import converter
import io
import os
from resumeapp.models import ResumeModel,EducationModel,WorkModel
def homepage(request):
    return render(request,'base.html')

def resumetable(request):
    resume=ResumeModel.objects.all()
    resumeData={
        'resume':resume
    }
    return render(request,'resumetable.html',resumeData)

def addresume(request):
    return render(request,'addresume.html')

def addresume(request):
    if request.method=='POST':
        profile_pic = request.FILES.get('profile_pic')
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email_address = request.POST.get('email_address')
        career_objective = request.POST.get('career_objective')
        degree = request.POST.get('degree')
        institution = request.POST.get('institution')
        graduation_year = request.POST.get('graduation_year')
        company = request.POST.get('company')
        position = request.POST.get('position')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        hard_skills = request.POST.get('hard_skills')
        soft_skills = request.POST.get('soft_skills')
        certifications = request.POST.get('certifications')
        projects = request.POST.get('projects')
        references = request.POST.get('references')

        resume = ResumeModel(
            Profile_pic=profile_pic,
            Full_name=full_name,
            Address=address,
            Phone_number=phone_number,
            Email_address=email_address,
            Career_objective=career_objective,
            Hard_skills=hard_skills,
            Soft_skills=soft_skills,
            Certifications=certifications,
            Projects=projects,
            References=references,
        )
        education=EducationModel(
            Degree=degree,
            Institution=institution,
            Graduation_year=graduation_year,
        )
        work = WorkModel(
            Company=company,
            Position=position,
            Start_date=start_date,
            End_date=end_date,
        )
        resume.save()
        education.save()
        work.save()
        return redirect('resumetable')
    return render(request,'addresume.html')

def deleteresume(request,myid):
    resume = ResumeModel.objects.get(id=myid)
    education = EducationModel.objects.get(id=myid)
    work = WorkModel.objects.get(id=myid)
    resume.delete()
    education.delete()
    work.delete()
    return redirect('resumetable')

def editresume(request,myid):
    resume = ResumeModel.objects.get(id=myid)
    education = EducationModel.objects.get(id=myid)
    work = WorkModel.objects.get(id=myid)
    resumedata={
        'resume':resume,
        'education':education,
        'work':work,
    }
    return render(request,'editresume.html',resumedata)

def updateresume(request):
    if request.method=='POST':
        myid = request.POST.get('myid')
        profile_pic = request.FILES.get('profile_pic')
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email_address = request.POST.get('email_address')
        career_objective = request.POST.get('career_objective')
        degree = request.POST.get('degree')
        institution = request.POST.get('institution')
        graduation_year = request.POST.get('graduation_year')
        company = request.POST.get('company')
        position = request.POST.get('position')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        hard_skills = request.POST.get('hard_skills')
        soft_skills = request.POST.get('soft_skills')
        certifications = request.POST.get('certifications')
        projects = request.POST.get('projects')
        references = request.POST.get('references')

        if profile_pic:
            resume = ResumeModel(
                id=myid,
                Profile_pic=profile_pic,
                Full_name=full_name,
                Address=address,
                Phone_number=phone_number,
                Email_address=email_address,
                Career_objective=career_objective,
                Hard_skills=hard_skills,
                Soft_skills=soft_skills,
                Certifications=certifications,
                Projects=projects,
                References=references,
            )
            education=EducationModel(
                id=myid,
                Degree=degree,
                Institution=institution,
                Graduation_year=graduation_year,
            )
            work = WorkModel(
                id=myid,
                Company=company,
                Position=position,
                Start_date=start_date,
                End_date=end_date,
            )
            resume.save()
            education.save()
            work.save()
        else:
            resumebyid = ResumeModel.objects.get(id=myid)
            resume=ResumeModel(
                id=myid,
                Profile_pic=resumebyid.Profile_pic,
                Full_name=full_name,
                Address=address,
                Phone_number=phone_number,
                Email_address=email_address,
                Career_objective=career_objective,
                Hard_skills=hard_skills,
                Soft_skills=soft_skills,
                Certifications=certifications,
                Projects=projects,
                References=references,
            )
            education=EducationModel(
                id=myid,
                Degree=degree,
                Institution=institution,
                Graduation_year=graduation_year,
            )
            work = WorkModel(
                id=myid,
                Company=company,
                Position=position,
                Start_date=start_date,
                End_date=end_date,
            )
            resume.save()
            education.save()
            work.save()
        return redirect('resumetable')
    
def viewresume(request,myid):
    global Down_id
    Down_id = myid
    resume = ResumeModel.objects.get(id=myid)
    education = EducationModel.objects.get(id=myid)
    work = WorkModel.objects.get(id=myid)

    resumedata={
        'resume':resume,
        'education':education,
        'work':work,
    }
    return render(request,'viewresume.html',resumedata)


def downloadresume(request, myid):
    # Run the converter function to generate/update the PDF file
    username=ResumeModel.objects.get(id=myid)
    print(username.Full_name)
    pdf_file = converter.convert(f'http://127.0.0.1:8000/viewresume/{myid}', 'resume.pdf')
    print(f"PDF file path from converter: {pdf_file}")

    # Get the root path of the project
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    print(f"Project root path: {project_root}")

    # If the converter returns a valid file path, use it
    if pdf_file:
        pdf_file_path = pdf_file
    else:
        # Otherwise, construct the file path relative to the project root
        pdf_file_path = os.path.join(project_root, 'resume.pdf')
        print(f"PDF file path: {pdf_file_path}")

    if not os.path.exists(pdf_file_path):
        # Handle the case where the file doesn't exist
        print("Error: PDF file not found.")
        return HttpResponse("Error: Unable to find PDF file.")

    try:
        with open(pdf_file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename=resume.pdf'
            response['Content-Disposition'] = f'attachment; filename={username}-Resume.pdf'
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return HttpResponse("Error: Unable to open PDF file.")

    return response


