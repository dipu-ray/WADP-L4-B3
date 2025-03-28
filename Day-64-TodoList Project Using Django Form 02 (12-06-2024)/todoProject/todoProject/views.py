from django.shortcuts import render,redirect,get_object_or_404
from todoApp.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

all_messages={
    'signup_success':'Signup successful!',
    'signin_success':'Signin successful!',
}

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, all_messages['signup_success'])
            return redirect('signin')
    else:
        form = CustomUserCreationForm()

    return render(request, 'common/signup.html', {'form': form})
            

def signin(request):
    if request.method=="POST":
        form=CustomUserAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request,all_messages['signin_success'])
            return redirect('dashboard')
    else:
        form=CustomUserAuthenticationForm()
    return render(request,'common/signin.html',{'form':form})

@login_required
def dashboard(request):
    all_task=TaskModel.objects.filter(created_by=request.user)
    all_task_count=TaskModel.objects.filter(created_by=request.user).count()
    completed_task=TaskModel.objects.filter(created_by=request.user,task_status='Completed')
    com_count=completed_task.count()
    incompleted_task=TaskModel.objects.filter(created_by=request.user,task_status='On Going')
    incom_count=incompleted_task.count()
    cat=CategoryModel.objects.filter(user=request.user)
    total_cat=cat.count()
    taskDict={
        'all_task':all_task,
        'all_task_count':all_task_count,
        'completed_task':completed_task,
        'com_count':com_count,
        'incompleted_task':incompleted_task,
        'incom_count':incom_count,
        'total_cat':total_cat,
    }
    return render(request,'common/dashboard.html',taskDict)

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def addcategory(request):
    if request.method=="POST":
        current_user=request.user
        form=CustomCategoryForm(request.POST)
        if form.is_valid():
            category=form.save(commit=False)
            category.user=current_user
            category.save()
            return redirect('categorylist')
    else:
        form=CustomCategoryForm()
    return render(request,'user/addcategory.html',{'form':form})

@login_required
def categorylist(request):
    cat=CategoryModel.objects.filter(user=request.user)
    return render(request,'user/categorylist.html',{'cat':cat})

@login_required
def categorydel(request,catid):
    cat=get_object_or_404(CategoryModel,id=catid)
    cat.delete()
    return redirect('categorylist')


@login_required
def editcategory(request,catid):
    cat=get_object_or_404(CategoryModel,id=catid)
    if request.method=="POST":
        form=CustomCategoryForm(request.POST,instance=cat)
        if form.is_valid():
            form.save()
            return redirect('categorylist')
    else:
        form=CustomCategoryForm(instance=cat)
    return render(request,'user/editcategory.html',{'form':form,'cat':cat})

@login_required
def addtask(request):
    current_user=request.user
    if request.method == "POST":
        form=CustomTaskForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.created_by=current_user
            user.save()
            return redirect('tasklist')
    else:
        form=CustomTaskForm()
    return render(request,'user/addtask.html',{'form':form})

@login_required
def tasklist(request):
    task=TaskModel.objects.filter(created_by=request.user)
    return render(request,'user/tasklist.html',{'task':task})

@login_required
def taskdel(request,taskid):
    task=get_object_or_404(TaskModel,id=taskid)
    task.delete()
    return redirect('tasklist')

@login_required
def edittask(request,taskid):
    task=get_object_or_404(TaskModel,id=taskid)
    if request.method=="POST":
        form=CustomTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasklist')
    else:
        form=CustomTaskForm(instance=task)
    return render(request,'user/edittask.html',{'form':form,'task':task})

@login_required
def markascompleted(request,taskid):
    task=TaskModel.objects.get(id=taskid)
    task.task_status="Completed"
    task.save()
    return redirect('tasklist')

@login_required
def markasincompleted(request,taskid):
    task=TaskModel.objects.get(id=taskid)
    task.task_status="On Going"
    task.save()
    return redirect('tasklist')

@login_required
def alluser(request):
    users=CustomUserModel.objects.filter(user_type='user')
    
    total_task=0
    total_cat=0
    for i in users:
        total_task=TaskModel.objects.filter(created_by=i).count()
        total_cat=CategoryModel.objects.filter(user=i).count()
        
    userDict={
        'users':users,
        'total_task':total_task,
        'total_cat':total_cat,
    }
    return render(request,'admin/alluser.html',userDict)

def deleteuser(request,userid):
    user=CustomUserModel.objects.get(id=userid)
    user.delete()
    return redirect('alluser')




