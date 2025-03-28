from django.shortcuts import render, redirect
from JobApp.models import CustomUserModel,JobModel,RecruiterProfileModel,SeekerProfileModel,RecruiterBasicInfoModel,RecruiterContactModel,SeekerBasicInfoModel,SeekerContactModel,SeekerEducationModel,SeekerWorkExModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

all_messages={
    'account_success':'Account create successful!',
    'password_warning':'Password not match',
    'credential_warning':'Account credential not match',
    'age_warning':'age is not valid',
    'first_name_warning':'First Name should only contain letters.',
    'last_name_warning':'Last Name should only contain letters.',
    'username_warning':'Username Already exists',
    'age_warning':'Please put your age in number; e.g: 19',
    'age_warning2':'Your age must be between 18 and 150.',
    'city_name_warning':'City Name not valid',
    'country_name_warning':'Country Name not valid',
    'user_not_found_warning':'Cant find the username',
}

def signup(request):
    if request.method=="POST":
        profile_photo = request.FILES.get('profile_photo')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        country = request.POST.get('country')
        blood_group = request.POST.get('blood_group')
        user_types = request.POST.get('user_types')
            
        # Preserve form data in the template
        context = {
            'first_name' : first_name,
            'last_name' : last_name,
            'username' : username,
            'password' : password,
            'cpassword' : cpassword,
            'age' : age,
            'gender' : gender,
            'city' : city,
            'country' : country,
            'blood_group' : blood_group,
            'user_types' : user_types,
        }
        # first name check
        if not re.match(r'^[a-zA-Z\s]+$', first_name):
            messages.warning(request, all_messages['first_name_warning'])
            return render(request,'signup.html',context)
        
        # last name check
        if not re.match(r'^[a-zA-Z\s]+$', last_name):
            messages.warning(request, all_messages['last_name_warning'])  
            return render(request,'signup.html',context)
        
        # Existing user check
        existing_user = CustomUserModel.objects.filter(username=username).exists()
        print(existing_user)
        if existing_user:
            messages.warning(request, all_messages['username_warning'])  
            return render(request,'signup.html',context)
        
        # age check
        if not age.isdigit():
            messages.warning(request, all_messages['age_warning'])  
            return render(request,'signup.html',context)
        
        if not (18<int(age)<150):
                messages.warning(request, all_messages['age_warning2'])  
                return render(request,'signup.html',context)
        
        # City name check
        if not re.match(r'^[a-zA-Z\s]+$', city):
            messages.warning(request, all_messages['city_name_warning'])  
            return render(request,'signup.html',context)
        
        # Country name check
        if not re.match(r'^[a-zA-Z\s]+$', country):
            messages.warning(request, all_messages['country_name_warning'])  
            return render(request,'signup.html',context)

        if password==cpassword:
            user = CustomUserModel.objects.create_user(
                profile_photo=profile_photo,
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                age=age,
                gender=gender,
                city=city,
                country=country,
                blood_group=blood_group,
                user_types=user_types,
            )
            if user_types == 'recruiter':
                RecruiterProfileModel.objects.create(user = user)
                RecruiterBasicInfoModel.objects.create(user = user)
                RecruiterContactModel.objects.create(user = user)
            elif user_types == 'seeker':
                SeekerProfileModel.objects.create(user = user)
                SeekerBasicInfoModel.objects.create(user = user)
                SeekerContactModel.objects.create(user = user)
                SeekerEducationModel.objects.create(user = user)
                SeekerWorkExModel.objects.create(user = user)
            user.save()
            messages.success(request, all_messages['account_success'])
            return redirect('signin')
        else:
            messages.warning(request, all_messages['password_warning'])
            return render(request,'signup.html',context)

    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        # Preserve form data in the template
        context={
            'username':username,
            'password':password,
        }
        # Check username exist or not
        existing_user = CustomUserModel.objects.filter(username=username).exists()
        if not existing_user:
            messages.warning(request,all_messages['user_not_found_warning'])
        
        user = authenticate(
            username=username,
            password=password,
            )
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request, all_messages['credential_warning'])
            return render(request,'signin.html',context)
    

    return render(request,'signin.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def addjob(request):
    if request.method=="POST":
        Company_logo=request.FILES.get('Company_logo')
        Job_title=request.POST.get('Job_title')
        Job_description=request.POST.get('Job_description')
        Job_location=request.POST.get('Job_location')
        Requirements=request.POST.get('Requirements')
        Qualifications=request.POST.get('Qualifications')
        Job_types=request.POST.get('Job_types')
        Workplace=request.POST.get('Workplace')
        Salary=request.POST.get('Salary')
        Experience=request.POST.get('Experience')
        Deadline=request.POST.get('Deadline')

        job = JobModel(
            Company_logo=Company_logo,
            Job_title=Job_title,
            Job_description=Job_description,
            Job_location=Job_location,
            Requirements=Requirements,
            Qualifications=Qualifications,
            Job_types=Job_types,
            Workplace=Workplace,
            Salary=Salary,
            Experience=Experience,
            Deadline=Deadline,
            Created_by=request.user,
        )
        job.save()
        return redirect('dashboard')
    return render(request,'addjob.html')

@login_required
def dashboard(request):
    current_user = request.user
    if current_user.user_types == 'recruiter':
        jobs=JobModel.objects.filter(Created_by=current_user)
    else:
        jobs=JobModel.objects.all()
    
    jobDict={
        'jobs':jobs
    }
    return render(request,'dashboard.html',jobDict)

@login_required
def deletejob(request,myid):
    job=JobModel.objects.get(id=myid)
    job.delete()
    return redirect('dashboard')

@login_required
def viewsinglejob(request,myid):
    job=JobModel.objects.get(id=myid)
    jobDict={
        'job':job
    }
    return render(request,'viewsinglejob.html',jobDict)

@login_required
def appliedjob(request):
    return render(request,'appliedjob.html')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def editjob(request,myid):
    job=JobModel.objects.get(id=myid)
    jobDict={
        'job':job
    }
    return render(request,'editjob.html',jobDict)

def updatejob(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        Company_logo=request.FILES.get('Company_logo')
        Job_title=request.POST.get('Job_title')
        Job_description=request.POST.get('Job_description')
        Job_location=request.POST.get('Job_location')
        Requirements=request.POST.get('Requirements')
        Qualifications=request.POST.get('Qualifications')
        Job_types=request.POST.get('Job_types')
        Workplace=request.POST.get('Workplace')
        Salary=request.POST.get('Salary')
        Experience=request.POST.get('Experience')
        Deadline=request.POST.get('Deadline')

        if Company_logo:
            job = JobModel(
                id=myid,
                Company_logo=Company_logo,
                Job_title=Job_title,
                Job_description=Job_description,
                Job_location=Job_location,
                Requirements=Requirements,
                Qualifications=Qualifications,
                Job_types=Job_types,
                Workplace=Workplace,
                Salary=Salary,
                Experience=Experience,
                Deadline=Deadline,
                Created_by=request.user,
            )
        else:
            job = JobModel(
                id=myid,
                Company_logo=JobModel.objects.get(id=myid).Company_logo,
                Job_title=Job_title,
                Job_description=Job_description,
                Job_location=Job_location,
                Requirements=Requirements,
                Qualifications=Qualifications,
                Job_types=Job_types,
                Workplace=Workplace,
                Salary=Salary,
                Experience=Experience,
                Deadline=Deadline,
                Created_by=request.user,
            )
        job.save()
    return redirect('dashboard')

def postedjob(request):
    current_user = request.user
    jobs=JobModel.objects.filter(Created_by=current_user)
    jobDict={
        'jobs':jobs
    }
    return render(request,'postedjob.html',jobDict)

def editprofile(request):
    return render(request,'editprofile.html')

# after profile template mastering

def profiles_info(request):
    return render(request,'profiles_info.html')


def recruiterbasicinfo(request):
    current_user=request.user
    recruiter = RecruiterBasicInfoModel.objects.filter(user=current_user)
    recruiterDict={
        'recruiter':recruiter
    }
    return render(request,'recruiter/recruiterbasicinfo.html',recruiterDict)

def recruitercontact(request):
    current_user=request.user
    recruiter = RecruiterContactModel.objects.filter(user=current_user)
    recruiterDict={
        'recruiter':recruiter
    }
    return render(request,'recruiter/recruitercontact.html',recruiterDict)

def seekerbasicinfo(request):
    current_user=request.user
    seeker = SeekerBasicInfoModel.objects.filter(user=current_user)
    seekerDict={
        'seeker':seeker
    }
    return render(request,'seeker/seekerbasicinfo.html',seekerDict)

def seekercontact(request):
    current_user=request.user
    seeker = SeekerContactModel.objects.filter(user=current_user)
    seekerDict={
        'seeker':seeker
    }
    return render(request,'seeker/seekercontact.html',seekerDict)

def seekereducation(request):
    current_user=request.user
    seeker = SeekerEducationModel.objects.filter(user=current_user)
    seekerDict={
        'seeker':seeker
    }
    return render(request,'seeker/seekereducation.html',seekerDict)

def seekerworkex(request):
    current_user=request.user
    seeker = SeekerWorkExModel.objects.filter(user=current_user)
    seekerDict={
        'seeker':seeker
    }
    return render(request,'seeker/seekerworkex.html',seekerDict)

