from django.shortcuts import render,redirect
from jobportalApp.models import CustomUserModel,JobModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        picture=request.FILES.get('picture')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        blood_group=request.POST.get('blood_group')
        user_type=request.POST.get('user_type')
        
        if password==cpassword:
            
            user = CustomUserModel.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=uname,
                email=email,
                password=password,
                picture=picture,
                dob=dob,
                address=address,
                blood_group=blood_group,
                user_type=user_type,
            )
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
        
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        
        user=authenticate(
            username=uname,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')
    return render(request,'signin.html')

def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def dashboard(request):
    current_user=request.user
    if current_user.user_type == 'recruiter':
        jobs=JobModel.objects.filter(Created_by=request.user)
    else:
        jobs=JobModel.objects.all()
    jobDict={
        'jobs':jobs
    }
    return render(request,'dashboard.html',jobDict)

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
def viewjob(request):
    current_user=request.user
    if current_user.user_type == 'recruiter':
        jobs=JobModel.objects.filter(Created_by=request.user)
    else:
        jobs=JobModel.objects.all()
    jobDict={
        'jobs':jobs
    }
    return render(request,'viewjob.html',jobDict)

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
    job=JobModel.objects.get(id=myid)
    jodDict={
        'job':job
    }
    return render(request,'viewsinglejob.html',jodDict)

@login_required
def profile(request):
    return render(request,'profile.html')





