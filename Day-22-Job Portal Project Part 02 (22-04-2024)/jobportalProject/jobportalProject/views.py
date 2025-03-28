from django.shortcuts import render,redirect
from jobportalApp.models import CustomUserModel

def signup(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        profile_picture=request.FILES.get('profile_picture')
        date_of_birth=request.POST.get('date_of_birth')
        blood_group=request.POST.get('blood_group')
        address=request.POST.get('address')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        usertype=request.POST.get('usertype')

        if password==confirm_password:
            user=CustomUserModel.objects.create_user(
                username=username,
                password=confirm_password,
            )
            user.fname=fname
            user.lname=lname
            user.profile_picture=profile_picture
            user.date_of_birth=date_of_birth
            user.blood_group=blood_group
            user.address=address
            user.email=email
            user.usertype=usertype
            user.save()
            return redirect('signin')

        else:
            return redirect('signup')

    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')

