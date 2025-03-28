from django.shortcuts import render,redirect
from recipeApp.models import CustomUserModel,RecipeModel,ChefProfileModel,ViewerProfileModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        city=request.POST.get('city')
        country=request.POST.get('country')
        user_type=request.POST.get('user_type')

        if password==cpassword:
            user=CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=password,
                gender=gender,
                age=age,
                city=city,
                country=country,
                user_type=user_type,
            )
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'signin.html')

def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def profile(request):
    current_user=request.user
    if current_user.user_type=='chef':
        pro_info=ChefProfileModel.objects.get(myuser=current_user)
    else:
        pro_info=ViewerProfileModel.objects.get(myuser=current_user)
    proDict={
        'pro_info':pro_info
    }
    return render(request,'profile.html',proDict)

@login_required
def dashboard(request):
    current_user=request.user
    if current_user.user_type=='chef':
        recipe=RecipeModel.objects.filter(created_by=current_user)
    else:
        recipe=RecipeModel.objects.all()
    recipeDict={
        'recipe':recipe
    }
    return render(request,'dashboard.html',recipeDict)

@login_required
def addrecipe(request):
    if request.method=="POST":
        recipe_title=request.POST.get('recipe_title')
        ingredients=request.POST.get('ingredients')
        Instructions=request.POST.get('Instructions')
        preparation_time=request.POST.get('preparation_time')
        cooking_time=request.POST.get('cooking_time')
        total_time=request.POST.get('total_time')
        difficulty_level=request.POST.get('difficulty_level')
        nutritional_info=request.POST.get('nutritional_info')
        recipe_image=request.FILES.get('recipe_image')
        recipe_category=request.POST.get('recipe_category')
        user_tags=request.POST.get('user_tags')
        total_calorie=request.POST.get('total_calorie')

        recipe=RecipeModel(
            recipe_title=recipe_title,
            ingredients=ingredients,
            Instructions=Instructions,
            preparation_time=preparation_time,
            cooking_time=cooking_time,
            total_time=total_time,
            difficulty_level=difficulty_level,
            nutritional_info=nutritional_info,
            recipe_image=recipe_image,
            recipe_category=recipe_category,
            user_tags=user_tags,
            total_calorie=total_calorie,
            created_by=request.user,
        )
        recipe.save()
        return redirect('dashboard')
    return render(request,'chef/addrecipe.html')
@login_required
def deleterecipe(request,myid):
    recipe=RecipeModel.objects.get(id=myid)
    recipe.delete()
    return redirect('dashboard')
@login_required
def viewallrecipe(request):
    current_user=request.user
    if current_user.user_type=='chef':
        recipes=RecipeModel.objects.filter(created_by=current_user)
    else:
        recipes=RecipeModel.objects.all()
    recipeDict={
        'recipes':recipes
    }
    return render(request,'viewallrecipe.html',recipeDict)
@login_required
def singlerecipeview(request,myid):
    recipes=RecipeModel.objects.get(id=myid)
    recipeDict={
        'recipe':recipes
    }
    return render(request,'singlerecipeview.html',recipeDict)
@login_required
def editrecipe(request,myid):
    recipes=RecipeModel.objects.get(id=myid)
    recipeDict={
        'recipe':recipes
    }
    return render(request,'chef/editrecipe.html',recipeDict)
@login_required
def udpaterecipe(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        recipe_title=request.POST.get('recipe_title')
        ingredients=request.POST.get('ingredients')
        Instructions=request.POST.get('Instructions')
        preparation_time=request.POST.get('preparation_time')
        cooking_time=request.POST.get('cooking_time')
        total_time=request.POST.get('total_time')
        difficulty_level=request.POST.get('difficulty_level')
        nutritional_info=request.POST.get('nutritional_info')
        recipe_image=request.FILES.get('recipe_image')
        recipe_category=request.POST.get('recipe_category')
        user_tags=request.POST.get('user_tags')
        total_calorie=request.POST.get('total_calorie')

        if recipe_image:
            recipe=RecipeModel(
                id=myid,
                recipe_title=recipe_title,
                ingredients=ingredients,
                Instructions=Instructions,
                preparation_time=preparation_time,
                cooking_time=cooking_time,
                total_time=total_time,
                difficulty_level=difficulty_level,
                nutritional_info=nutritional_info,
                recipe_image=recipe_image,
                recipe_category=recipe_category,
                user_tags=user_tags,
                total_calorie=total_calorie,
                created_by=request.user,
            )
        else:
            recipebyid=RecipeModel.objects.get(id=myid)
            recipe=RecipeModel(
                id=myid,
                recipe_title=recipe_title,
                ingredients=ingredients,
                Instructions=Instructions,
                preparation_time=preparation_time,
                cooking_time=cooking_time,
                total_time=total_time,
                difficulty_level=difficulty_level,
                nutritional_info=nutritional_info,
                recipe_image=recipebyid.recipe_image,
                recipe_category=recipe_category,
                user_tags=user_tags,
                total_calorie=total_calorie,
                created_by=request.user,
            )
        recipe.save()
    return redirect('dashboard')