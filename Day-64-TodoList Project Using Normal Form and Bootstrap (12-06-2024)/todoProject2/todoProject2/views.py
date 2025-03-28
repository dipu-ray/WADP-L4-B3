from django.shortcuts import render,redirect,get_object_or_404
from todoApp2.models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

all_messages={
    'signup_success':'Signup successful!',
    'signin_success':'Signin successful!',
}

def signup(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        city=request.POST.get('city')
        profile_pic=request.FILES.get('profile_pic')
        user_type=request.POST.get('user_type')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        
        if password==cpassword:
            user=CustomUserModel.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                city=city,
                profile_pic=profile_pic,
                user_type=user_type,
                password=password,
            )
            user.save()
            return redirect('signin')
    return render(request, 'common/signup.html')
            

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'common/signin.html')

@login_required
def dashboard(request):
    all_task=TaskModel.objects.all().count()
    completed_task=TaskModel.objects.filter(task_status='Completed')
    incompleted_task_task=TaskModel.objects.filter(task_status='on_going')
    incom=incompleted_task_task.count()
    com_count=completed_task.count()
    taskDict={
        'com_count':com_count,
        'all_task':all_task,
        'incom':incom,
    }
    return render(request,'common/dashboard.html',taskDict)

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def addcategory(request):
    return render(request,'user/addcategory.html')

@login_required
def categorylist(request):
    cat=CategoryModel.objects.all()
    return render(request,'user/categorylist.html')

@login_required
def categorydel(request,catid):
    cat=get_object_or_404(CategoryModel,id=catid)
    cat.delete()
    return redirect('categorylist')


@login_required
def editcategory(request,catid):
    return render(request,'user/editcategory.html')

@login_required
def addtask(request):
    return render(request,'user/addtask.html')

@login_required
def tasklist(request):
    task=TaskModel.objects.all()
    return render(request,'user/tasklist.html')

@login_required
def taskdel(request,taskid):
    task=get_object_or_404(TaskModel,id=taskid)
    task.delete()
    return redirect('tasklist')

@login_required
def edittask(request,taskid):
    return render(request,'user/edittask.html')

@login_required
def markascompleted(request,taskid):
    task=TaskModel.objects.get(id=taskid)
    task.task_status="Completed"
    task.save()
    return redirect('tasklist')



