from django.shortcuts import render, redirect
from JobApp.models import CustomUserModel,JobModel,RecruiterProfileModel,SeekerProfileModel,RecruiterBasicInfoModel,RecruiterContactModel,SeekerBasicInfoModel,SeekerContactModel,SeekerEducationModel,SeekerWorkExModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
import re

all_messages={
    'account_success':'Account create successful!',
    'password_warning':'Password and Confirm password not match',
    'password_warning2':'Password not match with Database',
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
    'signin_success':'Sign In Successful',
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
        user = authenticate(
            username=username,
            password=password,
        )
        # Check username exist or not
        existing_user = CustomUserModel.objects.filter(username=username).exists()
        if not existing_user:
            messages.warning(request,all_messages['user_not_found_warning'])
        
        elif user:
            login(request,user)
            messages.success(request, all_messages['signin_success'])
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

def updateprofile(request):
    current_user = request.user
    if request.method=="POST":
        profile_photo = request.FILES.get('profile_photo')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        country = request.POST.get('country')
        blood_group = request.POST.get('blood_group')
        user_types = request.POST.get('user_types')
        s_qualification = request.POST.get('s_qualification')
        s_experience = request.POST.get('s_experience')
        s_skills = request.POST.get('s_skills')
        s_last_education = request.POST.get('s_last_education')
        s_father_name = request.POST.get('s_father_name')
        s_mother_name = request.POST.get('s_mother_name')
        s_hobby = request.POST.get('s_hobby')
        s_languages = request.POST.get('s_languages')
        s_mobile_number = request.POST.get('s_mobile_number')
        s_email = request.POST.get('s_email')
        s_address = request.POST.get('s_address')
        s_education_name = request.POST.get('s_education_name')
        s_education_year = request.POST.get('s_education_year')
        s_education_institute = request.POST.get('s_education_institute')
        s_Position = request.POST.get('s_Position')
        s_Company_name = request.POST.get('s_Company_name')
        s_Duration = request.POST.get('s_Duration')
        r_company_name = request.POST.get('r_company_name')
        r_company_location = request.POST.get('r_company_location')
        r_recruiter_name = request.POST.get('r_recruiter_name')
        r_father_name = request.POST.get('r_father_name')
        r_mother_name = request.POST.get('r_mother_name')
        r_hobby = request.POST.get('r_hobby')
        r_languages = request.POST.get('r_languages')
        r_mobile_number = request.POST.get('r_mobile_number')
        r_email = request.POST.get('r_email')
        r_address = request.POST.get('r_address')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password==cpassword:
            if check_password(password,current_user.password):
                if not profile_photo:
                    current_user.profile_photo = CustomUserModel.objects.get(username=current_user).profile_photo
                    current_user.first_name = first_name
                    current_user.last_name = last_name
                    current_user.age = age
                    current_user.gender = gender
                    current_user.city = city
                    current_user.country = country
                    current_user.blood_group = blood_group
                    current_user.save()
                else:
                    current_user.profile_photo = profile_photo
                    current_user.first_name = first_name
                    current_user.last_name = last_name
                    current_user.age = age
                    current_user.gender = gender
                    current_user.city = city
                    current_user.country = country
                    current_user.blood_group = blood_group
                    current_user.save()

                if current_user.user_types == 'seeker':
                    current_user.seekerprofilemodel.Qualification=s_qualification
                    current_user.seekerprofilemodel.Experience=s_experience
                    current_user.seekerprofilemodel.Skills=s_skills
                    current_user.seekerprofilemodel.last_education=s_last_education
                    current_user.seekerprofilemodel.save()
                    current_user.seekerbasicinfomodel.father_name=s_father_name
                    current_user.seekerbasicinfomodel.mother_name=s_mother_name
                    current_user.seekerbasicinfomodel.hobby=s_hobby
                    current_user.seekerbasicinfomodel.languages=s_languages
                    current_user.seekerbasicinfomodel.save()
                    current_user.seekercontactmodel.languages=s_mobile_number
                    current_user.seekercontactmodel.email=s_email
                    current_user.seekercontactmodel.address=s_address
                    current_user.seekercontactmodel.save()
                    current_user.seekereducationmodel.education_name=s_education_name
                    current_user.seekereducationmodel.education_year=s_education_year
                    current_user.seekereducationmodel.education_institute=s_education_institute
                    current_user.seekereducationmodel.save()
                    current_user.seekerworkexmodel.Position=s_Position
                    current_user.seekerworkexmodel.Company_name=s_Company_name
                    current_user.seekerworkexmodel.Duration=s_Duration
                    current_user.seekerworkexmodel.save()

                elif current_user.user_types == 'recruiter':
                    current_user.recruiterprofilemodel.Company_name=r_company_name
                    current_user.recruiterprofilemodel.Company_location=r_company_location
                    current_user.recruiterprofilemodel.Recruiter_Name=r_recruiter_name
                    current_user.recruiterprofilemodel.save()
                    current_user.recruiterbasicinfomodel.father_name=r_father_name
                    current_user.recruiterbasicinfomodel.mother_name=r_mother_name
                    current_user.recruiterbasicinfomodel.hobby=r_hobby
                    current_user.recruiterbasicinfomodel.languages=r_languages
                    current_user.recruiterbasicinfomodel.save()
                    current_user.recruitercontactmodel.mobile_number=r_mobile_number
                    current_user.recruitercontactmodel.email=r_email
                    current_user.recruitercontactmodel.address=r_address
                    current_user.recruitercontactmodel.save()
            else:
                messages.warning(request,all_messages['password_warning2'])
                return redirect('editprofile')
        
        else:
            messages.warning(request,all_messages['password_warning'])
            return redirect('editprofile')

    return redirect('profile')

@login_required
def changepassword(request):
    if request.method == "POST":
        cu_password = request.POST.get('cu_password')
        n_password = request.POST.get('n_password')
        cn_password = request.POST.get('cn_password')

        if check_password(cu_password,request.user.password):
            if n_password == cn_password:
                request.user.set_password(n_password)
                request.user.save()
                update_session_auth_hash(request,request.user)
                return redirect('profile')
            else:
                messages.warning(request,all_messages['password_warning'])
        else:
            messages.warning(request,all_messages['password_warning2'])

    return render(request,'changepassword.html')

