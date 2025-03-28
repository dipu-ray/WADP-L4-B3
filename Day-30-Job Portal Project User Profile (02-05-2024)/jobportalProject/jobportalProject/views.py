from django.shortcuts import render,redirect
from jobportalApp.models import CustomUserModel,JobModel,JobRecruiterProfile,JobSeekerProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        picture=request.FILES.get('picture')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        blood_group=request.POST.get('blood_group')
        user_type=request.POST.get('user_type')

        if password==cpassword:
            user=CustomUserModel.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                picture=picture,
                dob=dob,
                address=address,
                blood_group=blood_group,
                user_type=user_type,
            )
            # user.save()
            if user_type == 'recruiter':
                recruiter = JobRecruiterProfile.objects.create(
                user = user
                )
            elif user_type == 'seeker':
                seeker = JobSeekerProfile.objects.create(
                user = user
                )
            return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        print(username)
        print(password)
        user = authenticate(
            username=username,
            password=password,
        )
        print(user)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')

    return render(request,'signin.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def addjob(request):
    if request.method=="POST":
        Job_title=request.POST.get('Job_title')
        Company_name=request.POST.get('Company_name')
        Address=request.POST.get('Address')
        Company_description=request.POST.get('Company_description')
        Job_description=request.POST.get('Job_description')
        Qualification=request.POST.get('Qualification')
        Salary_information=request.POST.get('Salary_information')
        Deadline=request.POST.get('Deadline')
        Designation=request.POST.get('Designation')
        Experience=request.POST.get('Experience')
        
        job=JobModel(
            Job_title=Job_title,
            Company_name=Company_name,
            Address=Address,
            Company_description=Company_description,
            Job_description=Job_description,
            Qualification=Qualification,
            Salary_information=Salary_information,
            Deadline=Deadline,
            Designation=Designation,
            Experience=Experience,
            Created_by=request.user
        )
        job.save()
        return redirect('dashboard')
    return render(request,'recruiter/addjob.html')

@login_required
def deletejob(request,myid):
    job=JobModel.objects.get(id=myid)
    job.delete()
    return redirect('dashboard')

@login_required
def editjob(request,myid):
    job=JobModel.objects.get(id=myid)
    jodDict={
        'job':job
    }
    return render(request,'recruiter/editjob.html',jodDict)

@login_required
def updatejob(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        Job_title=request.POST.get('Job_title')
        Company_name=request.POST.get('Company_name')
        Address=request.POST.get('Address')
        Company_description=request.POST.get('Company_description')
        Job_description=request.POST.get('Job_description')
        Qualification=request.POST.get('Qualification')
        Salary_information=request.POST.get('Salary_information')
        Deadline=request.POST.get('Deadline')
        Designation=request.POST.get('Designation')
        Experience=request.POST.get('Experience')
        
        if Deadline:
            job=JobModel(
                id=myid,
                Job_title=Job_title,
                Company_name=Company_name,
                Address=Address,
                Company_description=Company_description,
                Job_description=Job_description,
                Qualification=Qualification,
                Salary_information=Salary_information,
                Deadline=Deadline,
                Designation=Designation,
                Experience=Experience,
                Created_by=request.user
            )
        else:
            jobbyid=JobModel.objects.get(id=myid)
            job=JobModel(
            id=myid,
            Job_title=Job_title,
            Company_name=Company_name,
            Address=Address,
            Company_description=Company_description,
            Job_description=Job_description,
            Qualification=Qualification,
            Salary_information=Salary_information,
            Deadline=jobbyid.Deadline,
            Designation=Designation,
            Experience=Experience,
            Created_by=request.user
            )
        job.save()
        return redirect('dashboard')

@login_required
def viewsinglejob(request,myid):
    job=JobModel.objects.filter(id=myid)
    jodDict={
        'jobs':job
    }
    return render(request,'viewsinglejob.html',jodDict)


def viewalljob(request):
    jobs = JobModel.objects.all()
    jobDict={
        'jobs':jobs
    }
    return render(request,'viewalljob.html',jobDict)

@login_required
def dashboard(request):
    current_user = request.user
    if current_user.user_type == 'recruiter':
        jobs=JobModel.objects.filter(Created_by=current_user)
    else:
        jobs=JobModel.objects.all()
    jobDict={
        'jobs':jobs
    }
    return render(request,'dashboard.html',jobDict)

@login_required
def editprofile(request):
    return render(request,'editprofile.html')

@login_required
def updateprofile(request):
    if request.method == "POST":
        myid = request.POST.get('myid')
        picture = request.FILES.get('picture')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        blood_group = request.POST.get('blood_group')
        user_type = request.POST.get('user_type')
        
        # seeker info
        seeker_id = request.POST.get('seeker_id')
        skills = request.POST.get('skills')
        work_experience = request.POST.get('work_experience')
        
        # recruiter info
        recruiter_id = request.POST.get('recruiter_id')
        Skills_Required = request.POST.get('Skills_Required')
        Work_Schedule = request.POST.get('Work_Schedule')
        
        print('myid:', myid)
        print('picture:', picture)
        print('first_name:', first_name)
        print('last_name:', last_name)
        print('username:', username)
        print('email:', email)
        print('dob:', dob)
        print('address:', address)
        print('blood_group:', blood_group)
        print('user_type:', user_type)
        print('seeker_id:', seeker_id)
        print('skills:', skills)
        print('work_experience:', work_experience)
        print('recruiter_id:', recruiter_id)
        print('Skills_Required:', Skills_Required)
        print('Work_Schedule:', Work_Schedule)

        if picture:
            user = CustomUserModel(
                id=myid,
                picture=picture,
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                dob=CustomUserModel.objects.get(id=myid).dob,
                address=address,
                blood_group=blood_group,
                user_type=user_type,
                password = CustomUserModel.objects.get(id=myid).password,
            )
        else:
            user = CustomUserModel(
            id=myid,
            picture=CustomUserModel.objects.get(id=myid).picture,
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            dob=CustomUserModel.objects.get(id=myid).dob,
            address=address,
            blood_group=blood_group,
            user_type=user_type,
            password = CustomUserModel.objects.get(id=myid).password,
        )
        if request.user.user_type == "seeker":
            seeker = JobSeekerProfile.objects.get(id=seeker_id)
            seeker.skills=skills
            seeker.work_experience=work_experience
            seeker.save()
        else:
            recruiter = JobRecruiterProfile.objects.get(id=recruiter_id)
            recruiter.Skills_Required=Skills_Required
            recruiter.Work_Schedule=Work_Schedule
            recruiter.save()

        user.save()
        return redirect('profile')

def postedjob(request):
    current_user=request.user
    posted_job=JobModel.objects.filter(Created_by=current_user)
    postjobDict={
        'posted_job':posted_job
    }
    return render(request,'postedjob.html',postjobDict)