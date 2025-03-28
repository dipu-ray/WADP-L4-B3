from django.shortcuts import render,redirect
from jobApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash


def signup(request):
    if request.method=="POST":
        display_name=request.POST.get('display_name')
        profile_picture=request.FILES.get('profile_picture')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_type=request.POST.get('user_type')
        
        if password==confirm_password:
            user = CustomUserModel.objects.create_user(
                display_name=display_name,
                profile_picture=profile_picture,
                username=username,
                password=password,
                user_type=user_type
            )
            user.save()
            if user_type == 'recruiter':
                RecruiterModel.objects.create(
                    recruiteruser=user
                )
            else:
                SeekerModel.objects.create(
                    seekeruser=user
                )
            return redirect('signin')
    return render(request,'common/signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'common/signin.html')

@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def addjob(request):
    if request.method=='POST':
        Title=request.POST.get('Title')
        Number_openings=request.POST.get('Number_openings')
        Category=request.POST.get('Category')
        Job_description=request.POST.get('Job_description')
        Skills=request.POST.get('Skills')

        job=JobModel.objects.create(
            Title=Title,
            Number_openings=Number_openings,
            Category=Category,
            Job_description=Job_description,
            Skills=Skills,
            created_by=request.user
        )
        job.save()
        return redirect('joblist')
    return render(request,'recruiter/addjob.html')

@login_required
def joblist(request):
    jobs = JobModel.objects.all()
    return render(request,'common/joblist.html',{'jobs':jobs})

@login_required
def deletejob(request,jobid):
    job=JobModel.objects.get(id=jobid)
    job.delete()
    return redirect('joblist')

@login_required
def editjob(request,jobid):
    job=JobModel.objects.get(id=jobid)
    
    if request.method=='POST':
        Title=request.POST.get('Title')
        Number_openings=request.POST.get('Number_openings')
        Category=request.POST.get('Category')
        Job_description=request.POST.get('Job_description')
        Skills=request.POST.get('Skills')
        
        job=JobModel.objects.get(id=jobid)
        job.Title=Title
        job.Number_openings=Number_openings
        job.Category=Category
        job.Job_description=Job_description
        job.Skills=Skills
        job.save()
        return redirect('joblist')
    return render(request,'recruiter/editjob.html',{'job':job})

@login_required
def viewjob(request,jobid):
    job=JobModel.objects.get(id=jobid)
    return render(request,'common/viewjob.html',{'job':job})

@login_required
def applyjob(request,jobid):
    job=JobModel.objects.get(id=jobid)
    
    if request.method=='POST':
        skills=request.POST.get('skills')
        resume=request.FILES.get('resume')
        
        applyjob=JobApplymodel.objects.create(
            skills=skills,
            resume=resume,
            applicant=request.user,
            applied_job=job,
        )
        applyjob.save()
        return redirect('joblist')
    return render(request,'seeker/applyjob.html',{'job':job})

@login_required
def jobsearch(request):
    if request.method=='GET':
        search=request.GET.get('search')
        # jobs=JobModel.objects.filter(Title=search)
        jobs=JobModel.objects.filter(
            Q(Title__icontains=search)|
            Q(Category__icontains=search)|
            Q(Skills__icontains=search)|
            Q(created_by__username__icontains=search)
        )
    return render(request,'common/searchjob.html',{'jobs':jobs})

@login_required
def profile(request):
    return render(request,'profile/profile.html')

@login_required
def basicinfo(request):
    return render(request,'profile/basicinfo.html')

@login_required
def seekerinfo(request):
    return render(request,'profile/seekerinfo.html')

@login_required
def recruiterinfo(request):
    return render(request,'profile/recruiterinfo.html')

@login_required
def changepassword(request):
    if request.method=="POST":
        current_password=request.POST.get('current_password')
        new_password=request.POST.get('new_password')
        new_con_password=request.POST.get('new_con_password')

        pass_check=check_password(current_password,request.user.password)
        if pass_check:
            if new_password == new_con_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request,request.user)
                return redirect('dashboard')
    return render(request,'common/changepassword.html')

@login_required
def editbasicinfo(request):
    if request.method=='POST':
        display_name=request.POST.get('display_name')
        profile_picture=request.FILES.get('profile_picture')
        
        user_cus=CustomUserModel.objects.get(username=request.user)
        user_cus.display_name=display_name
        user_cus.profile_picture=profile_picture
        user_cus.save()
        return redirect('basicinfo')
    return render(request,'profile/editbasicinfo.html')

@login_required
def editseekerprofile(request):
    if request.method =="POST":
        Skills=request.POST.get('Skills')
        Resume=request.FILES.get('Resume')
        
        seeker = SeekerModel.objects.get(seekeruser=request.user)
        seeker.Skills=Skills
        seeker.Resume=Resume
        seeker.save()
        return redirect('seekerinfo')
    return render(request,'profile/editseekerprofile.html')

@login_required
def editrecruiterprofile(request):
    if request.method =="POST":
        company_name=request.POST.get('company_name')
        company_address=request.POST.get('company_address')
        
        recruiter = RecruiterModel.objects.get(recruiteruser=request.user)
        recruiter.company_name=company_name
        recruiter.company_address=company_address
        recruiter.save()
        return redirect('recruiterinfo')
    return render(request,'profile/editrecruiterprofile.html')










