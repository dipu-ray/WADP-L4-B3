<div align="center">
<h1>Web Application Development with Python Level 04 Batch 03</h1>
</div>

</br>

<details>
<summary>Day-01-Environment & Django Setup (13-03-2024)</summary>
    
## Day 01 Topics:

- Python Install
- Environment Setup
- Install Necessary Packages
- Creating First Project

### Python Install:

[Download](https://www.python.org/downloads/windows/) and install: 

`python 3.11.8`

> Make sure `add to path` is tick while installing or manually need to be added.

### Environment Setup:

Creation

```bash
python -m venv env
```

Activation

```bash
.\env\Scripts\activate
```

Deactivation

```bash
deactivate
```

### Install Necessary Packages:

Installing Django:

```bash
pip install Django
```

### Creating First Project:

Creating first_project:

```bash
django-admin startproject first_project
```

first_project Directory:

```bash
cd first_project
```

Run The Project:

```bash
python manage.py runserver
```
</details>


<details>
<summary>Day-02-Env Setup, Database, Super user & Views (14-03-2024)</summary>
    
## Day 02 Topics:

- Difference between languages
- Different scope of python
- Day 01 recap
- Default database
- Database migrations
- Super user
- Quick Recap
- Coding Editor Setup
- Creating views.py
- Special notes
- Day 02 Recap
- Task

### Difference between languages

- Time of execution
- Low level , High Level

### Different scope of python:

- Machine Learning
- Deep Learning
- Web Development

### Day 01 recap
- Setup environment
- Install django
- Create and run project

### Default database:
- db.sqlite3

### Database migrations

Always perform makemigrations first to initialize the schema (overal database structures initialization)

```bash
py manage.py makemigrations
```

Now do this:
```bash
py manage.py migrate
```
- Download [DB Browser for SQLite](https://sqlitebrowser.org/dl/) and install to see the `db.sqlite3` table or in VSCode install [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) extension

### Super user:
To create superuser:
```bash
py manage.py createsuperuser
```
This will prompt to enter `Username`,`Email address`,`Password`

### Quick Recap:
- Create environment 
- Activate environtment
- Install django
- Run `django-admin startproject <project_name>`
- Go to project directory by `cd project_name`
- Run `py manage.py runserver` 
- Database migration:
  - `py manage.py makemigrations`
  - `py manage.py migrate`
- For creating superuser :
  - `py manage.py createsuperuser`

### Coding Editor Setup
- Download [VSCode](https://code.visualstudio.com/download) and install
- To open in VSCode run in cmd: `code .`

### Creating views.py:
In project folder create `views.py` and write:
```python
from django.shortcuts import render,redirect,HttpResponse

```
- `render` To show `html`
- `redirect` to redirect Website url 
- `HttpResponse` to show any text or changes on website

Creating a function to show a simple text:
```python
from django.shortcuts import render,redirect,HttpResponse

def homePage():
    return HttpResponse("Hi how are you")
```
A parameter need to be set `request`
```python
from django.shortcuts import render,redirect,HttpResponse

def homePage(request):
    return HttpResponse("Hi how are you")
```
Now in `urls.py` we have to add path of `homePage`
```python
from django.contrib import admin
from django.urls import path
from first_project2.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage',homePage,name='homePage'),
]
```
here `homePage` function is imported by `from first_project2.views import homePage` and `path('homePage',homePage,name='homePage')` is added in `urlpatterns`.
Similarly more pages can be added

### Special notes
- Variable name can't be same as function,keywords
- While importing writing `*` will import all e.g: `from first_project2.views import *`

### Day 02 Recap
- Create environment 
- Activate environtment
- Install django
- Run `django-admin startproject <project_name>`
- Go to project directory by `cd project_name`
- Run `py manage.py runserver` 
- Migrate Database
- Create Superuser
- Create `views.py` in project directory
- Import neccesary library or modules
- Create function of 5 pages
- Import those fuction in `urls.py` and add 5 pages path in `urlpatterns`
- View those pages in browser

### Task
  - Learn all predefined variables in `settings.py`
  - Learn all predefined variables in `urls.py`
  - Write notes on [commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands) (e.g: `dir`,`cd` etc)
  - Submit a video of today's class

</details>

<details>
<summary>Day-02-Extra & Assignment Notes</summary>

## Day-02-Extra Topics:

- Windows Commands
- Exploring settings.py & urls.py

### Windows Commands

1. `mkdir (Make Directory)`: This command is used to create a new directory or folder.
Example: `mkdir MyFolder`
2. `cd (Change Directory)`: This command is used to change the current directory.
Example: `cd MyFolder`, `cd ..`
3. `dir (Directory Listing)`: This command is used to list the contents of a directory.
Example: `dir`.
Also by passing `/b` parameter output will be simple: `dir /b`
4. `echo`: This command is used to display a line of text/string on the console.
Example: `echo Hello, Tansen!`.
Text can be saved in file also like this: `echo Hello, Tansen! >> textfile.txt`
5. `copy`: This command is used to copy one or more files from one location to another.
Example: `copy file1.txt Destination_Path`
6. `xcopy`: This command is used to copy files and directories, including subdirectories.
Example: `xcopy source_folder destination_folder`
7. `move`: This command is used to move files from one location to another.
Example: `move file1.txt Destination_Path`
8. `ren (Rename)`: This command is used to rename a file or directory.
Example: `ren oldfilename.txt newfilename.txt`
9. `del (Delete)`: This command is used to delete one or more files.
Example: `del file1.txt`
10. `rmdir (Remove Directory)`:This command is used to delete a directory.
Example: `rmdir MyFolder`
11. `type`:This command is used to display the contents of a text file.
Example: `type file.txt`
12. `tree`: This command is used to display the folder structure of a directory and its subdirectories as a tree diagram.
Example: `tree`
13. `find`: This command is used to search for a specific text string in files.
Example: `find "search_term" file.txt`
14. `fc (File Compare)`: This command is used to compare the contents of two files or sets of files.
Example: `fc file1.txt file2.txt`
15. `attrib (Attribute)`: This command is used to display or change file attributes (such as hidden, read-only).
Example: `attrib +h file.txt` Here changing this command with `-h` will do the revert: `attrib -h file.txt`

### Exploring settings.py & urls.py

1. **BASE_DIR**: This variable represents the base directory of Django project.

2. **SECRET_KEY**: This is a secret key used by Django for cryptographic signing and protect user session data.

3. **DEBUG**: This is a boolean that determines whether project is in debug mode or not.Debug mode provides more detailed error pages and enables other debugging tools.

4. **ALLOWED_HOSTS**: This is a list of strings representing the host/domain names that Django site can serve. It's a security measure to prevent HTTP Host header attacks.

5. **INSTALLED_APPS**: This is a list of strings representing the names of all Django applications that are activated in the Django instance.

6. **MIDDLEWARE**: Middleware are hooks into Django's request/response processing. They're executed in the order listed, and they can modify request/response objects, handle exceptions, and perform other operations.

7. **ROOT_URLCONF**: This is the Python path to project's root URL configuration. It's the module that contains URL patterns.

8. **TEMPLATES**: This is a list of dictionaries representing the configuration of Django's template engine. It specifies template directories, template loaders, and context processors.

9. **WSGI_APPLICATION**: This is the Python path to the WSGI application object that Django's built-in server use.

10. **DATABASES**: This is a dictionary containing the configuration of all database connections used by Django project. Default database engine SQLite is used.

11. **AUTH_PASSWORD_VALIDATORS**: This is a list of validators that are used to validate user passwords. These validators enforce various password policies like minimum length, common password checks, etc.

12. **LANGUAGE_CODE**: This is the language code that is used in certain parts of Django's infrastructure.

13. **TIME_ZONE**: This is the time zone used to represent datetimes in the correct time zone.

14. **USE_I18N** and **USE_TZ**: These are boolean flags that control internationalization and time zone support in Django.

15. **STATIC_URL**: This is the URL prefix for static files (CSS, JavaScript, images, etc.) served by Django's static file server.

16. **DEFAULT_AUTO_FIELD**: This is the default primary key field type to use for models that don't have a primary key field explicitly defined. In this case, it's set to use `BigAutoField`, which is a 64-bit integer primary key field that automatically increments.

17. **urlpatterns**: This is a list of URL patterns that Django uses to match incoming browser requests to views within Django application.

</details>

<details>
<summary>Day-03-Render Template, Dictionary DS , Template Language (16-03-2024)</summary>

## Day 03 Topics:

- Day 2 recap
- Render template
- Show table data dinamically using dictionary
- Notes on dictionary
- Now Recap

### Render template
Create a folders `static`, `Template` in project directory where `manage.py` is present.
Now in `settings.py` add `STATICFILES_DIRS`:
```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
```
Now in `TEMPLATES`'s `DIRS` list add these:
```python
'DIRS': [BASE_DIR, "Template"],
```
Now similarly in `views.py` file `return render(request,'homePage.html')` will be added as below:
```python
from django.shortcuts import render,redirect,HttpResponse

def homePage(request):
    return render(request,'homePage.html')
```
Now in `urls.py` this will be added:
```python
from first_project.views import homePage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',homePage,name='homePage'),
]
```
### Show table data dynamically using dictionary
In `views.py` file:
```python
from django.shortcuts import render,redirect,HttpResponse

def tableData(request):
    myDict={
        'name':'Tansen',
        'department':'CSE',
        'city':'Dhaka',
        'name2':'Shakil',
        'department2':'EEE',
        'city2':'Barisal',
    }

    return render(request,'tableData.html',myDict)
```
In `urls.py` file:
```python
from django.contrib import admin
from django.urls import path
from first_project.views import homePage,contactPage,orderPage,paymentPage,productPage,navBar,tableData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tableData',tableData,name='tableData'),

]
```
In `tableData.html` file:
```html
<table id="info">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
  </tr>
  <tr>
    <td>{{name}}</td>
    <td>{{department}}</td>
    <td>{{city}}</td>
  </tr>
  <tr>
    <td>{{name2}}</td>
    <td>{{department2}}</td>
    <td>{{city2}}</td>
  </tr>

</table>
```
### Notes on dictionary
- Dictionary is `key - value` pair

### Day 03 Recap:
- Day 02 recap
  - Create environment
  - Activate environment
  - Install necessary package (django)
  - Create a project
  - Run the project and view in browser
  - Now migrate database
  - View the database
  - Create super user
  - Now Create function of 5 pages in `views.py`
  - Import those fuction in `urls.py` and add 5 pages path in `urlpatterns`
  - View those pages in browser
- Render template (`HTML` files)
- Create a table and view it
- Get a table from external source [Fancy HTML CSS table](https://www.w3schools.com/css/tryit.asp?filename=trycss_table_fancy) and create 5 html pages
- Dynamically change table data from backend using dictionary data structure & template laguage
</details>

<details>
<summary>Day-04-Template Mastering, Navigation, url,include,block,extends (18-03-2024)</summary>

## Day 04 Topics:

- Day 3 recap
- Template mastering
- Organize reuse code
- Day 04 Recap

### Template mastering
- clicking on navbar any section change other element of the page
- In template mastering we reuse same element again and again. e.g: navbar

Create a navbar (get it from [external source](https://www.w3schools.com/css/tryit.asp?filename=trycss_navbar_horizontal_black_right))

Now in created `home.html`:
```html
<ul>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li style="float:right"><a class="active" href="#about">About</a></li>
</ul>
```

Now in `urls.py` file there is `path('home/', home,name='home')` where `name='home'` needs to be added in `href` like this: `href="{% url 'home' %}"`:
```html
<ul>
  <li><a href="{% url 'home' %}">Home</a></li>
  <li><a href="{% url 'news' %}">News</a></li>
  <li><a href="{% url 'contact' %}">Contact</a></li>
  <li style="float:right"><a class="active" href="{% url 'about' %}">About</a></li>
</ul>
```
### Organize reuse code

create a new `navbar.html` and add:
```html
<ul>
  <li><a href="{% url 'home' %}">Home</a></li>
  <li><a href="{% url 'news' %}">News</a></li>
  <li><a href="{% url 'contact' %}">Contact</a></li>
  <li style="float:right"><a class="active" href="{% url 'about' %}">About</a></li>
</ul>
```

now include it in `home.html`:
```html
</head>
<body>

{% include 'navbar.html' %}

</body>
</html>
```

Now to use it in every page , block content need to be added in `home.html`:
```html
<body>

{% include 'navbar.html' %}

{% block content %}
<h1>This is home page</h1>
{% endblock content %}
</body>
```
now let's add in `about.html`:
first `home.html` need to be extend then all content need to be in `block` content:
```html
{% extends 'home.html' %}
{% block content %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This about page</h1>
</body>
</html>
{% endblock content %}
``` 

### Day 04 Recap:
- Day 03 recap
- In Virtual environment Start Django Project with DB migrate & superuser
- Initialize Django static file
- Get a navbar from [external source](https://www.w3schools.com/css/tryit.asp?filename=trycss_navbar_horizontal_black_right)
- Create a `template` folder `manage.py` file location
- Create a `index.html` file  inside `template` folder and view the navbar
- Template mastering
  - Now create individual other 3 pages (news,contact,about)
  - Make those navbar navigation working (hypertext reference `href`)
  - Stick navbar on each page (Organize reused code)
    - url
    - Include
    - block
    - Extend

### Task
- Upload today's recap video 
- Django Models

</details>

<details>
<summary>Day-05-App,Models,Entity & Attribute (19-03-2024)</summary>
    
## Day 05 Topics:
- Day 4 recap
- Create Django app
- Install app
- Models
- Database note
- Configure admin
- Make created object table name more identical

### Create Django app
for creating django app:
```bash
py manage.py startapp myapp
```
This command will create myapp project with additional files
### Install app
inside settings.py there is `INSTALLED_APPS` where we have to add our `myapp`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```
### Models
Now in created `myapp` there is `models.py` file where we will create models (database data/table) :
```python
from django.db import models

# Create your models here.
class studentModel(models.Model):
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
```
### Database note
`Entity` - Table initial column names (e.g.: name,roll,department,city)

`Attribute` - values of entities (Tansen,05,CSE,Dhaka)

**Whenever we change anything in models we must perform:**
```bash
py manage.py makemigrations
```
```bash
py manage.py migrate
```
### Configure admin
Now in `admin.py` which is in `myapp` we need to import the created model and register it.
```python
from django.contrib import admin

from myapp.models import studentModel

# Register your models here.

admin.site.register(studentModel)
```
### Make created object table name more identical
In `models.py` file inside `myapp` we need to add `__str__` functions:
```python
from django.db import models

# Create your models here.
class studentModel(models.Model):
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    # this will make the table name more identical:
    def __str__(self):
        return f"{self.name}-{self.department}-{self.roll}"
```
### Quick Recap:
- App
- Model
- Site Register
- Create

### Day 05 Recap:
- Create Django project in virtual environment
- Initialize database (migrate)
- Create superuser (admin)
- Models
    - Create Django app
    - Install app (`in settings.py`)
    - Create some models
    - Configure admin (`site register`)
    - Migrate database (`Whenever changes in models`)
    - View and add data in created models

### Task
- Create 5 apps, 5 models, each model with 3 entity
- Submit video

</details>

<details>
<summary>Day-05-Extra & Assignment Notes</summary>

## Notes on creating 5 apps, 5 models & 3 entity for each

### blogapp

- BlogModel
    - blog_title
    - blog_date
    - blog_category

- NewsModel
    - news_headings
    - news_date
    - news_category

- CommentModel
    - comment_text
    - comment_date
    - commenter_name

- AuthorModel
    - author_name
    - author_bio
    - author_email

- TagModel
    - tag_name
    - tag_description
    - tagged_items


### kidsapp

- KidModel
    - kid_name
    - kid_age
    - kid_gender

- ToyModel
    - toy_name
    - toy_category
    - toy_price

- RatingModel
    - rating_value
    - rating_date
    - reviewer_name

- ManufacturerModel
    - manufacturer_name
    - manufacturer_location
    - manufacturer_contact
- LocationModel
    - location_name
    - location_description
    - location_address

### portfolioapp

- PortfolioModel
    - project_title
    - project_description
    - project_date

- ExperienceModel
    - company_name
    - job_title
    - employment_duration

- SkillModel
    - skill_name
    - skill_category
    - skill_proficiency

- EducationModel
    - institution_name
    - degree_obtained
    - graduation_year

- ProjectCategoryModel
    - category_name
    - category_description
    - categorized_projects


### ecommerceapp

- ProductModel
    - product_name
    - product_price
    - product_quantity

- OrderModel
    - order_number
    - order_date
    - customer_name


- ReviewModel
    - review_text
    - review_date
    - product_id

- SellerModel
    - seller_name
    - seller_email
    - seller_location

- PaymentModel
    - payment_method
    - payment_date
    - payment_amount


### aiapp

- aiModel
    - ai_name
    - ai_usages
    - ai_category

- TaskModel
    - task_name
    - task_deadline
    - task_priority

- DatasetModel
    - dataset_name
    - dataset_format
    - dataset_size

- ExperimentModel
    - experiment_name
    - experiment_date
    - experiment_results

- UserModel
    - user_name
    - user_email
    - user_role

</details>

<details>
<summary>Day-06-Reading Data from Database and Displaying it in Frontend (20-03-2024)</summary>

## Day 06 Topics:

- Day 5 recap
- Render html recap
- Navbar recap
- Read database data and show in frontend
- Common errors
- Task

### Read database data and show in frontend
Create a model in `models.py`:
```python
class BlogModel(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_author = models.CharField(max_length=100)
    blog_date = models.CharField(max_length=100)
    
    def __str__(self):
        return self.blog_title
```
Now register `BlogModel` in `admin.py`:
```python
from blogapp.models import BlogModel,AuthorModel,CommentModel,ReviewModel,TagModel
# Register your models here.

admin.site.register(BlogModel)
```
Now perform database migrations:
```bash
py manage.py makemigrations
py manage.py migrate
```
Now Let's enter some data from admin site and prepare to show it in frontend:
create a `template` folder in `manage.py` directory and create `index.html` get a navbar from [external source](https://www.w3schools.com/css/tryit.asp?filename=trycss_navbar_horizontal_black_right) , make sure to add `template` dir in `settings.py` file: `'DIRS': [BASE_DIR, 'templates']`:
```html
<!DOCTYPE html>
<html>
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}
</style>
</head>
<body>

<ul>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li style="float:right"><a class="active" href="#about">About</a></li>
</ul>
<h1>This is home page</h1>
</body>
</html>
```
Now create separate `navbar.html` and only cut `ul` there:
```html
<ul>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li style="float:right"><a class="active" href="#about">About</a></li>
</ul>
```
Now in `index.html` do the template mastering using `include` and `block`:
```html
{% include 'navbar.html' %}
{% block content %}
<h1>This is home page</h1>
{% endblock content %}
```
Now when creating others page we just need to `extends` `index.html` and `block content` will be that page content. e.g:
```html
{% extends 'index.html' %}
{% block content %}
<h1>This is news page</h1>
{% endblock content %}
```
Now lets add it in `views.py`
```python
from django.shortcuts import render,redirect,HttpResponse
from blogapp.models import BlogModel,AuthorModel,CommentModel,ReviewModel,TagModel

def home(request):
    blog=BlogModel.objects.all()
    myDict={
        'blog':blog
    }
    return render(request,'index.html',myDict)
```
here `blog=BlogModel.objects.all()` to read `blogModel` data from database. now set `url.py`'s `urlpatterns`:
```python
path('home/',home,name='home'),
```
Now let's add a table from [external source](https://www.w3schools.com/css/tryit.asp?filename=trycss_table_fancy):
```html
<!DOCTYPE html>
<html>
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}
</style>
</head>
<body>

{% include 'navbar.html' %}

{% block content %}
<h1>This is blog page</h1>
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Blog Title</th>
    <th>Blog Author</th>
    <th>Blog Date</th>
  </tr>

  {% for i in blog %}
  <tr>
    <td>{{i.blog_title}}</td>
    <td>{{i.blog_author}}</td>
    <td>{{i.blog_date}}</td>
  </tr>
  {% endfor %}

</table>

</body>
</html>

{% endblock content %}
    
</body>
</html>

```
Here `{% for i in blog %}`is used to loop through the `blog`. Similarly other model will be created and read the data from database to show it in frontend.
###  Common errors
- `OperationalError`: When `makemigrations` / `migrate` not performed and try to access database data, it will give `OperationalError`
- `Value not Assign`: This error occurs sometimes, to solve this error inside `app`'s `models.py` file set `null=True` e.g: `author_name=models.CharField(max_length=100, null=True)`

### Day 06 Recap:
- Create project & app under virtual environment
- Migrate db & create superuser
- Create 5 models, 5 navbar for each model
- Read the database data
- Show the data in frontend

### Task
- Presentation from day 1 to day 6
- submit video (youtube)
- 1 app, 5 model, 5 navbar

</details>

<details>
<summary>Day-06-A Quick Recap from Day 01 to Day 06</summary>

1. Create and active environment
    - `py -m venv env`
    - `./env/Scripts/activate`
2. Create django project
    - `django-admin startproject my_project`
    - `cd my_project`
    - `py manage.py runserver`
3. Migrate database
    - `py manage.py makemigrations`
    - `py manage.py migrate`
4. Create superuser
    - `py manage.py createsuperuser`
5. Show simple text on website
    - Create a `views.py` within prject directory
    - Use `HttpResponse` to view a simple `Text/String`
    - import created function in `urls.py` file and add `urlpatterns` path
6. Render a simple html page
    - First add django static file path setting in `settings.py` file
    - Create `template` folder in `manage.py` directory
    - Now create a `html` file within `template` folder
    - Go to project directory and create a function to render the created `html` file.
7. Show a simple table in html page
    - After doing `6th` step, create a simple table with html `table tag`
8. Get a table from external source and view it
    - Get a `fancy table` from `w3school`
9. Now send table data from backend
    - In `views.py` where `function` is defined add a `dictionary` there and `return` it
10. Get a navbar from external source
    - Get a horizontal `navbar` from `w3school`
11. By template mastering separate navbar and use on other pages
    - Create a `navbar.html` file
    - Now use `include` in `index.html` page to show the navbar in index page
    - Use `block content` to show the content
    - For other pages use `extends`
12. Now Create a app and model
    - `py manage.py startapp blogapp`
    - Add this app name in `settings.py` file within `INSTALLED_APPS`
    - Now in created `blogapp` there is `models.py`
    - Create a `Model` and register it in `admin.py`
    - Each time changes in `models.py` do `py manage.py makemigrations` and `py manage.py migrate`
13. Now show the created model data in frontend
    - Create a `blog.html` put table data here using `block content` and `extends` `index.html` at first line which will include the `navbar`
    - In views.py import the created `model`. Create a function and get the model data in a `varible` using `objects.all()`. Now create a `dictionary` and assign it with the `variable` of `model data`. return the dictionary.
    - Now add `path` in `urls.py` file
    - Go to `navber.html` and add `url` with created `path name`
    - In `blog.html` create a for `loop` to show the model data

</details>

<details>
<summary>Day-07-Exam Day 01 Practical Exam (23-03-2024)</summary>

## Exam Day 01 on Day-06 task (Practical Exam)
### Question:
- Create a studentModel with all the functionality you have learned from day 01 to day 06:
  - Create a folder as 'your_name'
  - Create Django project within virtual environment
  - Create a app for model creation
  - Include a navbar for navigation
  - Do template mastering
  - Fetch the data from database to frontend
  - Show the student model data in frontend

</details>

<details>
<summary>Day-08-Exam Day 02 Written Exam (24-03-2024)</summary>

## Exam Day 02 on Day-06 task (Written Exam)
### Question:
- 5 MCQ Question
- 8 Short Question
- 2 Practical Question

### MCQ Question
Which of the following is not a component of a Django project?
  - [ ] Views
  - [ ] Models
  - [ ] Controllers
  - [ ] Templates

What is the purpose of the urls.py file in Django?
  - [ ] To define the structure of the database
  - [ ] To specify the URL patterns of the routing
  - [ ] To configure project-wide settings
  - [ ] To define HTML templates

What command is used to create a new Django project?
  - [ ] django new
  - [ ] django startproject
  - [ ] django create
  - [ ] django init

In Django, which file is used to define database models?
  - [ ] views.py
  - [ ] models.py
  - [ ] settings.py
  - [ ] admin.py

What command is used to apply database migrations in Django?
  - [ ] manage.py apply
  - [ ] manage.py migrate
  - [ ] manage.py update
  - [ ] manage.py deploy

### Short Question
1. Describe the purpose of urls.py, models.py, admin.py
2. Which files is responsible for defining the database settings for a Django project?
3. What are migrations in Django? Explain the purpose of the `manage.py makemigrations` and `manage.py migrate` commands.
4. How do you define URL patterns in Django's `urls.py`
5. What is the purpose of the `settings.py` file in Django?
6. What is the purpose of Django's template language?
7. What is the default database used by Django and how do you configure it?
8. Explain the concept of the middleware in Django

### Practical Question
- Create a Django project named "myproject" and an app named "myapp". Define a model in "myapp" with fields: name (CharField) and age (IntegerField)
- Write a function-based view in Django to render a simple HTML template that displays "Hello, World!"
### Task : 
- Poster presentation based on Day 01 to Day 06 (27-03-2024)
- Oral test tomorrow (25-03-2024)

</details>

<details>
<summary>Day-09-Django CRUD Add Operation From Frontend (25-03-2024)</summary>

## Day 09 Topics:
- Day 01 - 06 recap
- Oral test
- Model add operation from frontend
- null = True explained
- An error after modifying previous saved model (null return typeError)
- Day 09 Recap
- Task

### Model add operation from frontend
Create a form page `addstudent.html`
```html
{% extends 'base.html' %}

{% block content %}
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
<body>

<h3>Using CSS to style an HTML Form</h3>

<div>
  <form action="{% url 'addstudent' %}" method="POST">
    {% csrf_token %}
    <label for="fname">Name</label>
    <input type="text" id="fname" name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" name="city" placeholder="Your City">
  
    <input type="submit" value="Submit">
  </form>
</div>

</body>
</html>
{% endblock content %}
    
```
- Here method will be always `POST`
- Here action url will be the name value from `urls.py` file of `addstudent`
- `csrf_token` is used for security
- Here `name="department"` is important as we will get the form value by this

Now add a function in `views.py` as below:
```python
def addstudent(request):
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=studentModel(
            Name=name,
            Department=department,
            City=city,
        )
        
        student.save()
        return redirect('student')
    return render(request,'addstudent.html')
```
- Here if `request.method=='POST'` is true then we will get the value from form by `POST` method 
- Then we will add those value in our previously created model which is `studentModel`
- After that save the model and in frontend user will be redirected to `student.html` page

### null = True explained
Sometimes we get error while migrating a model. a common solution is adding `null=True`:
```python
class studentModel(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
```
For example let's assume we created a model with 3 entity and work with that but after sometimes when we add a new entity to that model an error will occur as empty value is being assign to the model. so to add that new entity we have to explicitly add `null=True` to add that new entity as empty null value.

### An error after modifying previous saved model (null return typeError)
This error occur as below:
```python
class studentModel(models.Model):
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
```
In this code when we have modified our studentModel entity `return self.Name` will throw an error of type error. commenting this will solved it.
### Day 09 Recap:
- Create Django Models with 5 add operation in frontend
  - Create django project & app in virtual environment
  - Setup app, static, template files
  - Create 5 navigation pages in navbar with table to show the added data
    - Student Table
    - Mark Table
    - Teacher Table
    - Subject Table
    - University Table
  - Create 5 more navigation pages in navbar to add data from frontend
    - Add Student
    - Add Mark
    - Add Teacher
    - Add Subject
    - Add University
  - Create form for each 5 add operation pages

### Task
- Create 5 add operation pages and show the data in table


</details>

<details>
<summary>Day-10-Django CRUD Delete Operation From Frontend (27-03-2024)</summary>

## Day 10 Topics:
- Day 09 recap
- Oral test
- Two annoying error (comma method in form, model return type error)
- Delete operation
- Special notes (return , redirect error)
- Exam Result
- Task

### Oral test:
- Explain urlpatterns (It define to specific path route to handle the request)
- How navigation route is working explain (from urls.py to views.py there request handle the request and fetch the required data to show in the defined html page)
- Explain models.Model and what will happened if we don't use it (in models.Model module SQL is defined)
- Explain Database concept (Entity,attribute,default value,primary key, etc.....)
- How database is configure by settings.py and not models.py (initially everything is configure in settings.py file)
- What we will find if we break database (answer: table)

### Two annoying error
The first one is form submit stay in the same page after submitting
```html
<div>
  <form action="{% url 'addstudent' %}" method="POST">
    {% csrf_token %}
    <label for="fname">Name</label>
    <input type="text" id="fname" name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" name="city" placeholder="Your City">
  
    <input type="submit" value="Submit">
  </form>
</div>
```
- `<form action="{% url 'addstudent' %}" method="POST">` if this line is include comma between `{% url 'addstudent' %}",method="POST"` this cause the page stay in the same page even after submit.

Second one is model return type error
```python
 class studentModel(models.Model):
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
```
- In here `self.Name` return will give error when there is `max_length=100,null=True` it is because when explicitly adding new entity we have to make it `null=True` but by doing this when `return` is trying to access `Name` it get `None` so that causes error. Deleting the value will solved it.

### Delete operation
Go to table html page and add as below `Action column` and Delete url with id:
```html
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
        </td>
    </tr>

  {% endfor %}
    
</table>
```
Now in `views.py` file add a function named `deleteStudent`
```python
def deleteStudent(request,myid):
    student=studentModel.objects.get(id=myid)
    student.delete()
    return redirect('student')
```
In `urls.py` file add as below:
```python
from django.contrib import admin
from django.urls import path
from d10_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteStudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
]
```
### Special notes
- When a function is defined but not return or redirect to anything than an error will occur
  ```python
  def deleteStudent(request,myid):
      student=studentModel.objects.get(id=myid)
      student.delete()
  ```
- This will do the delete but after that will show an error page with `deleteStudent didn't return an HttpResponse object it returned None Instead`

## Exam Result
- **Practical** --> 25/25 (Completed the task in 17 minutes ; time limit was 30 minutes)
- **Written** --> 21/25 (Short question database configure answer was `settings.py`, Others question need to be answer in more detail way)
- **Oral** --> 7/10 (Was confuse on database and how navigation works in backend question)
- **Total** --> `53 marks`

### Task:
- Create 5 models & perform delete operation from frontend
    - Create 5 model:
        - StudentModel
        - MarkModel
        - TeacherModel
        - SubjectModel
        - UniversityModel
    - Create 5 page in drop down navbar with table to show the added data
        - Student Table
        - Mark Table
        - Teacher Table
        - Subject Table
        - University Table
    - Create 5 form page for each table pages
        - Add Student
        - Add Mark
        - Add Teacher
        - Add Subject
        - Add University
    - Add an action on each table column to delete data


</details>

<details>
<summary>Day-11-Django CRUD Edit Update & View Operation (28-03-2024)</summary>

## Day 11 Topics:
- Day 10 Recap
- Edit operation
- Add view action
- Get vs Filter QuerySet
- Task

## Edit operation
In table page `student.html` add a href link for edit action:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="">Edit</a>
        </td>
    </tr>

  {% endfor %}
    
</table>

</body>
</html>



{% endblock content %}
    
```
- Here href is empty so let's add a page for editing then link that page in this `href`

Create `editstudent.html` file and add as below:
```html
{% extends 'base.html' %}


{% block content %}
<h1> edit page </h1>
{% endblock content %}
    
```
Now create a function in `views.py` file to view this page:
```python
def editstudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    myDict={
        'student':student
    }
    return render(request,'editstudent.html',myDict)
```
- Here we have `myid` which is needed to specific data and using `filter QuerySet` as it is iterable. 

Now import this in `urls.py` file and create the route path
```python
from django.contrib import admin
from django.urls import path
from d11_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,editstudent,
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
]

```
- Here `<int:myid>` to get the id in path route

Finally add this url `name` in `student table` page with for loop to iterate the data
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="{% url 'editstudent' i.id %}">Edit</a>
        </td>
    </tr>

  {% endfor %}
    
</table>

</body>
</html>

{% endblock content %}
    
```
Now we will be able to see the data in `edit page` as below:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}


</style>
<body>

<h3>Using CSS to style an HTML Form</h3>

<div>
  <form action="" method="POST">
    {% csrf_token %}
    
    {% for i in student %}
    <label for="fname">ID</label>
    <input type="text" id="fname" value={{i.id}} name="myid" placeholder="Your ID.." readonly>
    <label for="fname">Name</label>
    <input type="text" id="fname" value={{i.Name}} name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" value={{i.Department}} name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" value={{i.City}} name="city" placeholder="Your City">
    {% endfor %}
        

  
    <input type="submit" value="Submit">
  </form>
</div>

</body>
</html>
{% endblock content %}
    
```
As we are able to see the data which we can edit but we need to implement the submit to work with update functionalities. For that we will create a update function in `views.py`
```python
def updatestudent(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=studentModel(
            id=myid, # this need to be done otherwise new value will be added rather than update
            Name=name,
            Department=department,
            City=city,
        )
        student.save()
        return redirect('student')
```
- This is similar as add function only deference is editing it by specific `ID`

Now import and create the path in `urls.py`
```python
from django.contrib import admin
from django.urls import path
from d11_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,editstudent,updatestudent,viewstudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
    path('updatestudent',updatestudent,name='updatestudent'),
    
]

```
Now the `name` value `'updatestudent'` will be in the action url of the edit page form as: `<form action="{% url 'updatestudent' %}" method="POST">`


### Add view action:
Create a view page `viewstudent.html`:
```html
{% extends 'base.html' %}


{% block content %}

<h1>View student page</h1>

{% endblock content %}
    
```
It is similar as editing function; add view function in `views.py`:
```python
def viewstudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    myDict={
        'student':student
    }
    return render(request,'viewstudent.html',myDict)
```

Add path in `urls.py`:
```python
from django.contrib import admin
from django.urls import path
from d11_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,editstudent,updatestudent,viewstudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
    path('updatestudent',updatestudent,name='updatestudent'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    
]

```
Add `viewstudent` in `href` of `student table` view action:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="{% url 'editstudent' i.id %}">Edit</a>
          <a href="{% url 'viewstudent' i.id %}">View</a>
        </td>
    </tr>

  {% endfor %}
    
</table>

</body>
</html>
{% endblock content %}

```
Now after clicking on `View` it will go to `viewstudent.html` page , Let's add a `CSS card` and loop throw the value we will get to show it in user info format:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 40%;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.container {
  padding: 2px 16px;
}
</style>
</head>
<body>

<h2>Card</h2>

<div class="card">
  <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="width:100%">
  <div class="container">
    
    {% for i in student %}
    <h4><b>{{i.Name}}</b></h4> 
    <p>{{i.Department}}</p> 
    <p>{{i.City}}</p> 
    {% endfor %}
        

  </div>
</div>

</body>
</html> 

{% endblock content %}
    
```

### Get vs Filter QuerySet
- Get is not iterable
- Filter is iterable

While trying to get user data a problem was faced and this [Stack Overflow](https://stackoverflow.com/questions/56374741/django-model-object-is-not-iterable) answer helped.

### Task:
- Create Edit Update & View action in table data
- Saturday (30-03-2024) Exam based on Day 1 to 11 task

</details>

<details>
<summary>Day-11-Django CRUD Quick recap</summary>

## Django CRUD Quick recap:
1. setup virtual env and django project
    - `.\env\Scripts\activate`
    - `django-admin startproject d11_practise`
2. Migrate database and create superuser
    - `py manage.py makemigrations`
    - `py manage.py migrate`
    - `py manage.py createsuperuser`
3. Create an app
    - `py manage.py startapp studentapp`
4. Add the app name in `settings.py` file `INSTALLED_APPS`
    - `'studentapp'`
5. Add Django static file & template path
    - Static file (at the end):
        ```python
        STATICFILES_DIRS = [
        BASE_DIR / "static",
        "/var/www/static/",
        ]
        ```
    - Template path in TEMPLATES:
        `'DIRS': [BASE_DIR,'template'],`
6. Create a `template` folder in `manage.py` directory and create some initial pages like `base.html`, `navbar.html` etc.
7. Get a navbar code from external site and paste it in `base.html`
8. For template mastering separate navbar from the `base.html` and paste it in `navbar.html` file
    ```html
    <ul>
    <li><a href="#student">Student</a></li>
    </ul>
    ```
9. Now in `base.html` `include` it and create a empty `block content` inside body tag
    ```html
    <body>

    {% include 'navbar.html' %}


    {% block content %}
        
    {% endblock content %}

    </body>
    ```
10. Now create a `student.html` page and `extends` the `base.html` with its own `block content`
    ```html
    {% extends 'base.html' %}

    {% block content %}
        <h1>Student page</h1>
    {% endblock content %}
    ```
11. Now to view the `student.html` page we need to create `views.py` file in project directory where `settings.py` exits. In `views.py` we need to define a function where we will render our created `student.html` file
    ```python
    from django.shortcuts import render,redirect

    def student(request):
    return render(request,'student.html')
    ```
12. Now in` urls.py` file we have to import our created `student` function set the route
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
    ]
    ```
13. Now we have to add the `name` value in `navbar.html` file `href`
    ```html
    <ul>
        <li><a href="{% url 'student' %}">Student</a></li>
    </ul>
    ```
14. Now in `http://127.0.0.1:8000/student/` link we can view our created `student.html` page
15. Let's add a table in our student page. a table from w3school (fancy table)
    ```html
    {% extends 'base.html' %}


    {% block content %}
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    #customers {
    font-family: Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width: 100%;
    }

    #customers td, #customers th {
    border: 1px solid #ddd;
    padding: 8px;
    }

    #customers tr:nth-child(even){background-color: #f2f2f2;}

    #customers tr:hover {background-color: #ddd;}

    #customers th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    background-color: #04AA6D;
    color: white;
    }
    </style>
    </head>
    <body>

    <h1>A Fancy Table</h1>

    <table id="customers">
    <tr>
        <th>Name</th>
        <th>Department</th>
        <th>City</th>
    </tr>
    </table>

    </body>
    </html>
    {% endblock content %}
    ```
16. To add table let's create model in our app `models.py` file
    ```python
    from django.db import models

    # Create your models here.
    class studentModel(models.Model):
        Name=models.CharField(max_length=100)
        Department=models.CharField(max_length=100)
        City=models.CharField(max_length=100)
        
        def __str__(self):
            return self.Name
    ```
17. Register this model in `admin.py`
    ```python
    from django.contrib import admin
    from studentapp.models import studentModel

    # Register your models here.
    admin.site.register(studentModel)
    ```
18. Now we have to migrate it
    - `py manage.py makemigrations`
    - `py manage.py migrate`
19. Now go to admin page `http://127.0.0.1:8000/admin/` and add data in student model
20. To see the data in frontend we have to `READ` it. let's import our model in `views.py` and return the data as `dictionary` in frontend
    ```python
    from django.shortcuts import render,redirect
    from studentapp.models import studentModel

    def student(request):
        student=studentModel.objects.all()
        myDict={
            'student':student
        }
        return render(request,'student.html',myDict)
    ```
21. Now in our `student.html` file we have to iterate the student data using loop
    ```python
    <table id="customers">
    <tr>
        <th>Name</th>
        <th>Department</th>
        <th>City</th>
    </tr>
    
    {% for i in student %}
        <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        </tr>
    {% endfor %}
        
    </table>
    ```
    Here `i.Name`, `i.Department`, `i.City` will be same as defined in `models.py` file. Now we can see the data in frontend at `http://127.0.0.1:8000/student/` route.
22. Now let's add data from frontend not from admin page, to do that we will create a form page named `addstudent.html`
    ```html
    {% extends 'base.html' %}

    {% block content %}
    <!DOCTYPE html>
    <html>
    <style>
    input[type=text], select {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    }

    input[type=submit] {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    }

    input[type=submit]:hover {
    background-color: #45a049;
    }
    </style>
    <body>

    <h3>Using CSS to style an HTML Form</h3>

    <div>
    <form action="" method="">
        {% csrf_token %}
        <label for="fname">Name</label>
        <input type="text" id="fname" name="name" placeholder="Your name..">

        <label for="lname">Department</label>
        <input type="text" id="lname" name="department" placeholder="Your Department">
        <label for="lname">City</label>
        <input type="text" id="lname" name="city" placeholder="Your City">
    
        <input type="submit" value="Submit">
    </form>
    </div>

    </body>
    </html>
    {% endblock content %}
    ```
    Here `action`, `method`, `name` attribute is important
23. To view `addstudent` form page we will similarly create a function in `views.py` to render it
    ```python
    def addstudent(request):
        return render(request,'addstudent.html')
    ```
    Add the path in `urls.py` file for routing
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student,addstudent

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
        path('addstudent/',addstudent,name='addstudent'),
    ]
    ```
    To see it in frontend let's add the `name` in `navbar.html` file
    ```html
    <ul>
        <li><a href="{% url 'student' %}">Student</a></li>
        <li><a href="{% url 'addstudent' %}">Add Student</a></li>
    </ul>
    ```
24. Now to get the data from frontend to backend we will assign the `action`
    - `action="{% url 'addstudent' %}"` and set the method as POST `method="POST"`
    - Set the `name` attribute, will be used to get the value
25. In `views.py` `addstudent` function we will get the value and assign it in our model
    ```python
    def addstudent(request):
        if request.method=='POST':
            name=request.POST.get('name')
            department=request.POST.get('department')
            city=request.POST.get('city')
            
            student=studentModel(
                Name=name,
                Department=department,
                City=city,
            )
            student.save()
            return redirect('student')
        return render(request,'addstudent.html')
    ```
    Here we have get the values by `name attribute` then assign those value in our `model` after that we save it and `redirect` to the `student` page. Now in our `http://127.0.0.1:8000/addstudent/` route we can add data in our form and after submitting the data will be shown in `http://127.0.0.1:8000/student/` route
26. Now Let's create a action for deleting the data, In `student.html` page create a table column `Action` and create a `href link` as `Delete`
    ```html
    <table id="customers">
    <tr>
        <th>Name</th>
        <th>Department</th>
        <th>City</th>
        <th>Action</th>
    </tr>
    
    {% for i in student %}
        <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td><a href="">Delete</a></td>
        </tr>
    {% endfor %}
        
    </table>
    ```
27. Now we have to create a functions in `views.py` with id so that we can `filter` the specific id to delete
    ```python
    def deletestudent(request,myid):
        student=studentModel.objects.filter(id=myid)
        student.delete()
        return redirect('student')
    ```
    In `urls.py` we have to specify the id also
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student,addstudent,deletestudent

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
        path('addstudent/',addstudent,name='addstudent'),
        path('deletestudent/<int:myid>',deletestudent,name='deletestudent'),
    ]
    ```
    Now we have to add the `href` url in` Delete`:

    `<td><a href="{% url 'deletestudent' i.id %}">Delete</a></td>`

    Now the `Delete action` will work in our student table
28. Now let's Edit the table value, add a new Action in table as `Edit`
    ```html
      <td>
        <a href="{% url 'deletestudent' i.id %}">Delete</a>
        <a href="">Edit</a>
      </td>
    ```
    Create the same form page of add student but as `editstudent.html`
    ```html
    {% extends 'base.html' %}

    {% block content %}
    <!DOCTYPE html>
    <html>
    <style>
    input[type=text], select {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    }

    input[type=submit] {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    }

    input[type=submit]:hover {
    background-color: #45a049;
    }
    </style>
    <body>

    <h3>Using CSS to style an HTML Form</h3>

    <div>
    <form action="" method="POST">
        {% csrf_token %}
        <label for="fname">Name</label>
        <input type="text" id="fname" name="name" placeholder="Your name..">

        <label for="lname">Department</label>
        <input type="text" id="lname" name="department" placeholder="Your Department">
        <label for="lname">City</label>
        <input type="text" id="lname" name="city" placeholder="Your City">
    
        <input type="submit" value="Submit">
    </form>
    </div>

    </body>
    </html>
    {% endblock content %}
    ```
    Create a function in `views.py`
    ```python
    def editstudent(request,myid):
        student=studentModel.objects.filter(id=myid)
        myDict={
            'student':student
        }
        return render(request,'editstudent.html',myDict)
    ``` 
    Here we are reading the data from our model and sending it to form of `editstudent.html` file.

    Add the path in `urls.py`
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student,addstudent,deletestudent,editstudent

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
        path('addstudent/',addstudent,name='addstudent'),
        path('deletestudent/<int:myid>',deletestudent,name='deletestudent'),
        path('editstudent/<int:myid>',editstudent,name='editstudent'),
    ]
    ```
    Now add this `name` value in `Edit` action `href`

    `<a href="{% url 'editstudent' i.id %}">Edit</a>`

    Now after clicking on edit it wil show the form of `editstudent.html` file. Let's iterate using loop to show the value also for editing with `value` attribute
    ```html
    <form action="" method="POST">
        {% csrf_token %}
        
        {% for i in student %}
        <label for="fname">ID</label>
        <input type="text" id="fname" value={{i.id}} name="myid" placeholder="Your id.." readonly>
        <label for="fname">Name</label>
        <input type="text" id="fname" value={{i.Name}} name="name" placeholder="Your name..">

        <label for="lname">Department</label>
        <input type="text" id="lname" value={{i.Department}} name="department" placeholder="Your Department">
        <label for="lname">City</label>
        <input type="text" id="lname" value={{i.City}} name="city" placeholder="Your City">
        {% endfor %}
        <input type="submit" value="Submit">
    </form>
    ```
    Here a new attribute added which is `value` also `id` viewing as `readonly`

29. Now to make the edit work we will define a function `views.py` as `updatestudent`
    ```python
    def updatestudent(request):
        if request.method=='POST':
            myid=request.POST.get('myid')
            name=request.POST.get('name')
            department=request.POST.get('department')
            city=request.POST.get('city')
            
            student=studentModel(
                id=myid,
                Name=name,
                Department=department,
                City=city,
            )
            student.save()
            return redirect('student')
    ```
    Now add the path in `urls.py` 
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student,addstudent,deletestudent,editstudent,updatestudent

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
        path('addstudent/',addstudent,name='addstudent'),
        path('deletestudent/<int:myid>',deletestudent,name='deletestudent'),
        path('editstudent/<int:myid>',editstudent,name='editstudent'),
        path('updatestudent',updatestudent,name='updatestudent'),
    ]
    ```
    Now update the `action` in `editstudent.html` file as `action="{% url 'updatestudent' %}"`

    This will make the submit work after editing.
30. To add `View action` we can do the same as where we define our function with id to view the specific table data.

</details>

<details>
<summary>Day-12-Assessment-02 (30-03-2024)</summary>

## Day 12 Assessment-02

Question: As a job recruiter, you are tasked with hiring a Django developer for a project that involves managing user data. You need to create a model to store information about potential candidates. Define the fields for this model, keeping in mind the CRUD (Create, Read, Update, Delete) operations you may need to perform.

> Define the following fields for the candidate model, using only CharField type:

`full_name`: A CharField to store the full name of the candidate.

`email`: A CharField to store the email address of the candidate.

`phone_number`: A CharField to store the phone number of the candidate.

`address`: A CharField to store the address of the candidate.

`job_title`: A CharField to store the job title or desired position of the candidate.

`linkedin_profile`: A CharField to store the Linkedin profile URL of the candidate.

`university`: A CharField to store the university or educational institution of the candidate.

`degree`: A CharField to store the degree attained by the candidate.

`languages`: A CharField to store the languages known by the candidate.

`years_of_experience`: A CharField to store the years of professional experience of the candidate.

> Total time took for me --> 43 Minutes

</details>

<details>
<summary>Day-13-Python Basic Day 01, View Action & All Model Table Data in Single Page (31-03-2024)</summary>

## Day 13 Topics:
- Security & code editor
- Python Basic Day 01
- Variable
- View Action 
- Task

### Security & code editor
Compiler / Interpreter -->Translator (Python has both)

- Interpreter--> (line by line)
- Compiler--> (Run at once)
- Security (csrf,session-hijack,man in the middle attack,vulnerability)
- Authentication

### Python Basic
- Variable
- Operator
- Condition (increment / decrement)
    - Nested condition
- Loop
    - Nested loop
- Array (1d,2d,3d)
    - List
    - Set
    - Tuple
    - Dictionary
- Function
    - Recurssion (self call)
- OOP 
    - Inheritance
    - Incapsulation
    - Polymorphism
    - Class / Object
### Variable
- Changeable (able to vary)
- It is volatile
- Assign sign (`=`)
- Comparison / equal (`==`)

### View Action

To add view action go to the table page `student.html` file and add view action:
```html
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="">View</a>
        </td>
    </tr>

  {% endfor %}
    
</table>
```
Now create a page `viewstudent.html` page and use the css card html code there:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>

<h2 style="text-align:center">User Profile Card</h2>


{% for i in student %}
<div class="card">
    <img src="/w3images/team2.jpg" alt="John" style="width:100%">
    <h1>{{i.Name}}</h1>
    <p class="title">{{i.Department}}, {{i.City}}</p>
  </div>
{% endfor %}
    


</body>
</html>

{% endblock content %}
    
```
Now Create function in `views.py` file:
```python
def viewstudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    myDict={
        'student':student
    }
    return render(request,'viewstudent.html',myDict)
```
Add the url path in `urls.py` file
```python
from django.contrib import admin
from django.urls import path
from d13_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,viewstudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
]
```
Now add url in student page view action `<a href="{% url 'viewstudent' i.id %}">View</a>` with id.

Similarly it is done with other pages too.

For viewing all model table in single page. Just create a new page and add a function in `views.py` that return all table data from models  and link the url path 

`alltable.html`:
```html
{% extends 'base.html' %}

{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>Student Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
    </tr>
  {% endfor %}
    
</table>
<h1>Mark Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Roll</th>
    <th>Mark</th>
  </tr>
  
  {% for i in mark %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Roll}}</td>
        <td>{{i.Mark}}</td>
    </tr>
  {% endfor %}
    
</table>
<h1>Teacher Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
  </tr>
  
  {% for i in teacher %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
    </tr>
  {% endfor %}
    
</table>
<h1>Subject Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Category</th>
    <th>Mark</th>
  </tr>
  
  {% for i in subject %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Category}}</td>
        <td>{{i.Mark}}</td>
    </tr>
  {% endfor %}
    
</table>
<h1>University Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Rank</th>
    <th>Location</th>
  </tr>
  
  {% for i in university %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Rank}}</td>
        <td>{{i.Location}}</td>
    </tr>
  {% endfor %}
    
</table>

</body>
</html>

{% endblock content %}
    
```

`views.py`:
```python
def alltable(request):
    student=studentModel.objects.all()
    mark=markModel.objects.all()
    teacher=teacherModel.objects.all()
    subject=subjectModel.objects.all()
    university=universityModel.objects.all()
    myDict={
        'student':student,
        'mark':mark,
        'teacher':teacher,
        'subject':subject,
        'university':university,
    }
    return render(request,'alltable.html',myDict)
```

`urls.py`:
```python
from django.contrib import admin
from django.urls import path
from d13_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,viewstudent,viewteacher,viewmark,viewsubject,viewuniversity,alltable
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    path('viewteacher/<int:myid>',viewteacher,name='viewteacher'),
    path('viewmark/<int:myid>',viewmark,name='viewmark'),
    path('viewsubject/<int:myid>',viewsubject,name='viewsubject'),
    path('viewuniversity/<int:myid>',viewuniversity,name='viewuniversity'),
    path('alltable/',alltable,name='alltable'),
    
]
```
Now link the `alltable.html` page in navbar:
```html
<div class="navbar">
    <div class="dropdown">
      <button class="dropbtn">Add Tables 
        <i class="fa fa-caret-down"></i>
      </button>
      <div class="dropdown-content">
        <a href="{% url 'addstudent' %}">Add Student</a>
        <a href="{% url 'addmark' %}">Add Mark</a>
        <a href="{% url 'addteacher' %}">Add Teacher</a>
        <a href="{% url 'addsubject' %}">Add Subject</a>
        <a href="{% url 'adduniversity' %}">Add University</a>
      </div>
    </div> 
    <div class="dropdown">
      <button class="dropbtn">View Tables 
        <i class="fa fa-caret-down"></i>
      </button>
      <div class="dropdown-content">
        <a href="{% url 'student' %}">Student Table</a>
        <a href="{% url 'mark' %}">Mark Table</a>
        <a href="{% url 'teacher' %}">Teacher Table</a>
        <a href="{% url 'subject' %}">Subject Table</a>
        <a href="{% url 'university' %}">University Table</a>
        <a href="{% url 'alltable' %}">All Table</a>
      </div>
    </div> 
  </div>
```
### Task:
- Practice variable task
- Add view action
- Show all model data in single page

</details>

<details>
<summary>Day-14-Add Image Option with Delete, Edit, View Action (01-04-2024)</summary>

## Day 14 Topics:
- Day 13 recap
- Add Image
- Disscussion on previous batch final assessment
- Task

### Add Image
For adding image , first we have to add image field in our model
```python
class studentModel(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    StudentImage=models.ImageField(upload_to='media/StudentImages',null=True)
    
    def __str__(self):
        return self.Name
```
- Here `StudentImage` is added with `ImageField` which include path `media/StudentImages`
- Setting `null=True` either an error will occur

After changes in model we have to use migrations command: `py manage.py makemigrations` then `py manage.py migrate`

Now we can add image from admin site : `http://127.0.0.1:8000/admin/`

After adding image to view it in frontend table, we have to edit our `student.html` page table 
```html
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Image</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <img src="/{{i.StudentImage}}" alt="" width="50">
        </td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="{% url 'viewstudent' i.id %}">View</a>
        </td>
    </tr>

  {% endfor %}
    
</table>
```
- Here `<img src="/{{i.StudentImage}}" alt="" width="50">` is added ad source of the image. This line can be written like this also: `<img src="{{i.StudentImage.url}}" alt="" width="50">`
- Now another important things to do otherwise image won't show. which is adding `static media url` in `urls.py` file
    ```python
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        # ... the rest of URLconf goes here ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
- Now we can see the image in table

Now Let's add the image from frontend, modify the `addstudent.html` file as below:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}


</style>
<body>

<h3>Using CSS to style an HTML Form</h3>

<div>
  <form action="{% url 'addstudent' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    <label for="fname">Name</label>
    <input type="text" id="fname" name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" name="city" placeholder="Your City">
    <label for="lname">Image</label>
    <input type="file" id="lname" name="studentImage" placeholder="Your City">
  
    <input type="submit" value="Submit">
  </form>
</div>

</body>
</html>

{% endblock content %}
    
```
- Here Image type is file which is written as `type="file"`
- `enctype="multipart/form-data"` is important otherwise image won't be added

Now we have to edit our `addstudent` function in `views.py`
```python
def addstudent(request):
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        studentImage=request.FILES.get('studentImage')
        
        student=studentModel(
            Name=name,
            Department=department,
            City=city,
            StudentImage=studentImage,
        )
        
        student.save()
        return redirect('student')
    return render(request,'addstudent.html')
```
- Here `studentImage` is getting the image by `request.FILES.get('studentImage')`
- After that including it in model `StudentImage=studentImage,` then save and redirected to student table page

Now to make the image to view in `viewstudent.html` page
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>

<h2 style="text-align:center">User Profile Card</h2>


{% for i in student %}
<div class="card">
    <img src="/{{i.StudentImage}}" alt="" style="width:100%">
    <h1>{{i.Name}}</h1>
    <p class="title">{{i.Department}}, {{i.City}}</p>
  </div>
{% endfor %}
    


</body>
</html>

{% endblock content %}
    
```
- Here same as the way we show the image source in table `<img src="/{{i.StudentImage}}" alt="" style="width:100%">`

Now let's do the edi part, we need the same form as `addstudent.html` page form in `editstudent.html`
```html
{% extends 'base.html' %}

{% block content %}
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

</style>
<body>

<h3>Using CSS to style an HTML Form</h3>

<div>
  <form action="{% url 'updatestudent' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}

    
    {% for i in student %}
               
    <label for="fname">ID</label>
    <input type="text" id="fname" value={{i.id}} name="myid" placeholder="Your id.." readonly>
    <label for="fname">Name</label>
    <input type="text" id="fname" value={{i.Name}} name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" value={{i.Department}} name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" value={{i.City}} name="city" placeholder="Your City">
    <label for="lname">Current Image:</label><br>
    <img src="/{{i.StudentImage}}" alt="" width="50"> <br>
    
    <label for="lname">Image</label>
    <input type="file" id="lname" name="studentImage" placeholder="Your City"> 
    {% endfor %}

  
    <input type="submit" value="Update">
  </form>
</div>

</body>
</html>

{% endblock content %}
    
```
- Here for loop is added
- `value` attribute added
- To show the current image , image source is added
- To make the update work the function `updatestudent` is created in `views.py`
```python
def updatestudent(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        studentImage=request.FILES.get('studentImage')
        
        student=studentModel(
            id=myid,
            Name=name,
            Department=department,
            City=city,
            StudentImage=studentImage,
        )
        student.save()
        return redirect('student')
```
- All are similar but image is getting by `FILES`

Finally add the url path in `urls.py`
```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from d14_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,viewstudent,viewteacher,viewmark,viewsubject,viewuniversity,alltable,editstudent,updatestudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    path('viewteacher/<int:myid>',viewteacher,name='viewteacher'),
    path('viewmark/<int:myid>',viewmark,name='viewmark'),
    path('viewsubject/<int:myid>',viewsubject,name='viewsubject'),
    path('viewuniversity/<int:myid>',viewuniversity,name='viewuniversity'),
    path('alltable/',alltable,name='alltable'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
    path('updatestudent',updatestudent,name='updatestudent'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Now add this `name` in table edit action
```html
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Image</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <img src="/{{i.StudentImage}}" alt="" width="50">
        </td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="{% url 'viewstudent' i.id %}">View</a>
          <a href="{% url 'editstudent' i.id %}">Edit</a>
        </td>
    </tr>

  {% endfor %}
    
</table>
```
- Here `<a href="{% url 'editstudent' i.id %}">Edit</a>` is added with specific id to view in editpage for editing.

Now the update will work.

### Disscussion on previous batch final assessment
- Portfolio Project

### Task:
- Add image in form
- Delete, Edit, View action with image 

</details>

<details>
<summary>Day-15-Image update (02-04-2024)</summary>

## Day 15 Topics:
- Recap old days work
- Image add problem
- Two ways to write object class
- Edit Image
- Task

### Image add problem
When User don't update image while editing there will be no image to get and error will occur.To handle this we need to implement condition in update function
```python
def updatestudent(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        studentImage=request.FILES.get('studentImage')
        print(f"This is image: {studentImage}")
        if studentImage:
            student=studentModel(
                id=myid,
                Name=name,
                Department=department,
                City=city,
                StudentImage=studentImage,
            )
        else:
            studentbyid=studentModel.objects.get(id=myid)
            student=studentModel(
                id=myid,
                Name=name,
                Department=department,
                City=city,
                StudentImage=studentbyid.StudentImage
            )
        student.save()
        return redirect('student')
```
- Here If-Else condition is applied to check if we are getting the image from frontend or not
- When we don't get the image we will give the model the old image by id `studentbyid=studentModel.objects.get(id=myid)`
- To handle this properly , after learning user authentication this will be implement in good way.

### Two ways to write object class
- We can use `.` with model to inherit the class like this: `student.id`, `student.Name`...

### Edit image
Similar task is repeated for student who failed to complete it. In Day 14 full details is already covered.

### Task
- No task assigned 
- Tomorrow (03-04-2024) exam on Django CRUD

</details>

<details>
<summary>Day-16-Python Basics Day 02 & PDF Download Test (03-04-2024)</summary>

## Day 16 Topics:
- Previous days recap
- Python basics day 2
- PDF Download

### Python basics day 2
- Variable recap 
- Code editor
- first code run
- sum operation
- Symbol - Character - Sign - Letters
    - A - Z
    - 0 - 9
    - Special Character

### PDF Download
- Tested few packages for pdf output of a profile page.
- [pyhtml2pdf](https://pypi.org/project/pyhtml2pdf/) give good output
- Need to implement it in future

</details>

<details>
<summary>Day-17-Python Day 03 & Custom Template Setup (04-04-2024)</summary>

## Day 17 Topics:
- Django Framework Disscussion
- Custom template setup / Customize UI
- Python Day 03
- Task

### Custom template setup / Customize UI
- Download site: [Bootstrapmade](https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/)

- Custom Template setup guide : [Youtube](https://www.youtube.com/watch?v=bFsIXYygsg4)

To setup custom template we have to add the js,images,css files in static folder and in `settings.py` include the static path & template folder path also in template DIR:
```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
```
Now add all the html files in our template folder and set the `index.html` as base html and do the template mastering.
```html
  <main id="main">

{% include 'about.html' %}

{% include 'facts.html' %}

{% include 'skills.html' %}

{% include 'resume.html' %}

{% include 'portfolio.html' %}

{% include 'services.html' %}

{% include 'testomonial.html' %}

{% include 'contact.html' %}

  </main><!-- End #main -->

{% include 'footer.html' %}
```
To make the static files work, we have to load the static and add the static in each files url with static:
```html
<!-- load static at the top line of the base html -->
{% load static %}
  <!-- Vendor JS Files -->
  <script src="{% static 'assets/vendor/purecounter/purecounter_vanilla.js' %}"></script>
  <script src="{% static 'assets/vendor/aos/aos.js' %}"></script>
  <script src="{% static 'assets/vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>
  <script src="{% static 'assets/vendor/glightbox/js/glightbox.min.js' %}"></script>
  <script src="{% static 'assets/vendor/isotope-layout/isotope.pkgd.min.js' %}"></script>
  <script src="{% static 'assets/vendor/swiper/swiper-bundle.min.js' %}"></script>
  <script src="{% static 'assets/vendor/typed.js/typed.umd.js' %}"></script>
  <script src="{% static 'assets/vendor/waypoints/noframework.waypoints.js' %}"></script>
  <script src="{% static 'assets/vendor/php-email-form/validate.js' %}"></script>
```
Now create a function in `views.py`
```python
def portfolio(request):
    return render(request,'index.html')
```
Add the path route in `urls.py`
```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from d17_project.views import student,addstudent,viewstudent,portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    path('portfolio/',portfolio,name='portfolio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
Now we will be able to see our custom website is working.

To include a model table in this custom template we will create our model as usual and add it in here using block content
```html
      <nav id="navbar" class="nav-menu navbar">
        <ul>
          <li><a href="#hero" class="nav-link scrollto active"><i class="bx bx-home"></i> <span>Home</span></a></li>
          <li><a href="#about" class="nav-link scrollto"><i class="bx bx-user"></i> <span>About</span></a></li>
          <li><a href="{% url 'student' %}" class="nav-link scrollto"><i class="bx bx-envelope"></i> <span>Student Table</span></a></li>
          <li><a href="#resume" class="nav-link scrollto"><i class="bx bx-file-blank"></i> <span>Resume</span></a></li>
          <li><a href="#portfolio" class="nav-link scrollto"><i class="bx bx-book-content"></i> <span>Portfolio</span></a></li>
          <li><a href="#services" class="nav-link scrollto"><i class="bx bx-server"></i> <span>Services</span></a></li>
          <li><a href="#contact" class="nav-link scrollto"><i class="bx bx-envelope"></i> <span>Contact</span></a></li>
        </ul>
      </nav><!-- .nav-menu -->
```
- Here we added the `{% url 'student' %}` student table. to show it in page:
```html
{% extends 'index.html' %}

{% block content %}

<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>Student Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Image</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
      <td>{{i.Name}}</td>
      <td>{{i.Department}}</td>
      <td>{{i.City}}</td>
      <td>
        <img src="/{{i.Image}}" alt="" width="50">
      </td>
      <td>
        <a href="{% url 'viewstudent' i.id %}">View</a>
      </td>
    </tr>
  {% endfor %}
</table>

</body>
</html>

{% endblock content %}
```
- We have extends the base html which is `index.html` then our content is in block
- Now let's add this after about section just like we did in navbar
```html
{% include 'about.html' %}

{% block content %}
  
{% endblock content %}

{% include 'facts.html' %}

{% include 'skills.html' %}

{% include 'resume.html' %}

{% include 'portfolio.html' %}

{% include 'services.html' %}

{% include 'testomonial.html' %}

{% include 'contact.html' %}

  </main><!-- End #main -->

{% include 'footer.html' %}
```
- Here after about section we added the block content.
- Now we will be able to see our student table.

### Python Day 03
- Discussion on `Operator` & `Operand`

### Contingency management
- Doing same task in variety of way
- Environment management

### Expression evaluation
- [Operator Precedence](https://www.google.com/search?q=operator+precedence)

### Task
- Setup full portfolio custom template in django

</details>

<details>
<summary>Day-17-Portfolio Project</summary>

## Day-17-Portfolio Project
- Created a portfolio project based on this [template](https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/)
- Most of the task followed by creating models and showing the data in frontend
    - First create a project: `django-admin startproject portfolio`
    - Now create app:
        - `cd portfolio`
        - `py manage.py startapp portfolioapp`
    - Add the app in `INSTALLED_APPS` list
        ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'portfolioapp',
        ]
        ```
    - Add static directory `STATICFILES_DIRS` at the end of `settings.py` file
        ```python
        STATICFILES_DIRS = [
            BASE_DIR / "static",
        ]
        ```
    - Add `DIRS` of tamplates folder directory in `TEMPLATES`
        > 'DIRS': [BASE_DIR, 'templates']
    - Add downloaded `.html` content file in `templates` folder which will be created in `manage.py` directory
        ```python 
        project_name/ # Which is portfolio
        │
        ├── manage.py
        ├── project_name/ # portfolio
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── asgi.py
        │   ├── urls.py
        │   └── wsgi.py
        │   └── views.py # This is created manually
        │
        └── templates # This folder is created manually
        │
        └── static # This folder is created manually
        │
        └── app_name/ # Which is portfolioapp
            ├── migrations/
            │   └── __init__.py
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── tests.py
            └── views.py
        ```
    - Now Create static folder and paste all the static files here from the downloaded template
    - Now create `views.py` in project directory and create a function to render it:
        ```python
        from django.shortcuts import redirect,render

        def portfolio(request):

            return render(request,'index.html',myDict)
        ```
    - Now add url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from portfolio.views import portfolio

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',portfolio,name='portfolio'),
        ]
        ```
    - Now if we visit `http://127.0.0.1:8000/admin/` we won't see any static file effect on our html page.
    - We have to load the static file in html to see the effect.
    - Add `{% load static %}` at the top in `index.html` file
    - And change each `src` & `href` that include files from `assets/static` like this: `  <link href="{% static 'assets/img/favicon.png' %}" rel="icon">`
    - If everything done correctly we will be able to see the html page with all the static files loaded perfectly.
    - Now let's make the `index.html` base html and separate other section.
    - Now include those separated section:
        ```html
        <main id="main">

        {% include 'about.html' %}

        {% include 'facts.html' %}

        {% include 'skills.html' %}

        {% include 'resume.html' %}

        {% include 'portfolio.html' %}

        {% include 'services.html' %}

        {% include 'testimonials.html' %}

        {% include 'contact.html' %}

        </main><!-- End #main -->
        ```
    - Now let's create necessary models 
        ```python
        from django.db import models

        # Create your models here.
        class SocialMediaModel(models.Model):
            twitter=models.CharField(max_length=100)
            facebook=models.CharField(max_length=100)
            Instagram=models.CharField(max_length=100)
            skype=models.CharField(max_length=100)
            linkedin=models.CharField(max_length=100)

            def __str__(self):
                return self.twitter

        class AboutModel(models.Model):
            Profile_img = models.ImageField(upload_to='media/ProfileImg')
            Name=models.CharField(max_length=100)
            Profession1=models.CharField(max_length=100)
            Profession2=models.CharField(max_length=100)
            Profession3=models.CharField(max_length=100)
            About_details=models.CharField(max_length=500)
            Profession_title1=models.CharField(max_length=100)
            Profession_title2=models.CharField(max_length=100)
            Profession_details=models.CharField(max_length=500)
            Profession_para=models.CharField(max_length=500)
            Birthday=models.CharField(max_length=100)
            Website=models.CharField(max_length=100)
            Phone=models.CharField(max_length=100)
            City=models.CharField(max_length=100)
            Age=models.CharField(max_length=100)
            Email=models.CharField(max_length=100)
            Freelance_status=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Name
            
        class factModel(models.Model):
            Fact_para=models.CharField(max_length=500)
            Happy_clients=models.CharField(max_length=100)
            Projects=models.CharField(max_length=100)
            Hours_of_support=models.CharField(max_length=100)
            Hard_workers=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Happy_clients
            
        class SkillsModel(models.Model):
            Skill_para=models.CharField(max_length=500)
            
            def __str__(self):
                return self.Skill_para
            
        class SkillMatricesModel(models.Model):
            Skill_name=models.CharField(max_length=100)
            Skill_progressbar=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Skill_name
            
        class ResumeModel(models.Model):
            Resume_para=models.CharField(max_length=500)
            Name=models.CharField(max_length=100)
            About=models.CharField(max_length=100)
            Address=models.CharField(max_length=100)
            Mobile=models.CharField(max_length=100)
            Email=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Name  

        class ResumeEducationModel(models.Model):
            Education_name=models.CharField(max_length=100)
            Education_year=models.CharField(max_length=100)
            Education_institute=models.CharField(max_length=100)
            Education_details=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Education_name
            
        class ResumeProfessionalModel(models.Model):
            Professional_experience=models.CharField(max_length=100)
            Professional_experience_year=models.CharField(max_length=100)
            Professional_experience_location=models.CharField(max_length=100)
            Professional_responsibilities=models.CharField(max_length=100)

            def __str__(self):
                return self.Professional_experience

        class PortfolioModel(models.Model):
            Portfolio_para=models.CharField(max_length=500)
            
            def __str__(self):
                return self.Portfolio_para
            
        class ServicesModel(models.Model):
            Services_para=models.CharField(max_length=500)

            def __str__(self):
                return self.Services_para

        class ServicesSectionModel(models.Model):
            Service_icon=models.CharField(max_length=100)
            Service_name=models.CharField(max_length=100)
            Service_details=models.CharField(max_length=500)
            
            def __str__(self):
                return self.Service_name
            
        class TestimonialModel(models.Model):
            Testimonial_para=models.CharField(max_length=500)
            
            def __str__(self):
                return self.Testimonial_para

        class ClientTestimonialModel(models.Model):
            Client_name=models.CharField(max_length=100)
            Client_img=models.ImageField(upload_to='media/ClientImg')
            Client_profession=models.CharField(max_length=100)
            Client_quote=models.CharField(max_length=500)

            def __str__(self):
                return self.Client_name

        class ContactModel(models.Model):
            Contact_para=models.CharField(max_length=500)
            Contact_location=models.CharField(max_length=100)
            Contact_Email=models.CharField(max_length=100)
            Contact_Call=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Contact_para
        ```
    - Register it in `admin.py`
        ```python
        from django.contrib import admin
        from portfolioapp.models import SocialMediaModel,AboutModel,factModel,SkillsModel,SkillMatricesModel,ResumeModel,ResumeEducationModel,ResumeProfessionalModel,PortfolioModel,ServicesModel,ServicesSectionModel,TestimonialModel,ContactModel,ClientTestimonialModel
        # Register your models here.
        admin.site.register(SocialMediaModel)
        admin.site.register(AboutModel)
        admin.site.register(factModel)
        admin.site.register(SkillsModel)
        admin.site.register(SkillMatricesModel)
        admin.site.register(ResumeModel)
        admin.site.register(ResumeEducationModel)
        admin.site.register(ResumeProfessionalModel)
        admin.site.register(PortfolioModel)
        admin.site.register(ServicesModel)
        admin.site.register(ServicesSectionModel)
        admin.site.register(TestimonialModel)
        admin.site.register(ClientTestimonialModel)
        admin.site.register(ContactModel)
        ```
    - As we can see there will be image too. In order to show the image we have to set the media static:
        ```python 
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from portfolio.views import portfolio

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',portfolio,name='portfolio'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now let's migrate and create our superuser to input data in our model:
        - `py manage.py makemigrations`
        - `py manage.py migrate`
        - `py manage.py createsuperuser`
    - Now to show those data , we have to import it in our `views.py` and return it in `dictionary`
        ```python
        from django.shortcuts import redirect,render
        from portfolioapp.models import SocialMediaModel,AboutModel,factModel,SkillsModel,SkillMatricesModel,ResumeModel,ResumeEducationModel,ResumeProfessionalModel,PortfolioModel,ServicesModel,ServicesSectionModel,TestimonialModel,ClientTestimonialModel,ContactModel

        def portfolio(request):
            socialmedia = SocialMediaModel.objects.get()
            about = AboutModel.objects.get()
            fact = factModel.objects.get()
            skills = SkillsModel.objects.get()
            skills_matrices = SkillMatricesModel.objects.all()
            resume = ResumeModel.objects.get()
            resume_edu = ResumeEducationModel.objects.all()
            resume_pro = ResumeProfessionalModel.objects.all()
            portfolio_des = PortfolioModel.objects.get()
            services_des = ServicesModel.objects.get()
            services_section = ServicesSectionModel.objects.all()
            testimonial_des = TestimonialModel.objects.get()
            client_testimonial = ClientTestimonialModel.objects.all()
            contact = ContactModel.objects.get()
            myDict={
                'socialmedia':socialmedia,
                'about':about,
                'fact':fact,
                'skills':skills,
                'skills_matrices':skills_matrices,
                'resume':resume,
                'resume_edu':resume_edu,
                'resume_pro':resume_pro,
                'portfolio_des':portfolio_des,
                'services_des':services_des,
                'services_section':services_section,
                'testimonial_des':testimonial_des,
                'client_testimonial':client_testimonial,
                'contact':contact,
                
            }
            return render(request,'index.html',myDict)
        ```
    - Everything is set , now all we have to do is to view the models in html file iterate in for loop for those model which are `.objects.all()` and for others which are `.objects.get()` can be directly accessible.

</details>

<details>
<summary>Day-18-Custom Template CRUD Update Operation (16-04-2024)</summary>

## Day 18 Topics:
- Custom template setup recap
- CRUD Operation on Custom Template
- Task

  > Note:- The update option should be on separated admin page but as a practise I did it on the same page. Which will be changed in future.

### CRUD Operation on Custom Template
- It follow up the Day-17 portfolio project
- Today added the `edit option` in about section
    - Get a bootstrap form from [bootstrap site](https://getbootstrap.com/docs/4.0/components/forms/#:~:text=%3Cform%3E%0A%20%20%3Cdiv%20class%3D%22form%2Dgroup,primary%22%3ESubmit%3C/button%3E%0A%3C/form%3E)
    - Create `editabout.html`
        ```html
        {% extends 'index.html' %}

        {% block content %}
        <div class="container mt-5">
            <form action="{% url 'updateabout' %}" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">ID</label>
                    <input type="text" class="form-control" name= "myid" value="{{about.id}}" id="exampleInput" aria-describedby="emailHelp" readonly>
                </div>
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Current Image</label><br>
                    <img src="/{{about.Profile_img}}" alt="" width="50"><br>
                </div>
                <div class="form-group">
                    <label for="exampleFormControlFile1">Update Image</label>
                    <input type="file" name="profile_img" class="form-control-file" id="exampleFormControlFile1">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Name</label>
                <input type="text" class="form-control" name= "name" value="{{about.Name}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession 1</label>
                <input type="text" class="form-control" name="profession1" value="{{about.Profession1}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession 2</label>
                <input type="text" class="form-control" name="profession2" value="{{about.Profession2}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession 3</label>
                <input type="text" class="form-control" name="profession3" value="{{about.Profession3}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">About details</label>
                <textarea class="form-control" name="about_details" name="about_details" id="exampleFormControlTextarea1" rows="3">{{about.About_details}}</textarea>
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession title 1</label>
                <input type="text" class="form-control" name="profession_title1" value="{{about.Profession_title1}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession title 2</label>
                <input type="text" class="form-control" name="profession_title2" value="{{about.Profession_title2}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession details</label>
                <textarea class="form-control" name="profession_details" name="profession_details" id="exampleFormControlTextarea1" rows="3">{{about.Profession_details}}</textarea>
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession Paragraph</label>
                <textarea class="form-control" name="profession_para"  id="exampleFormControlTextarea1" rows="3">{{about.Profession_para}}</textarea>
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Birthday</label>
                <input type="text" class="form-control" name="birthday" value="{{about.Birthday}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Website</label>
                <input type="text" class="form-control" name="website" value="{{about.Website}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Phone</label>
                <input type="text" class="form-control" name="phone" value="{{about.Phone}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">City</label>
                <input type="text" class="form-control" name="city" value="{{about.City}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Age</label>
                <input type="text" class="form-control" name="age" value="{{about.Age}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email</label>
                <input type="email" class="form-control" name="email" value="{{about.Email}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Freelance status</label>
                <input type="text" class="form-control" name="freelance_status" value="{{about.Freelance_status}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
        {% endblock content %}
        ```
        - Here `action`, `method`, `enctype`, `name` & `value` must be included
    - Now render this html page in `views.py`
        ```python
        def editabout(request, myid):
            about = AboutModel.objects.get(id=myid)
            myDict={
                'about':about
            }
            return render(request,'editabout.html',myDict)
        ```
    - Set the path url in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from portfolio.views import portfolio,editabout,updateabout

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',portfolio,name='portfolio'),
            path('editabout/<str:myid>',editabout,name='editabout'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now to make it work create a button under edit section of html page so after clicking it the form will be open
        ```html
        <a href="{% url 'editabout' about.id %}" type="button" class="btn mt-2" style="background-color: #173b6c; color: #fff;">Edit About</a>
        ```
    - Create a `updateabout` function in `views.py`
        ```python
        def updateabout(request):
            if request.method=="POST":
                myid = request.POST.get('myid')
                profile_img = request.FILES.get('profile_img')
                name=request.POST.get('name')
                profession1=request.POST.get('profession1')
                profession2=request.POST.get('profession2')
                profession3=request.POST.get('profession3')
                about_details=request.POST.get('about_details')
                profession_title1=request.POST.get('profession_title1')
                profession_title2=request.POST.get('profession_title2')
                profession_details=request.POST.get('profession_details')
                profession_para=request.POST.get('profession_para')
                birthday=request.POST.get('birthday')
                website=request.POST.get('website')
                phone=request.POST.get('phone')
                city=request.POST.get('city')
                age=request.POST.get('age')
                email=request.POST.get('email')
                freelance_status=request.POST.get('freelance_status')
                if profile_img:  
                    about = AboutModel(
                        id = myid,
                        Profile_img = profile_img,
                        Name=name,
                        Profession1=profession1,
                        Profession2=profession2,
                        Profession3=profession3,
                        About_details=about_details,
                        Profession_title1=profession_title1,
                        Profession_title2=profession_title2,
                        Profession_details=profession_details,
                        Profession_para=profession_para,
                        Birthday=birthday,
                        Website=website,
                        Phone=phone,
                        City=city,
                        Age=age,
                        Email=email,
                        Freelance_status=freelance_status,
                    )
                else:
                    aboutbyid=AboutModel.objects.get(id=myid)
                    about = AboutModel(
                        id = myid,
                        Profile_img = aboutbyid.Profile_img,
                        Name=name,
                        Profession1=profession1,
                        Profession2=profession2,
                        Profession3=profession3,
                        About_details=about_details,
                        Profession_title1=profession_title1,
                        Profession_title2=profession_title2,
                        Profession_details=profession_details,
                        Profession_para=profession_para,
                        Birthday=birthday,
                        Website=website,
                        Phone=phone,
                        City=city,
                        Age=age,
                        Email=email,
                        Freelance_status=freelance_status,
                    )
                about.save()
                return redirect('/')
        ```
        - Here image also handle when user don't update image
        - after updating it will redirect to homepage
        - This function will be trigger after clicking on submit button which is in form page action
### Task
- Complete remaining CRUD operation in Custom Template

</details>

<details>
<summary>Day-19-Lab Exam 03 (18-04-2024)</summary>

## Day 19 Topics:
- Lab Exam 03
- PDF download using js (Test code)
- Bonus task: PDF download implementation

### Lab Exam 03
> Question: Building a Resume Builder Web Application with Django You are tasked with creating a simple Resume Builder web application using Django.The application should allow users to cease, view, update, and delete their resumes, Including various fields such as profile picture, address, phone number, career objective, and others. Your task is to Implement the CRUD (Create, Read, Update, Delete) operations for managing resumes.

Resume Creation:
- Profile picture
- Full name
- Address
- Phone number
- Email address
- Career objective
- Education history (e.g., degree, Institution, graduation year)
- Work experience (e.g., company, position, start and end dates)
- Skills (Hard Skills, Soft Skills)
- Certifications
- Projects
- References, etc.

Listing Resumes:
- Display a list of all resumes

Viewing and Editing Resumes:
- View the details of a specific resume.
Provide options to edit and update the information within the resume.

Deleting Resumes:
- Implement functionality to delete resumes when required.

Bonus (optional):
- Add the ability for users to upload and manage multiple profile pictures.
- Implement search and filtering functionality for resumes.
- Allow users to download their resumes in PDF format.
- Implement rich text editors for fields like career objective and project descriptions. 

Requirements: 
- Use Django models to define the resume structure.
- Create clean and responsive templates for the user Interface.

Submission: 
- Submit the project as a zip file or provide a link to a version control repository GitHub. Include a README file with instructions and any necessary dependencies. 

> Total time took by me 1 Hour 40 Minutes.

### PDF download using js (Test code)
- Below code was done to test how to generate pdf with js
    ```html
    <!--CDN:--> 
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.3.2/jspdf.debug.js"></script>

    <script>
        document.getElementById("downloadPDF").addEventListener("click", function() {
            // Create a new instance of jsPDF
            const doc = new jsPDF();
        
            // Add profile section
            doc.text("Profile", 10, 10);
            doc.text("Name: " + "{{ resume.Full_name }}", 10, 20);
            doc.text("Address: " + "{{ resume.Address }}", 10, 30);
            doc.text("Phone: " + "{{ resume.Phone_number }}", 10, 40);
            doc.text("Email: " + "{{ resume.Email_address }}", 10, 50);
        
            // Add career objective section
            doc.text("Career Objective", 10, 70);
            doc.text("{{ resume.Career_objective }}", 10, 80);
            
            // Add education section
            doc.text("Education", 10, 100);
            doc.text("{{ education.Degree }} - {{ education.Institution }}, {{ education.Graduation_year }}", 10, 110);
            
            // Add work experience section
            doc.text("Work Experience", 10, 130);
            doc.text("{{ work.Position }} at {{ work.Company }}, {{ work.Start_date }} - {{ work.End_date }}", 10, 140);
            
            // Add skills section
            doc.text("Skills", 10, 160);
            doc.text("Hard Skills: {{ resume.Hard_skills }}", 10, 170);
            doc.text("Soft Skills: {{ resume.Soft_skills }}", 10, 180);
            
            // Add certifications section
            doc.text("Certifications", 10, 200);
            doc.text("{{ resume.Certifications }}", 10, 210);
            
            // Add projects section
            doc.text("Projects", 10, 230);
            doc.text("{{ resume.Projects }}", 10, 240);
            
            // Add references section
            doc.text("References", 10, 260);
            doc.text("{{ resume.References }}", 10, 270);
        
            // Save the PDF
            doc.save("resume.pdf");
        });
    </script>
    ```

### Bonus task: PDF download implementation
- I found a package in python which is `pyhtml2pdf` which i used to convert the created resume in pdf. Below function was implemented to download the generated pdf file:
    ```python
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
    ```

</details>

<details>
<summary>Day-20-Python Basic Day 04 & Lab Exam 03 Portfolio Project Recap (20-04-2024)</summary>

## Day 20 Topics:

- Arithmetic operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Conditions and If statements
- Lab exam 03 portfolio project recap
- Task

### Arithmetic operators

|Operator|	Name|	Example|
|-       | -    |      -   |
|+	|Addition	| x + y |	
|-	|Subtraction|	x - y |	
|*	|Multiplication	| x * y |	
|/	|Division|	x / y |	
|%	|Modulus	| x % y	|
|**	|Exponentiation|	x ** y |	
|//	|Floor division|	x // y |


### Assignment Operators
- Task
    - a/=10
        > a=a/10
    - a+=b+10
        > a=a/10
    - a**=3+c
        > a=a**(3+c)
    - a//=x+y**4
        > a=a//(x+(y**4))
    - b-=x**y
        > b=b-(x**y)

### Comparison Operators

|Operator	|Name|	Example|
|    -      |  - |     -    |        
|==	|Equal|	 x == y |	
|!=	|Not equal	| x != y	|
|>	|Greater than|	x > y |	
|<	|Less than	| x < y |	
|>=	|Greater than or equal to|	x >= y |	
|<=	|Less than or equal to	| x <= y |

- Task
    - x= 5
    - y = 3
    - print(x==y)
        > z =(x==y)
        
        > print(z)

### Logical Operators

|Operator	|Description	|Example|
|-|-|-|
|and 	|Returns True if both statements are true	|x < 5 and  x < 10	|
|or	|Returns True if one of the statements is true|	x < 5 or x < 4	|
|not	|Reverse the result, returns False if the result is true	|not(x < 5 and x < 10)|

### Conditions and If statements

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

### Lab exam 03 portfolio project recap
> Question: Building a Resume Builder Web Application with Django You are tasked with creating a simple Resume Builder web application using Django.The application should allow users to cease, view, update, and delete their resumes, Including various fields such as profile picture, address, phone number, career objective, and others. Your task is to Implement the CRUD (Create, Read, Update, Delete) operations for managing resumes.

Resume Creation:
- Profile picture
- Full name
- Address
- Phone number
- Email address
- Career objective
- Education history (e.g., degree, Institution, graduation year)
- Work experience (e.g., company, position, start and end dates)
- Skills (Hard Skills, Soft Skills)
- Certifications
- Projects
- References, etc.

Listing Resumes:
- Display a list of all resumes

Viewing and Editing Resumes:
- View the details of a specific resume.
Provide options to edit and update the information within the resume.

Deleting Resumes:
- Implement functionality to delete resumes when required.

Bonus (optional):
- Add the ability for users to upload and manage multiple profile pictures.
- Implement search and filtering functionality for resumes.
- Allow users to download their resumes in PDF format.
- Implement rich text editors for fields like career objective and project descriptions. 

Requirements: 
- Use Django models to define the resume structure.
- Create clean and responsive templates for the user Interface.

Submission: 
- Submit the project as a zip file or provide a link to a version control repository GitHub. Include a README file with instructions and any necessary dependencies.

### Solution
- Initial setup:
    - Create Project : `django-admin startproject resumeProject`
    - Create App: `py manage.py startapp resumeApp`
    - Migrate Database: `py manage.py migrate`
    - Modification in `settings.py`:
        - Add app name `resumeApp` in `settings.py`'s `INSTALLED_APPS`:
            ```python
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'resumeApp',
            ]
            ```
        - Add static file path at the end of the `settings.py` file:
            ```python
            STATICFILES_DIRS = [
                BASE_DIR / "static",
            ]
            ```
        - Add template path in `TEMPLATES`
            ```python
            'DIRS': [BASE_DIR,'templates'],
            ```
    - Now create a folder and name it exactly as added in `TEMPLATES`'s `DIRS` which is `templates` In project directory:
        ```text
        project_name/ # Which is resumeProject
        │
        ├── manage.py
        ├── project_name/ # resumeProject
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── asgi.py
        │   ├── urls.py
        │   └── wsgi.py
        │   └── views.py # This is created manually
        │
        ├── templates # This folder is created manually
        │
        ├── static # This folder is created manually
        │
        └── app_name/ # Which is resumeApp
            ├── migrations/
            │   └── __init__.py
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── tests.py
            └── views.py
        ```
- Now let's begin with first task which is **Listing Resumes**
    - To do this let's create our `base.html`, `navbar.html`, `home.html`,  files. 
    - Here: 
        - `base.html` :- For our base structure of the template 
        - `navbar.html` :- This will be included in `base.html`
        - `home.html` :-  Now this will extends `base.html` and show it's own content in block; As per requirement we will list all the resume in table data list in the block content of `home.html`
    - Let's create the required models in our app directory `models.py`
        ```python
        from django.db import models

        # Create your models here.
        class ResumeModel(models.Model):
            Profile_picture=models.ImageField(upload_to='media/ProfilePic')
            Full_name=models.CharField(max_length=100)
            Address=models.CharField(max_length=100)
            Phone_number=models.CharField(max_length=100)
            Email_address=models.CharField(max_length=100)
            Career_objective=models.TextField()
            Hard_Skills=models.CharField(max_length=100)
            Soft_Skills=models.CharField(max_length=100)
            Certifications=models.CharField(max_length=100)
            Projects=models.CharField(max_length=100)
            References=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Full_name
            
        class ResumeEducationModel(models.Model):
            Degree=models.CharField(max_length=100)
            Institution=models.CharField(max_length=100)
            Graduation_year=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Institution
            
        class ResumeWorkModel(models.Model):
            Company=models.CharField(max_length=100)
            Position=models.CharField(max_length=100)
            Start_dates=models.CharField(max_length=100)
            End_dates =models.CharField(max_length=100)
            
            def __str__(self):
                return self.Company
        ```
    - In `admin.py` we have to register it
        ```python
        from django.contrib import admin
        from resumeApp.models import ResumeModel,ResumeEducationModel,ResumeWorkModel
        # Register your models here.

        admin.site.register(ResumeModel)
        admin.site.register(ResumeEducationModel)
        admin.site.register(ResumeWorkModel)
        ```
    - Now as we have done changes in model so we have to migrate it;
        - `py manage.py makemigrations`
        - `py manage.py migrate`
    - Run the server `py manage.py runserver`
    - Now add some data from admin page so that we can show it in frontend
    -  Let's setup our template pages
    - `base.html`:
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Resume Builder</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body>
            {% include 'navbar.html' %}
            
            {% block content %}
                
            {% endblock content %}
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
        </html>
        ```
        - Here we can see we have also added bootstrap cdn as we are using bootstrap to build our project.
    - `navbar.html`:
        ```html
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'home' %}">Resume Builder</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'home' %}">All Resume</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'addresume' %}">Add Resume</a>
                </li>
                </ul>
            </div>
            </div>
        </nav>
        ```
        - Here we have two navigation `All Resume`,  `Add Resume` & a default one which is navigating to home page `Resume Builder`.
    - Now the page we are going to show the list of all resumes which is `home.html`
        ```html
        {% extends 'base.html' %}

        {% block content %}
            <table class="table">
                <thead>
                <tr>
                    <th scope="col">Profile picture</th>
                    <th scope="col">Full name</th>
                    <th scope="col">Address</th>
                    <th scope="col">Phone number</th>
                    <th scope="col">Action</th>
                </tr>
                </thead>
                
                {% for i in resumedata %}
                <tbody>
                <tr>
                    <td>
                    <img src="/{{i.Profile_picture}}" width="50px" alt="">
                    </td>
                    <td>{{i.Full_name}}</td>
                    <td>{{i.Address}}</td>
                    <td>{{i.Phone_number}}</td>
                    <td>
                    <a href="{% url 'deleteresume' i.id %}">Delete</a>
                    <a href="{% url 'editresume' i.id %}">Edit</a>
                    <a href="{% url 'viewresume' i.id %}">View</a>
                    </td>
                </tr>
                </tbody>
                {% endfor %}
                
            </table>
        {% endblock content %}
        ```
        - We can see there is a for loop, which is working because we have done some work in `views.py` which we have to create in project directory manually:
            ```python
            from django.shortcuts import render,redirect
            from resumeApp.models import ResumeModel,ResumeEducationModel,ResumeWorkModel

            def home(request):
                resumedata=ResumeModel.objects.all()
                educationdata=ResumeEducationModel.objects.all()
                workdata=ResumeWorkModel.objects.all()
                
                resume={
                    'resumedata':resumedata,
                    'educationdata':educationdata,
                    'workdata':workdata,
                }
                return render(request,'home.html',resume)
            ```
        - In `urls.py` we have to add the path route
            ```python
            from django.contrib import admin
            from django.urls import path
            from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('',home,name='home'),
            ]
            ```
- We added the data from django admin page , So now let's add it from frontend
    - First create a html page `addresume.html` and add bootstrap form 
        ```html
        {% extends 'base.html' %}


        {% block content %}
        <div class="container">
            <form action="{% url 'addresume' %}" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profile Picture</label>
                <input type="file" class="form-control" id="exampleInputEmail1" name="profile_picture" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Full name</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="full_name" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Address</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="address" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Phone number</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="phone_number" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="email_address" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Career objective</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="career_objective" aria-describedby="emailHelp">
                </div>
                <h4>Education history:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Degree</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="degree" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Institution</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="institution" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Graduation_year</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="graduation_year" aria-describedby="emailHelp">
                </div>
                <h4>Work experience:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Company</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="company" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Position</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="position" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Start dates</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="start_dates" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">End dates</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="end_dates" aria-describedby="emailHelp">
                </div>
                <h4>Skills:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Hard Skills</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="hard_Skills" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Soft Skills</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="soft_Skills" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Certifications</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="certifications" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Projects</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="projects" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">References</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="references" aria-describedby="emailHelp">
                </div>

                <button type="submit" class="btn btn-primary">Submit</button>
            </form>

        </div>
        {% endblock content %}
        ```
        - Here `action`,`method`,`enctype` and the html `name` attribute is important
    - Now create a function which we included in action
        ```python
        def addresume(request):
            if request.method=="POST":
                profile_picture=request.FILES.get('profile_picture')
                full_name=request.POST.get('full_name')
                address=request.POST.get('address')
                phone_number=request.POST.get('phone_number')
                email_address=request.POST.get('email_address')
                career_objective=request.POST.get('career_objective')
                hard_Skills=request.POST.get('hard_Skills')
                soft_Skills=request.POST.get('soft_Skills')
                certifications=request.POST.get('certifications')
                projects=request.POST.get('projects')
                references=request.POST.get('references')
                degree=request.POST.get('degree')
                institution=request.POST.get('institution')
                graduation_year=request.POST.get('graduation_year')
                company=request.POST.get('company')
                position=request.POST.get('position')
                start_dates=request.POST.get('start_dates')
                end_dates=request.POST.get('end_dates')
                
                resume=ResumeModel(
                    Profile_picture=profile_picture,
                    Full_name=full_name,
                    Address=address,
                    Phone_number=phone_number,
                    Email_address=email_address,
                    Career_objective=career_objective,
                    Hard_Skills=hard_Skills,
                    Soft_Skills=soft_Skills,
                    Certifications=certifications,
                    Projects=projects,
                    References=references,
                )
                education=ResumeEducationModel(
                    Degree=degree,
                    Institution=institution,
                    Graduation_year=graduation_year,
                )
                work=ResumeWorkModel(
                    Company=company,
                    Position=position,
                    Start_dates=start_dates,
                    End_dates=end_dates,
                    
                )
                resume.save()
                education.save()
                work.save()
                
                return redirect('home')
                
            return render(request,'addresume.html')
        ```
    - Now add the url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
        - Here MEDIA static url added so that image related task work properly
    - Now in `navbar.html` url will be added in `href`
        ```html
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'addresume' %}">Add Resume</a>
          </li>
        ```
- Now let's do the delete action
    - First create a function with id in parameter as we need specific id to delete it
        ```python
        def deleteresume(request,myid):
            resumedata=ResumeModel.objects.get(id=myid)
            educationdata=ResumeEducationModel.objects.get(id=myid)
            workdata=ResumeWorkModel.objects.get(id=myid)
            
            resumedata.delete()
            educationdata.delete()
            workdata.delete()
            return redirect('home')
        ```
    - Create url route path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now in table :
        ```html
            <td>
              <a href="{% url 'deleteresume' i.id %}">Delete</a>
            </td>
        ```
- Now let's edit and update the data
    - first create a form as same as `addresume.html` page which is `editresume.html`
        ```html
        {% extends 'base.html' %}


        {% block content %}
        <div class="container">
            <form action="{% url 'updateresume' %}" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">ID</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.id}}" name="myid" aria-describedby="emailHelp" readonly>
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Current Profile Picture:</label> <br>
                <img src="/{{resumedata.Profile_picture}}" width="50px" alt=""><br>
                <input type="file" class="form-control" id="exampleInputEmail1" name="profile_picture" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Full name</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Full_name}}" name="full_name" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Address</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Address}}" name="address" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Phone number</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Phone_number}}" name="phone_number" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Email_address}}" name="email_address" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Career objective</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Career_objective}}" name="career_objective" aria-describedby="emailHelp">
                </div>
                <h4>Education history:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Degree</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{educationdata.Degree}}" name="degree" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Institution</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{educationdata.Institution}}" name="institution" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Graduation_year</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{educationdata.Graduation_year}}" name="graduation_year" aria-describedby="emailHelp">
                </div>
                <h4>Work experience:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Company</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{workdata.Company}}" name="company" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Position</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{workdata.Position}}" name="position" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Start dates</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{workdata.Start_dates}}" name="start_dates" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">End dates</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{workdata.End_dates}}" name="end_dates" aria-describedby="emailHelp">
                </div>
                <h4>Skills:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Hard Skills</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Hard_Skills}}" name="hard_Skills" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Soft Skills</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Soft_Skills}}" name="soft_Skills" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Certifications</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Certifications}}" name="certifications" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Projects</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Projects}}" name="projects" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">References</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.References}}" name="references" aria-describedby="emailHelp">
                </div>

                <button type="submit" class="btn btn-primary">Update</button>
            </form>

        </div>
        {% endblock content %}
        ```
        - Here difference between add page is the action which is for updating after clicking on update.
        - Value attribute for seeing the current data 
    - Now create a function for this page to show
        ```python
        def editresume(request,myid):
            resumedata=ResumeModel.objects.get(id=myid)
            educationdata=ResumeEducationModel.objects.get(id=myid)
            workdata=ResumeWorkModel.objects.get(id=myid)
            
            resume={
                'resumedata':resumedata,
                'educationdata':educationdata,
                'workdata':workdata,
            }
            return render(request,'editresume.html',resume)
        ```
        - Here we first the created `editresume.html` page 
        - As we need id so that we can show the current data of that specific person
        - and finally we return the model data as dictionary
    - Now in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
            path('editresume/<str:myid>',editresume,name='editresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
        - As we can see there is the id 
    - Now in action 
        ```html
            <td>
              <a href="{% url 'editresume' i.id %}">Edit</a>
            </td>
        ```
        - So after clicking on it it will open that specific id's data for editing
    - Now to make the update button work we have to create a update function as below:
        ```python
        def updateresume(request):
            if request.method=="POST":
                myid=request.POST.get('myid')
                profile_picture=request.FILES.get('profile_picture')
                full_name=request.POST.get('full_name')
                address=request.POST.get('address')
                phone_number=request.POST.get('phone_number')
                email_address=request.POST.get('email_address')
                career_objective=request.POST.get('career_objective')
                hard_Skills=request.POST.get('hard_Skills')
                soft_Skills=request.POST.get('soft_Skills')
                certifications=request.POST.get('certifications')
                projects=request.POST.get('projects')
                references=request.POST.get('references')
                degree=request.POST.get('degree')
                institution=request.POST.get('institution')
                graduation_year=request.POST.get('graduation_year')
                company=request.POST.get('company')
                position=request.POST.get('position')
                start_dates=request.POST.get('start_dates')
                end_dates=request.POST.get('end_dates')
                
                if profile_picture:
                    resume=ResumeModel(
                        id=myid,
                        Profile_picture=profile_picture,
                        Full_name=full_name,
                        Address=address,
                        Phone_number=phone_number,
                        Email_address=email_address,
                        Career_objective=career_objective,
                        Hard_Skills=hard_Skills,
                        Soft_Skills=soft_Skills,
                        Certifications=certifications,
                        Projects=projects,
                        References=references,
                    )
                    education=ResumeEducationModel(
                        id=myid,
                        Degree=degree,
                        Institution=institution,
                        Graduation_year=graduation_year,
                    )
                    work=ResumeWorkModel(
                        id=myid,
                        Company=company,
                        Position=position,
                        Start_dates=start_dates,
                        End_dates=end_dates,
                        
                    )
                else:
                    resumebyid=ResumeModel.objects.get(id=myid)
                    resume=ResumeModel(
                        id=myid,
                        Profile_picture=resumebyid.Profile_picture,
                        Full_name=full_name,
                        Address=address,
                        Phone_number=phone_number,
                        Email_address=email_address,
                        Career_objective=career_objective,
                        Hard_Skills=hard_Skills,
                        Soft_Skills=soft_Skills,
                        Certifications=certifications,
                        Projects=projects,
                        References=references,
                    )
                    education=ResumeEducationModel(
                        id=myid,
                        Degree=degree,
                        Institution=institution,
                        Graduation_year=graduation_year,
                    )
                    work=ResumeWorkModel(
                        id=myid,
                        Company=company,
                        Position=position,
                        Start_dates=start_dates,
                        End_dates=end_dates,
                        
                    )
                resume.save()
                education.save()
                work.save()
            return redirect('home')
        ```
        - This function also handle the `None` image 
        - As we are updating the values withing a model so id is playing very important role here, if we don't do that we will create a new table data rather than updating.
        - finally we save it and redirect to home page.
    - Add the url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
            path('editresume/<str:myid>',editresume,name='editresume'),
            path('updateresume/',updateresume,name='updateresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
- Now let's view the resume we created 
    - We will need a good template for that , gpt will be very helpful in this part. Create a `viewresume.html`
        ```html
        {% extends 'base.html' %}

        {% block content %}
        <style>
            /* Custom styles */
            body {
                background-color: #f8f9fa;
                color: #343a40;
            }
            .section-title {
                color: #007bff;
            }
            .section-heading {
                color: #28a745;
            }
            .profile-picture {
                border-radius: 50%;
                border: 5px solid #17a2b8;
                max-width: 200px;
                height: auto;
            }
            .list-group-item {
                background-color: #f1f1f1;
                border-color: #dee2e6;
            }
        </style>
        <div class="container mt-5">
            <div class="row">
                <div class="col-md-4">
                    <img src="/{{ resumedata.Profile_picture }}" class="img-fluid profile-picture" alt="Profile Picture">
                </div>
                <div class="col-md-8">
                    <h1 class="section-heading">{{ resumedata.Full_name }}</h1>
                    <p><strong>Address:</strong> {{ resumedata.Address }}</p>
                    <p><strong>Phone:</strong> {{ resumedata.Phone_number }}</p>
                    <p><strong>Email:</strong> {{ resumedata.Email_address }}</p>
                    <hr>
                    <h3 class="section-title">Career Objective</h3>
                    <p>{{ resumedata.Career_objective }}</p>
                </div>
            </div>
            <hr>
            <div class="row mt-4">
                <div class="col-md-6">
                    <h3 class="section-title">Education</h3>
                    <ul class="list-group">
                        <li class="list-group-item">{{ educationdata.Degree }} - {{ educationdata.Institution }} ({{ educationdata.Graduation_year }})</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h3 class="section-title">Work Experience</h3>
                    <ul class="list-group">
                        <li class="list-group-item">{{ workdata.Position }} at {{ workdata.Company }} ({{ workdata.Start_dates }} - {{ workdata.End_dates }})</li>
                    </ul>
                </div>
            </div>
            <hr>
            <div class="row mt-4">
                <div class="col-md-6">
                    <h3 class="section-title">Hard Skills</h3>
                    <p>{{ resumedata.Hard_Skills }}</p>
                </div>
                <div class="col-md-6">
                    <h3 class="section-title">Soft Skills</h3>
                    <p>{{ resumedata.Soft_Skills }}</p>
                </div>
            </div>
            <hr>
            <div class="row mt-4">
                <div class="col-md-6">
                    <h3 class="section-title">Certifications</h3>
                    <p>{{ resumedata.Certifications }}</p>
                </div>
                <div class="col-md-6">
                    <h3 class="section-title">Projects</h3>
                    <p>{{ resumedata.Projects }}</p>
                </div>
            </div>
            <hr>
            <div class="row mt-4">
                <div class="col-md-12">
                    <h3 class="section-title">References</h3>
                    <p>{{ resumedata.References }}</p>
                </div>
            </div>
        </div>
        {% endblock content %}
        ```
    - Now create a function for this html page to view
        ```python
        def viewresume(request,myid):
            resumedata=ResumeModel.objects.get(id=myid)
            educationdata=ResumeEducationModel.objects.get(id=myid)
            workdata=ResumeWorkModel.objects.get(id=myid)
            
            resume={
                'resumedata':resumedata,
                'educationdata':educationdata,
                'workdata':workdata,
            }
            return render(request,'viewresume.html',resume)
        ```
    - Create url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
            path('editresume/<str:myid>',editresume,name='editresume'),
            path('updateresume/',updateresume,name='updateresume'),
            path('viewresume/<str:myid>',viewresume,name='viewresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now in action 
        ```html
            <td>
              <a href="{% url 'viewresume' i.id %}">View</a>
            </td>
        ```
- We have done all the required CRUD operation in this Portfolio project

> Bonus Task solution not included here
### Task
- Do full lab-3 project video and submit

</details>

<details>
<summary>Day-21-Python Basic Day 05 & Job Portal Project Part 01 (21-04-2024)</summary>
    
## Day 21 Topics:
- Python Basics Day 04 recap
- Nested If else
- Simple problem solving using only if..else
- Job Portal Project Part 01 (Using AbstractUser)

### Simple problem solving using only if..else
> Problem-01: x,y,z who is greater
```python
x=10
y=20
z=30

if x>y:
    if x>z:
        print("x is greater")
    else:
        print("z is greater")
else:
    if y>x:
        if y>z:
            print("y is greater")
        else:
            print("z is greater")
```
> Problem-02: w,x,y,z who is greater
```python
w=10
x=20
y=30
z=40

if w>x:
    if w>y:
        if w>z:
            print("w is greater")
        else:
            print("z is greater")
    else:
        if y>z:
            print("y is greater")
        else:
            print("z is greater")
else:
    if x>y:
        if x>z:
            print("x is greater")
        else:
            print("z is greater")
    else:
        if y>z:
            print("y is greater")
        else:
            print("z is greater")
```
> Problem-03: write the output of below code
```python
a=100
b=300
c=0
c=a
a=b
b=c
c=0
if c:
    print("Hello")
else:
    print(f"Value of a = {a} and value of b = {b}")
```

### Job Portal Project Part 01 (Using AbstractUser)
- Create project and app as usual way
- Create a signup page `signuppage.html`:
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Signup Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            
            .container {
                max-width: 400px;
                margin: 50px auto;
                background-color: #fff;
                border-radius: 5px;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            
            h2 {
                text-align: center;
            }
            
            label {
                display: block;
                margin-bottom: 5px;
            }
            
            input[type="text"],
            input[type="password"],
            input[type="email"],
            select {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            
            input[type="submit"] {
                width: 100%;
                background-color: #4caf50;
                color: #fff;
                padding: 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Signup</h2>
            <form action="#" method="POST">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" placeholder="Enter your username" required>
                
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
                
                <label for="confirm_password">Confirm Password:</label>
                <input type="password" id="confirm_password" name="confirm_password" placeholder="Confirm your password" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
                
                <label for="user_type">User Type:</label>
                <select id="user_type" name="user_type" required>
                    <option value="" disabled selected>Select User Type</option>
                    <option value="job_seeker">Job Seeker</option>
                    <option value="job_recruiter">Job Recruiter</option>
                </select>
                
                <input type="submit" value="Sign Up">
            </br>
            </br>
                <a href="{% url 'signinpage' %}">Already have an account?</a>
            </form>
        </div>
    </body>
    </html>
    {% endblock content %}
    ```
    - Create function for signin:
        ```python
        from django.shortcuts import render, redirect

        def signuppage(request):
            return render(request,'signuppage.html')

        ```
    - Create url path
        ```python
        from django.contrib import admin
        from django.urls import path
        from jobportalProject.views import signuppage

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signuppage/',signuppage,name='signuppage'),
        ]
        ```
- Now create a signin page `signinpage.html`
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Signup Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            
            .container {
                max-width: 400px;
                margin: 50px auto;
                background-color: #fff;
                border-radius: 5px;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            
            h2 {
                text-align: center;
            }
            
            label {
                display: block;
                margin-bottom: 5px;
            }
            
            input[type="text"],
            input[type="password"],
            input[type="email"],
            select {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            
            input[type="submit"] {
                width: 100%;
                background-color: #4caf50;
                color: #fff;
                padding: 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Signup</h2>
            <form action="#" method="POST">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" placeholder="Enter your username" required>
                
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
                <input type="submit" value="Sign In">
            </br>
            </br>
                <a href="{% url 'signuppage' %}">Don't have an account?</a>
            </form>
        </div>
    </body>
    </html>
    {% endblock content %}

    ```
    - Create function for the singinpage
        ```python
        from django.shortcuts import render, redirect

        def signinpage(request):
            return render(request,'signinpage.html')
        ```
    - Add url path:
        ```python
        from django.contrib import admin
        from django.urls import path
        from jobportalProject.views import signuppage,signinpage

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signuppage/',signuppage,name='signuppage'),
            path('',signinpage,name='signinpage'),
        ]
        ```
- Now new changes:
    - Create class of `AbstractUser` in `models.py`
        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser

        # Create your models here.
        class CustomUserModel(AbstractUser):
            USER=[
                ('recruiter','Recruiter'),
                ('jobseeker','JobSeeker'),
            ]
            user_type=models.CharField(choices=USER,max_length=100)
            user_name = models.CharField(max_length=100)
            display_name=models.CharField(max_length=100)
            email=models.CharField(max_length=100)
            password=models.EmailField(max_length=100)
            confirm_password=models.CharField(max_length=100)

            def __str__(self):
                return self.user_name
        ```
        - Here `CustomUserModel(AbstractUser)` is new, where we created the model.
    - In `admin.py`
        ```python
        from django.contrib import admin
        from jobportalApp.models import CustomUserModel

        # Register your models here.
        class Custom_User_Display(admin.ModelAdmin):
            list_display=['display_name','user_name','email']

        admin.site.register(CustomUserModel,Custom_User_Display)
        ```
        - Here we did some modification before registering the model.
        - The modification is done to display the model data properly in custom way
    - Changes in `settings.py` where we have to include the Auth user model in end line
        ```python
        AUTH_USER_MODEL='jobportalApp.CustomUserModel' # here appname.created_model_name
        ```
    - Now we will migrate our database and create the sueruser:
        - `py manage.py makemigrations jobportalApp`
        - `py manage.py migrate jobportalApp`
        - `py manage.py migrate`
        - `py manage.py makemigrations`
        - `py manage.py createsuperuser`
    - Now we will be able to add new data in our created model

</details>

<details>
<summary>Day-22-Job Portal Project Part 02 (22-04-2024)</summary>

## Day 22 Topics:
- Day 21 recap
- Job Portal Project Part 02 (Signup)

### Job Portal Project Part 02 (Signup)
- Modify in `settings.py`
    - Add app in installed app
    - Add template path
    - Add static path
    - Add `AUTH_USER_MODEL`
- Creating model:
    - As we are creating custom model from AbstractUser where many common thing already defined, So we will add only things that are uncommon are not include in AbstractUser:
        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser
        # Create your models here.
        class CustomUserModel(AbstractUser):
            USER=[
                ('recruiter','Recruiter'),
                ('seeker','Seeker'),
            ]
            BLOOD_GROUP=[
                ('A+', 'A positive'),
                ('A-', 'A negative'),
                ('B+', 'B positive'),
                ('B-', 'B negative'),
                ('AB+', 'AB positive'),
                ('AB-', 'AB negative'),
                ('O+', 'O positive'),
                ('O-', 'O negative'),
            ]

            fname=models.CharField(max_length=100)
            lname=models.CharField(max_length=100)
            profile_picture=models.ImageField(upload_to='media/profilePic')
            # date_of_birth=models.DateField(auto_now=True)
            date_of_birth=models.DateField(auto_now_add=True)
            address=models.CharField(max_length=100)
            blood_group=models.CharField(choices=BLOOD_GROUP,max_length=100)
            usertype=models.CharField(choices=USER,max_length=100)

            def __str__(self):
                return self.fname
        ```
        - Here `DateField` field is `auto_now_add=True` which will take the date and save it, if it is set as `auto_now=True` then it will save the current date
    - Register the Model
        ```python
        from django.contrib import admin
        from jobportalApp.models import CustomUserModel
        # Register your models here.

        class Custom_User_Display(admin.ModelAdmin):
            list_display=['fname','usertype','blood_group','date_of_birth']

        admin.site.register(CustomUserModel,Custom_User_Display)
        ```
        - Here `Custom_User_Display` class is used to show some of the selected column in admin page in table structure
    - Now let's do the database migrate
        > Execute below command one by one
        - `py manage.py makemigrations jobportalApp`
        - `py manage.py migrate jobportalApp`
        - `py manage.py migrate`
        - `py manage.py makemigrations`
        - `py manage.py createsuperuser`
    - Now we can add model data 
- To add it from frontend page we will create a `signup.html` page
    ```html
    {% extends 'base.html' %}


    {% block content %}
    <form action="{% url 'signup' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
        <label for="name">First Name:</label><br>
        <input type="text" id="name" name="fname" required><br><br>
        <label for="name">Last Name:</label><br>
        <input type="text" id="name" name="lname" required><br><br>
        <label for="name">User Name:</label><br>
        <input type="text" id="name" name="username" required><br><br>
    
        <label for="username">Profile Picture:</label><br>
        <input type="file" id="username" name="profile_picture" required><br><br>
        <label for="date_of_birth">Date of Birth:</label><br>
        <input type="date" id="date_of_birth" name="date_of_birth" required><br><br>
        

        <label for="usertype">Blood Group:</label><br>
        <select id="usertype" name="blood_group" required>
        <option value="" disabled selected>Please select an option</option>
        <option value="A+">A+</option>
        <option value="A-">A-</option>
        <option value="B+">B+</option>
        <option value="B-">B-</option>
        <option value="AB+">AB+</option>
        <option value="AB-">AB-</option>
        <option value="O+">O+</option>
        <option value="O-">O-</option>
    </select><br><br>
    
        <label for="email">Address:</label><br>
        <input type="text" id="email" name="address" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
    
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
    
        <label for="confirm_password">Confirm Password:</label><br>
        <input type="password" id="confirm_password" name="confirm_password" required><br><br>
    
        <label for="usertype">User Type:</label><br>
        <select id="usertype" name="usertype" required>
            <option value="" disabled selected>Please select an option</option>
        <option value="seeker">Job Seeker</option>
        <option value="recruiter">Job Recruiter</option>
        </select><br><br>
    
        <input type="submit" value="Sign Up">
    </form>
    
    {% endblock content %}
    ```
    - Create a function to render it
        ```python
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
        ```
    - Add url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from jobportalProject.views import signin,signup

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signup/',signup,name='signup'),
        ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now we will be able to add it from this frontend form

</details>

<details>
<summary>Day-23-Job Portal Project Part 01 to 03 (23-04-2024)</summary>

## Day 23 Topics:

- Day 22 recap
- Job Portal Part 03 (Sign-In Authentication)
- Task

### Job Portal Part 03 (Sign-In Authentication)
- For authenticate user login `authenticate`,`login` is used 
    ```python 
    from django.contrib.auth import authenticate,login,logout
    def signin(request):
        if request.method=="POST":
            uname=request.POST.get('uname')
            password=request.POST.get('password')
            
            user = authenticate(
                username=uname,
                password=password,
            )
            print(f'Logged in user: {user}')
            if user:
                login(request,user)
                return redirect('dashboard')
            else:
                return redirect('signin')
        return render(request,'signin.html')
    ```
    - For log out
        ```python
        def logoutpage(request):
            logout(request)
            return redirect('signin')
        ```
- Other task are similar to previous CRUD operation
### Task
- Job Portal Project Part 01 - 03
    - Create user model using `AbstractUser` Model
    - Create `SignUp` / `SignIn` page using below field
        - **First Name**
        - **Last name**
        - **Username**
        - **Email**
        - **Password**
        - **Confirm Password**
        - **Profile Picture**
        - **Date of Birth**
        - **Address**
        - **Blood Group**
        - **User Type** 
    - After Login user will be in a `Dashboard` with `navbar` where:
        - **Dashboard**
        - **View Job**
        - **Add Job**
        - **Applied Job**
        - **Recent Job**
        - **Profile**
        - **Log out**

            - If user is `Job Recruiter` below navigation will be present
                - **Dashboard**
                - **View Job**
                - **Add Job**
                - **Profile**
                - **Log out**
            - If user is `Job Seeker` below navigation will be present
                - **Dashboard**
                - **View Job**
                - **Applied Job**
                - **Recent Job**
                - **Profile**
                - **Log out**
            > Create all those above mentioned individual navigation pages including CRUD Operation
        - `Add Job` page will have these field:
            - **Job title**
            - **Company name**
            - **Address**
            - **Company description**
            - **Job description**
            - **Qualification**
            - **Salary information**
            - **Deadline**
            - **Designation**
            - **Experience**

</details>

<details>
<summary>Day-24-Job Portal Project Part 04 (24-04-2024)</summary>

## Day 24 Topics:
- Day 23 recap
- Job Portal Project Part 04
    - Organize Templates
    - Login Required
    - In Dashboard/view job page Only Recruiter can edit/update, delete job post where seeker can only view
    - Recruiter can see their post only which they posted but Job seeker will be able to see all the job

### Organize Templates
- Create individual folder in template folder
    ```text
    |----templates
         |
         |--recruiter
             |
             |--addjob.html
    ```
- Now edit the edit the path in `views.py` function `'recruiter/addjob.html'`

### Login Required
- It is used to restrict an user from access some pages which required login
    ```python
    from django.contrib.auth.decorators import login_required
    @login_required
    def dashboard(request):
        job=JobModel.objects.all()
        jobDict={
            'job':job
        }
        return render(request,'dashboard.html',jobDict)
    ```
    - Now in `settings.py` we have to include the `LOGIN_URL`
        ```python
        LOGIN_URL='signin'
        ```
    - Now the `dashboard.html` is being restricted from accessing without login

- Now what if according to our project there is two type of person can login `recruiter` and `seeker` where `seeker` want to access `addjob` page, so we can restrict it by using below method:
    ```python
    @login_required
    def addjob(request):
        if request.user.user_type == 'recruiter':
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
                    Recruiter=request.user.username,
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
                )
                job.save()
                return redirect('viewjob')
            return render(request,'recruiter/addjob.html')
        else:
            logout(request)
            return redirect('signin')
    ```
    > Also we can use is_authenticated to authenticate an user before accessing

### In Dashboard/view job page Only Recruiter can edit/update, delete job post where seeker can only view
- To do this we will use condition
    ```python
    @login_required
    def dashboard(request):
        job=JobModel.objects.all()
        jobDict={
            'job':job
        }
        return render(request,'dashboard.html',jobDict)
    ```
- Now `dashboard.html` page
    ```html
    <table id="customers">
    <tr>
        <th>Recruiter</th>
        <th>Job title</th>
        <th>Company name</th>
        <th>Address</th>
        <th>Company description</th>
        <th>Job description</th>
        <th>Qualification</th>
        <th>Salary information</th>
        <th>Deadline</th>
        <th>Designation</th>
        <th>Experience</th>
        <th>Action</th>
    </tr>
    {% for i in job %}
    {% if user.username == i.Recruiter %}
        <tr>
            <td>{{i.Recruiter}}</td>
            <td>{{i.Job_title}}</td>
            <td>{{i.Company_name}}</td>
            <td>{{i.Address}}</td>
            <td>{{i.Company_description}}</td>
            <td>{{i.Job_description}}</td>
            <td>{{i.Qualification}}</td>
            <td>{{i.Salary_information}}</td>
            <td>{{i.Deadline}}</td>
            <td>{{i.Designation}}</td>
            <td>{{i.Experience}}</td>
            <td>
            
            {% if user.user_type == 'recruiter' %}
            <a href="{% url 'editjob' i.id %}">Edit</a>
            <a href="{% url 'deletejob' i.id %}">Delete</a>
            {% endif %}
            <a href="{% url 'viewjob' %}">View</a>

            </td>
        </tr>
        {% elif user.user_type == 'seeker' %}
        <tr>
        <td>{{i.Recruiter}}</td>
        <td>{{i.Job_title}}</td>
        <td>{{i.Company_name}}</td>
        <td>{{i.Address}}</td>
        <td>{{i.Company_description}}</td>
        <td>{{i.Job_description}}</td>
        <td>{{i.Qualification}}</td>
        <td>{{i.Salary_information}}</td>
        <td>{{i.Deadline}}</td>
        <td>{{i.Designation}}</td>
        <td>{{i.Experience}}</td>
        <td>
            
            {% if user.user_type == 'recruiter' %}
            <a href="{% url 'editjob' i.id %}">Edit</a>
            <a href="{% url 'deletejob' i.id %}">Delete</a>
            {% endif %}
            <a href="{% url 'viewjob' %}">View</a>

        </td>
        {% endif %}
    {% endfor %}
        
    </table>
    ```
### Recruiter can see their post only which they posted but Job seeker will be able to see all the job
- To do this we can use condition 
    ```python
    @login_required
    def viewjob(request):
        job=JobModel.objects.all()
        jobDict={
            'jobs':job
        }
        return render(request,'viewjob.html',jobDict)
    ```
- Now the `viewjob.html` page
    ```html
    <body>
        <h1>Job Listings</h1>
        <div class="job-listings">
            
            {% for job in jobs %}
            
            {% if user.username == job.Recruiter %}
            <div class="job">
                <h2>{{ job.Job_title }}</h2>
                <p><strong>Company:</strong> {{ job.Company_name }}</p>
                <p><strong>Location:</strong> {{ job.Address }}</p>
                <p><strong>Company Description:</strong> {{ job.Company_description }}</p>
                <p><strong>Job Description:</strong> {{ job.Job_description }}</p>
                <p><strong>Qualification:</strong> {{ job.Qualification }}</p>
                <p><strong>Salary Information:</strong> {{ job.Salary_information }}</p>
                <p><strong>Deadline:</strong> {{ job.Deadline }}</p>
                <p><strong>Designation:</strong> {{ job.Designation }}</p>
                <p><strong>Experience:</strong> {{ job.Experience }}</p>
                <div class="actions">
                    {% if user.user_type == 'recruiter' %}
                    <button class="update"> <a href="{% url 'editjob' job.id %}" >Update</a></button>
                    <button class="delete"><a href="{% url 'deletejob' job.id %}" >Delete</a></button> 
                    {% endif %}
                </div>
            </div>
            {% elif user.user_type == 'seeker' %}
            <div class="job">
                <h2>{{ job.Job_title }}</h2>
                <p><strong>Recruiter:</strong> {{ job.Recruiter }}</p>
                <p><strong>Company:</strong> {{ job.Company_name }}</p>
                <p><strong>Location:</strong> {{ job.Address }}</p>
                <p><strong>Company Description:</strong> {{ job.Company_description }}</p>
                <p><strong>Job Description:</strong> {{ job.Job_description }}</p>
                <p><strong>Qualification:</strong> {{ job.Qualification }}</p>
                <p><strong>Salary Information:</strong> {{ job.Salary_information }}</p>
                <p><strong>Deadline:</strong> {{ job.Deadline }}</p>
                <p><strong>Designation:</strong> {{ job.Designation }}</p>
                <p><strong>Experience:</strong> {{ job.Experience }}</p>
                <div class="actions">
                    {% if user.user_type == 'recruiter' %}
                    <button class="update"> <a href="{% url 'editjob' job.id %}" >Update</a></button>
                    <button class="delete"><a href="{% url 'deletejob' job.id %}" >Delete</a></button> 
                    {% endif %}
                </div>
            </div>
            {% endif %}
        {% endfor %}
        </div>
    </body>
    {% endblock content %}
    ```
    - Here `username` of the recruiter is checked to show their posting job only
    - As job seeker can view all jobs so only the type is checked which showed all the job

</details>

<details>
<summary>Day-25-Job Portal Project (ForeignKey) (25-04-2024)</summary>

## Day 25 Topics:
- Job Portal Project Day 01 to 04 Recap
- Using ForeignKey

### Using ForeignKey
- To make sure the recruiter who posted the job we can use `ForeignKey` in `JobModel` to make a relationship with `CustomUserModel`
    ```python
    from django.db import models
    from django.contrib.auth.models import AbstractUser

    # Create your models here.

    class CustomUserModel(AbstractUser):
        fname=models.CharField(max_length=100)
        lname=models.CharField(max_length=100)
        profile_picture=models.ImageField(upload_to='media/profile_pic')
        date_of_birth=models.DateField(auto_now_add=True)
        address=models.CharField(max_length=100)
        BLOOD_GROUP=[
            ('a+','A Positive'),
            ('a-','A Negative'),
            ('b+','B Positive'),
            ('b-','B Negative'),
            ('ab+','AB Positive'),
            ('ab-','AB Negative'),
            ('o+','O Positive'),
            ('o-','O Negative'),
        ]
        blood_group=models.CharField(choices=BLOOD_GROUP,max_length=100)
        USER_TYPE=[
            ('recruiter','Job Recruiter'),
            ('seeker','Job Seeker'),
        ]
        user_type=models.CharField(choices=USER_TYPE,max_length=100)
        
        def __str__(self):
            return self.fname
        
    class JobModel(models.Model):
        Job_title=models.CharField(max_length=100)
        Company_name=models.CharField(max_length=100)
        Address=models.CharField(max_length=100)
        Company_description=models.TextField()
        Job_description=models.TextField()
        Qualification=models.CharField(max_length=100)
        Salary_information=models.CharField(max_length=100)
        Deadline=models.DateField(auto_now_add=True)
        Designation=models.CharField(max_length=100)
        Experience=models.CharField(max_length=100)
        Recruiter=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
        
        def __str__(self):
            return self.Job_title
    ```
    - Here in `JobModel` we used `Recruiter=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)` 
    - Now the argument we are passing are:
        - First one is our `CustomUserModel`
        - Second one is `on_delete=models.CASCADE`
        > First one is used for creating the relationship and the Second one is used when we gonna delete a recruiter it will also delete the jobs created by that user
</details>

<details>
<summary>Day-26-Job Portal Project Part 01 to 04 Recap (27-04-2024)</summary>

## Job portal Part 01 to 04 recap
1. Create project: `django-admin startproject jobportalProject`
2. Create app: 
    - `cd jobportalProject`
    - `py manage.py startapp jobportalApp`
3. Initial modification in `settings.py`
    - Add app name in `INSTALLED_APPS`
        ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'jobportalApp',
        ]
        ```
    - Static file directory
        ```python
        STATICFILES_DIRS = [
            BASE_DIR / "static",
        ]
        ```
    - Add the value of `'DIRS'` in `TEMPLATES` for templates directory path
        ```python
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR, 'templates'],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
        ```
4. Now Create a folder `templates` which we have added in `TEMPLATES`'s in `'DIRS'` project directory where `manage.py` present
    ```text
    jobportalProject/ # this is project name
    │
    ├── manage.py
    ├── jobportalProject/ # this is project name
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├─── jobportalApp/ # this is app name
    │    ├── migrations/
    │    ├── __init__.py
    │    ├── admin.py
    │    ├── apps.py
    │    ├── models.py
    │    ├── tests.py
    │    └── views.py
    │
    └──── templates/  # this is created manually
    ```
5. Create a `signup.html` in `templates` directory
    - Get a simple `css form` from [w3school](https://www.w3schools.com/css/css_form.asp)
    - Now let's render it; Create a file `views.py` in project directory
        ```text
        jobportalProject/ # this is project name
        │
        └── jobportalProject/ # this is project name
            ├── __init__.py
            ├── settings.py
            ├── urls.py
            ├── wsgi.py
            └── views.py # manually created
        ```
    - Create a function in `views.py`
        ```python
        from django.shortcuts import render,redirect

        def signup(request):
            return render(request,'signup.html')
        ```
    - Add url path in url pattern 
        ```python
        from django.contrib import admin
        from django.urls import path
        from jobportalProject.views import signup

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signup/',signup,name='signup'),
        ]
        ```
    - Now we can view the page in `http://127.0.0.1:8000/signup/` path
    - Modify the `signup.html` page with those below field
        - **First Name**
        - **Last name**
        - **Username**
        - **Email**
        - **Password**
        - **Confirm Password**
        - **Profile Picture**
        - **Date of Birth**
        - **Address**
        - **Blood Group**
        - **User Type**
    - As there is image in `signup`, So we need to add the media url in our `urls.py`
        ```python
        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = [
            # ... the rest of your URLconf goes here ...
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now create `AbstractUser` model in `models.py` which is in app directory
        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser
        # Create your models here.
        class CustomUserModel(AbstractUser):
            picture=models.ImageField(upload_to='static/profilepics')
            dob=models.DateField(auto_now_add=True)
            address=models.TextField()
            BLOOD_GROUP=[
                ('a+','A Positive'),
                ('a-','A Negative'),
                ('b+','B Positive'),
                ('b-','B Negative'),
                ('ab+','AB Positive'),
                ('ab-','AB Negative'),
                ('o+','O Positive'),
                ('o-','O Negative'),
            ]
            blood_group=models.CharField(choices=BLOOD_GROUP,max_length=100)
            USER_TYPE=[
                ('recruiter','Job Recruiter'),
                ('seeker','Job Seeker'),
            ]
            user_type=models.CharField(choices=USER_TYPE,max_length=100)
            
            def __str__(self):
                return self.username
        ````
        - Here missing `first_name`,`last_name`,`username`,`email`,`password` are already defined in `AbstractUser`
    - Now register the model in `admin.py`
        ```python
        from django.contrib import admin
        from jobportalApp.models import CustomUserModel

        # Register your models here.

        class CustomUserModelDisplay(admin.ModelAdmin):
            list_display=['username','blood_group','user_type']

        admin.site.register(CustomUserModel)
        ```
        - Here `CustomUserModelDisplay` is created to display the model data in admin page in more detailed.
    - Add `CustomUserModel` in `settings.py` 
        ```python
        AUTH_USER_MODEL='jobportalApp.CustomUserModel'
        ```
    - Run those command in order
        ```bash
        py manage.py makemigrations jobportalApp
        py manage.py migrate jobportalApp
        py manage.py makemigrations
        py manage.py migrate
        ```
    - Now let's modify our `signup` function in `views.py`
        ```python
        from django.shortcuts import render,redirect
        from jobportalApp.models import CustomUserModel
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
            return render(request,'signin.html')
        ```
        - Here after we get the data from form we checked if password and confirm password is same or not
        - We created another page in `templates` which is `signin.html` so that after signup user will be redirected to `signin.html` page
6. Now let's modify `signin.html`
    - `signin.html` page will have those field
        - **Username**
        - **Password**
    - Modify `signin` function
        ```python
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

        def dashboard(request):
            return render(request,'dashboard.html')
        ```
        - Here we have imported `from django.contrib.auth import authenticate,login,logout` where 
            - `authenticate` is used to authenticate an user
            - `login` is used to login an user with session
            - `logout` which will be used in separate function to logout an user
        - After authentication is successful user will be redirected to `dashboard.html` page
7. Now we have to do the template mastering while creating `dashboard.html`
    - Get a navbar from [w3school](https://www.w3schools.com/css/css_navbar_horizontal.asp)
    - Create `base.html`, `navbar.html`, `dashboard.html`
        - `base.html` - This is the base structure of the page
        - `navbar.html` - This will only contain the navbar content and include it in `base.html`
        - `dashboard.html` - This will extends the `base.html` and it's content will be inside block content
8. Let's implement logout function
    - Create a `logoutpage` function in `views.py` 
        ```python
        def logoutpage(request):
            logout(request)
            return redirect('signin')
        ```
    - Add url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from jobportalProject.views import signup,signin,dashboard,logoutpage

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signup/',signup,name='signup'),
            path('',signin,name='signin'),
            path('dashboard/',dashboard,name='dashboard'),
            path('logoutpage/',logoutpage,name='logoutpage'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Add the `logoutpage` name in navbar url 
        ```html
        <ul>
            <li><a href="{% url 'dashboard' %}">Dashboard</a></li>
            <li style="float:right"><a class="active" href="{% url 'logoutpage' %}">Log Out</a></li>
        </ul>
        ```
9. Now after logout we can still visit the dashboard url which should not.
    - Let's add login required functionality
        ```python
        from django.contrib.auth.decorators import login_required
        @login_required
        def dashboard(request):
            return render(request,'dashboard.html')
        ```
        Now we have to add `LOGIN_URL` in `settings.py`
        ```python
        LOGIN_URL='signin'
        ```
        - Now without login dashboard can't be access
        - As we have added `LOGIN_URL` so whenever user try to access dashboard page without login , user will be redirected in login page
10. Now we have to add those pages in our `navbar.html` where we already created `dashboard` and `logout`
    - **Dashboard**
    - **View Job**
    - **Add Job**
    - **Applied Job**
    - **Recent Job**
    - **Profile**
    - **Log out**
        - First let's create add job page; In `addjob.html` form page below field will be present and the template file will be in `recuiter/addjob.html` of templates directory
            - **Job title**
            - **Company name**
            - **Address**
            - **Company description**
            - **Job description**
            - **Qualification**
            - **Salary information**
            - **Deadline**
            - **Designation**
            - **Experience**
        - After creating form we will create the `addjob` function 
            ```python
            def addjob(request):
                return render(request,'addjob.html')
            ```
        - Add this in `urls.py` and `navbar` and proceed to create the model in `models.py`
            ```python
            class JobModel(models.Model):
                Job_title=models.CharField(max_length=100)
                Company_name=models.CharField(max_length=100)
                Address=models.CharField(max_length=100)
                Company_description=models.TextField()
                Job_description=models.TextField()
                Qualification=models.CharField(max_length=100)
                Salary_information=models.CharField(max_length=100)
                Deadline=models.DateField(auto_now_add=True)
                Designation=models.CharField(max_length=100)
                Experience=models.CharField(max_length=100)
                Created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
                
                def __str__(self):
                    return f"{self.Job_title} created by {self.Created_by}"
            ```
            - Here `Created_by` is creating a relationship with our `CustomUserModel` model and when a user is deleted it will delete all the job created by that user too which is done by using `on_delete=models.CASCADE`
        - Register the model in `admin.py`
            ```python
            admin.site.register(JobModel)
            ```
        - Now we can modify our `addjob` function to get the user input and save it in our `JobModel`
            ```python
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
                return render(request,'addjob.html')
            ```
        - Now let's create `viewjob.html` page to view the job which we have added; where below function will pass all the job data
            ```python
            @login_required
            def viewjob(request):
                jobs=JobModel.objects.all()
                jobDict={
                    'jobs':jobs
                }
                return render(request,'viewjob.html',jobDict)
            ```
        - Now let's create the dashboard where all the job will be present in table with three action: `edit`,`delete`,`view`; get the table from [w3school](https://www.w3schools.com/css/tryit.asp?filename=trycss_table_fancy)
            ```python
            @login_required
            def dashboard(request):
                jobs=JobModel.objects.all()
                jobDict={
                    'jobs':jobs
                }
                return render(request,'dashboard.html',jobDict)
            ```
            Where the table will be as below
            ```html
            <table id="customers">
            <tr>
                <th>Job title</th>
                <th>Company name</th>
                <th>Address</th>
                <th>Action</th>
            </tr>

            {% for i in jobs %}
                <tr>
                    <td>{{i.Job_title}}</td>
                    <td>{{i.Company_name}}</td>
                    <td>{{i.Address}}</td>
                    <td>
                        <a href="">View</a>
                        <a href="">Edit</a>
                        <a href="">Delete</a>
                    </td>
                </tr>
            {% endfor %}
                
            </table>
            ```
            - Here we will implement the delete action first
                ```python
                @login_required
                def deletejob(request,myid):
                    job=JobModel.objects.get(id=myid)
                    job.delete()
                    return redirect('dashboard')
                ```
                Now add the function in `urls.py` pattern and add the name in dashboard delete action url
            - Now let's implement the edit action; Where we will create the `editjob.html` page same as `addjob.html` in recruiter directory of our templates folder with different action function; Below we implement the `editjob function`
                ```python
                @login_required
                def editjob(request,myid):
                    job=JobModel.objects.get(id=myid)
                    jodDict={
                        'job':job
                    }
                    return render(request,'recruiter/editjob.html',jodDict)
                ```
                Now the update function which will be the action of the `editjob.html` page
                ```python
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
                ```
                - Here `Deadline` is checked if it is not updated by user it will take the currently available deadline from the model
            - Now we will implement the `viewsinglejob.html` page where user will view the specific single job from dashboard
                ```python
                @login_required
                def viewsinglejob(request,myid):
                    job=JobModel.objects.get(id=myid)
                    jodDict={
                        'job':job
                    }
                    return render(request,'viewsinglejob.html',jodDict)
                ```
        - As we haven't complete the profile page yet, so let's do it by adding a `profile.html` in templates directory and implement the below function
            ```python
            @login_required
            def profile(request):
                return render(request,'profile.html')
            ```
            Now the `profile.html` page which already have the `user` data after login, so we can access the model data using `{{user.variable_name_in_model}}`
            ```html
            <div class="user-info">
                <label>First Name:</label>
                <p>{{ user.first_name }}</p>

                <label>Last Name:</label>
                <p>{{ user.last_name }}</p>

                <label>Username:</label>
                <p>{{ user.username }}</p>

                <label>Email:</label>
                <p>{{ user.email }}</p>

                <label>Date of Birth:</label>
                <p>{{ user.dob }}</p>

                <label>Address:</label>
                <p>{{ user.address }}</p>

                <label>Blood Group:</label>
                <p>{{ user.blood_group }}</p>

                <label>User Type:</label>
                <p>{{ user.user_type }}</p>
            </div>
            ```
11. Now we have completed the project but there is something which we can notice, like Job seeker can 
    - Add job
    - Delete job
    - Edit job
    
    To solve this we have to use condition to verify the `usertype`
    - First we will solve the add job where only recruiter can add job; For now we can simply check it in frontend if usertype is recruiter or not. Let's edit the `navbar.html`
        ```html
        <ul>
            <li><a href="{% url 'dashboard' %}">Dashboard</a></li>
            
            {% if user.user_type == 'recruiter' %}
            <li><a href="{% url 'addjob' %}">Add Job</a></li>
            {% endif %}
            <li><a href="{% url 'viewjob' %}">View Job</a></li>
            <li style="float:right"><a class="active" href="{% url 'logoutpage' %}">Log Out</a></li>
            <li style="float:right"><a href="{% url 'profile' %}">Profile</a></li>
        </ul>
        ```
        - Here we checked the user type `user.user_type == 'recruiter'`
    - Now the delete and edit action in `dashboard.html` page; Here similarly we will checked the user type
        ```html
        {% for i in jobs %}
            <tr>
                <td>{{i.Job_title}}</td>
                <td>{{i.Company_name}}</td>
                <td>{{i.Address}}</td>
                <td>
                {% if user.user_type == 'recruiter' %}
                <a href="{% url 'editjob' i.id %}">Edit</a>
                <a href="{% url 'deletejob' i.id %}">Delete</a>
                {% endif %}
                <a href="{% url 'viewsinglejob' i.id %}">View</a>
                </td>
            </tr>
        {% endfor %}
        ```
        - Here we also checked the user type `user.user_type == 'recruiter'`
12. Now a recruiter can only see their posted job and edit those only not the others 
    - To do this we have to modify our `viewjob` function
        ```python
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
        ```
    - Now let's fix the `dashboard.html` page also by modifying the dashboard function
        ```python
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
        ```
        ```diff
        - The old viewjob & dashboard function was passing the whole job model data in dictionary
        + We changes that by checking the user type if it is recruiter then who created that job by filtering that we pass the data in dictionary otherwise if user type is job seeker we pass whole job model data
        ```
</details>

<details>
<summary>Day-27-Lab Exam 04 (28-04-2024)</summary>

## Lab Exam 04 Recipe Manager Project

> Recipe Manager Project Overview: The Recipe Manager is a web application built with using Django. allowing users to manage their recipes. It provides features for user authentication, recipe management. The application utilizes Django's built-in authentication system, SQLite for the database, and Django templates for rendering HTML pages. Two types of users: chef (or owners) who can create, edit, delete, and update recipes. and viewers who can only view recipes.

User Authentication: 
- **Sign up**: Users can create a new account by providing a Username, E-mail. and Password, Gender, Age, City, Country. **(15 Marks)**
- **Log in**: Registered users can log in using their Username and Password. **(10 Marks)**
- **Log out**: Users can log out of their accounts. **(5 Marks)**
- **Recipe**: Recipe Title, Ingredients, Instructions, Preparation Time, Cooking Time, Total Time. Difficulty Level, Nutritional Information, Sample Recipe image, Recipe Category, Tags (vegetarian, non-vegetarian), Total Calorie. **(20 Marks)**
- Viewers will view all Recipe which is created by Chef **(25 Marks)**
- Create a Profile for both users **(15 Marks)**
- When a chef login the website only he/she can view his/her created recipe. **(10 Marks)**

> It took 2 hour 50 minutes for me which placed me 2nd position; total given time was 4 hours

</details>

<details>
<summary>Day-28-Profile Model (OneToOneField) (29-04-2024)</summary>

## Day 28 Topics:
- Lab Exam 04 : Recipe Manager Project Recap
- Profile Model

### Profile Model
- To create profile we will use `OneToOneField`
    ```python
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    # Create your models here.

    class CustomUserModel(AbstractUser):
        GENDER=[
            ('male','Male'),
            ('female','Female'),
        ]
        gender=models.CharField(choices=GENDER,max_length=50)
        age=models.CharField(max_length=100)
        city=models.CharField(max_length=100)
        country=models.CharField(max_length=100)
        USER_TYPE=[
            ('chef','Chef'),
            ('viewer','Viewer'),
        ]
        user_type=models.CharField(choices=USER_TYPE,max_length=50)

        def __str__(self):
            return self.username
        
    class ChefProfileModel(models.Model):
        myuser = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
        experience=models.CharField(max_length=100)
        skill=models.CharField(max_length=100)
        resume_latter=models.CharField(max_length=100)
        profile_pic=models.ImageField(upload_to='static/profile_pic')

        def __str__(self):
            return self.myuser.username

    class ViewerProfileModel(models.Model):
        myuser = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
        favourite=models.CharField(max_length=100)
        profile_pic=models.ImageField(upload_to='static/profile_pic')

        def __str__(self):
            return self.myuser.username
    ```
    - Here we  created two profile `ChefProfileModel` and `ViewerProfileModel`
    - Both has `OneToOneField` relationship with `CustomUserModel` model
- Register both model in `admin.py`
    ```python
    from django.contrib import admin
    from recipeApp.models import CustomUserModel,RecipeModel,ChefProfileModel,ViewerProfileModel
    # Register your models here.

    class CustomUserModelDisplay(admin.ModelAdmin):
        list_display=['username','user_type','gender']

    admin.site.register(CustomUserModel,CustomUserModelDisplay)
    admin.site.register(RecipeModel)
    admin.site.register(ChefProfileModel)
    admin.site.register(ViewerProfileModel)
    ```

</details>

<details>
<summary>Day-29-Recipe Management Project recap Day 02 & Python Day 06 (30-04-2024)</summary>

## Day 29 Topics:
- Lab Exam 04 : Recipe Manager Project Recap Day 02
- Python Day 06

### Python Day 06
- Nested if...else recap
- Test exam on previous day's class
- if...elif

### Nested if...else recap
- Problem 01: which one is the greater number among 4 using nested `if..else`
    ```python
    w=10
    x=20
    y=30
    z=40

    if w>x:
        if w>y:
            if w>z:
                print('w is greater')
            else:
                print('z is greater')
        else:
            if y>z:
                print('y is greater')
            else:
                print('z is greater')
    else:
        if x>y:
            if x>z:
                print('x is greater')
            else:
                print('z is greater')
        else:
            if y>z:
                print('y is greater')
            else:
                print('z is greater')
    ```

### Test exam on previous day's class
Which of the following is not a valid comparison operator in Python?
 - [ ] ==
 - [ ] !=
 - [ ] <=
 - [ ] ><

What is the output of the following code snippet?
```python
x = 5
y = 2
print(x ** y)
```
 - [ ] 10
 - [ ] 25
 - [ ] 7
 - [ ] 32

What is the output of the following code snippet?
```python
print(2 ** 3)
```
 - [ ] 6
 - [ ] 7
 - [ ] 8
 - [ ] 16

Which of the following is not a valid variable name in Python?
 - [ ] my_var
 - [ ] 2var
 - [ ] _var
 - [ ] var2

What is the output of the following code snippet?
```python
print("Hello" * 3)
```
 - [ ] HelloHelloHello
 - [ ] Hello3
 - [ ] HelloHello
 - [ ] 3Hello

What is the output of the following code snippet?
```python
print(10 / 3)
```
 - [ ] Error
 - [ ] 3.0
 - [ ] 3
 - [ ] 3.3333

What function can be used to convert a string to an integer in Python?
 - [ ] str()
 - [ ] int()
 - [ ] float()
 - [ ] bool(

What is the result of the expression `10 / 2` ?
 - [ ] 5.0
 - [ ] 5
 - [ ] 2.5
 - [ ] 2


What is the output of the following code snippet?
```python
x = 5
x += 2
print(x)
```
 - [ ] Error
 - [ ] 10
 - [ ] 7
 - [ ] 5

Which of the following is the correct way to assign a value to a variable in Python?
 - [ ] x := 5
 - [ ] x == 5
 - [ ] 5 = x
 - [ ] x = 5

What is the output of the following code snippet?
```python
print(5 == 5.0)
```
 - [ ] 1
 - [ ] Error
 - [ ] False
 - [ ] True

What symbol is used to denote comments in Python?
 - [ ] //
 - [ ] #
 - [ ] /*
 - [ ] %

What is the output of the following code snippet?
```python
x = 10
y = 3
print(x // y)
```
 - [ ] 4
 - [ ] 3.0
 - [ ] 3
 - [ ] 3.3333

What is the result of the expression `3 * "2"`?
 - [ ] Error
 - [ ] 32
 - [ ] "222"
 - [ ] 6

### if...elif
- Problem 02: which one is the greater number among 5 using `elif`
    ```python
    v=10
    w=20
    x=30
    y=40
    z=50

    if (v>=w and v>=x and v>=y and v>=z):
        print('v is greater')
    elif (w>=x and w>=y and w>=z):
        print('w is greater')
    elif (x>=y and x>=z):
        print('x is greater')
    elif (y>=z):
        print('y is greater')
    else:
        print('z is greater')
    ```
- Creating a simple application (Bkash) using condition
    ```python
    bkash_menu = '''
    1. Send Money
    2. Send Money to Non-Bkash User
    3. Mobile Recharge
    4. Payment
    5. Cash Out
    6. Pay Bill
    7. Microfinance
    8. Download Bkash App
    9. My Bkash
    10. Reset Pin
    '''
    print(bkash_menu)

    choice = int(input("Enter your choice: "))

    print(f'You choose: {choice}')

    if choice==1:
        receiver_number = int(input("Enter receiver number: "))
        if receiver_number:
            amount = int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Sent Successful to {receiver_number}")
                else:
                    print("Please enter valid number")
            else:
                print("Please enter valid pin")
        else:
            print("please enter valid number")
    ```
    > Only option 1 implemented

</details>

<details>
<summary>Day-29-Bkash Simple Application using Python</summary>

## Creating a simple application (Bkash) using condition

- Using if..elif..else create an Bkash like application
    ```python
    bkash_menu = '''
    1. Send Money
    2. Send Money to Non-Bkash User
    3. Mobile Recharge
    4. Payment
    5. Cash Out
    6. Pay Bill
    7. Microfinance
    8. Download Bkash App
    9. My Bkash
    10. Reset Pin
    '''
    print(bkash_menu)

    choice = int(input("Enter your choice: "))

    print(f'You choose: {choice}')

    if choice==1:
        receiver_number = int(input("Enter receiver number: "))
        if receiver_number:
            amount = int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Sent Successful to {receiver_number}")
                else:
                    print("Please enter valid number")
            else:
                print("Please enter valid pin")
        else:
            print("please enter valid number")
    elif choice==2:
        receiver_number = int(input("Enter receiver number: "))
        if receiver_number:
            amount = int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Sent Successful to {receiver_number}")
                else:
                    print("Please enter valid number")
            else:
                print("Please enter valid amount")
        else:
            print("please enter valid number")
    elif choice==3:
        operator = int(input('''
    Choose Operator:
    1. Robi
    2. Airtel
    3. Banglalink
    4. Grameenphone
    5. Teletalk
        '''))
        if operator:
            mobile_number = int(input("Enter mobile number: "))
            if mobile_number:
                recharge_amount=int(input("Enter recharge amount: "))
                if recharge_amount:
                    pin = int(input("Enter pin: "))
                    if pin:
                        print(f"{recharge_amount} BDT Recharge Successful to {mobile_number}")
                    else:
                        print("Please enter valid pin")
                else:
                    print("Please enter valid recharge amount")
            else:
                print("Please enter valid number")
        else:
            print("please choose a valid option")
    elif choice==4:
        merchant_number = int(input("Enter merchant number: "))
        if merchant_number:
            amount=int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Payment Successful to {merchant_number}")
                else:
                    print("Please enter valid pin")
            else:
                print("Please enter valid amount")
        else:
            ("Please enter valid number")
    elif choice==5:
        from_whom = int(input('''
    Choose an option:
    1. From Agent
    2. From ATM
    3. Priyo Agent Numbers
        '''))
        if from_whom:
            num= int(input("Enter number: "))
            if num:
                amount=int(input("Enter amount: "))
                if amount:
                    pin = int(input("Enter pin: "))
                    if pin:
                        print(f"{amount} BDT Cash Out Successful to {num}")
                    else:
                        print("Please enter valid pin")
                else:
                    print("Please enter valid amount")
            else:
                print("Please enter valid number")
        else:
            print("please choose a valid option")
    elif choice==6:
        bill_type = int(input('''
    Choose an option:
    1. Electricity (Prepaid)
    2. Electricity (Postpaid)
    3. Gas
    4. Water
    5. Internet & Phone
    6. TV
    7. City Services
    8. Education
    9. Financial Services
    10. Others
        '''))
        bill_number = int(input("Enter bill number: "))
        if bill_number:
            if bill_number:
                amount=int(input("Enter amount: "))
                if amount:
                    pin = int(input("Enter pin: "))
                    if pin:
                        print(f"{amount} BDT Pay Bill Successful to {bill_number}")
                    else:
                        print("Please enter valid pin")
                else:
                    print("Please enter valid amount")
            else:
                print("Please enter valid bill number")
        else:
            print("please choose a valid option")
    ```
    > Only option 1 to 6 implemented

</details>

<details>
<summary>Day-30-Job Portal Project User Profile (02-05-2024)</summary>

## Day 30 Topics:
- Job Portal Project recap
- User Profile Model
- User Profile Update
- Recruiter posted job
- Task

### User Profile Model
- In job portal project app directory `models.py`
    ```python
    class CustomUserModel(AbstractUser):
        picture = models.ImageField(upload_to='static/profilePic')
        dob = models.DateField(auto_now_add=True)
        address = models.CharField(max_length=100)
        BLOOD_GROUP=[
            ('a+','A Positive'),
            ('a-','A Negative'),
            ('b+','B Positive'),
            ('b-','B Negative'),
            ('c+','C Positive'),
            ('c-','C Negative'),
            ('ab+','AB Positive'),
            ('ab-','AB Negative'),
            ('o+','O Positive'),
            ('o-','O Negative'),
        ]
        blood_group = models.CharField(choices=BLOOD_GROUP,max_length=100)
        USER_TYPE=[
            ('recruiter','Job Recruiter'),
            ('seeker','Job Seeker'),
        ]
        user_type=models.CharField(choices=USER_TYPE,max_length=100)

        def __str__(self):
            return self.username

    class JobSeekerProfile(models.Model):
        user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='jobseekerprofile')
        skills=models.CharField(max_length=100)
        work_experience=models.CharField(max_length=100)

        def __str__(self):
            return self.user.user_type

    class JobRecruiterProfile(models.Model):
        user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='jobrecruiterprofile')
        Skills_Required = models.CharField(max_length=200)
        Work_Schedule = models.CharField(max_length=50)
        def __str__(self):
            return self.user.user_type
    ```
    - Here `JobSeekerProfile` and `JobRecruiterProfile` models has `One to One` relationship with `CustomUserModel`
    - In `JobSeekerProfile` and `JobRecruiterProfile`
        - `CustomUserModel` is the model name of the custom user model to make the `One to One` relationship
        - `on_delete=models.CASCADE` is used so that when a user is deleted other info will also deleted
        - `related_name='jobrecruiterprofile'` which will be used in html page to get access; e.g: `{{ user.jobrecruiterprofile.Skills_Required }}`

### User Profile Update
- To update the user profile we will add the `updateprofile` function in `views.py`
    ```python
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
    ```
    - Here We take all the info from the edit page form
    - Then we checked if `picture` is present in user edited one
    - If `picture` is present then we update it otherwise we take those value from previously saved one which we get by `id`
        > We can check it separately for `dob` also but for now we are checking only once
    - Another tricky one is `password`, We have to give the model password otherwise it will store empty in password field in the model; So we assign the user password which we get by `id`
    - Now according to our application there are two types and both type has separate model, to update those we checked the `user_type` then we update it by `id`

### Recruiter posted job
- First create a function to filterout who created the job then we will sent that as dictionary in frontend
    ```python
    def postedjob(request):
        current_user=request.user
        posted_job=JobModel.objects.filter(Created_by=current_user)
        postjobDict={
            'posted_job':posted_job
        }
        return render(request,'postedjob.html',postjobDict)
    ```
- Now in `postedjob` html a for loop will do the rest
- Make sure to add the url name in posted job action button

### Task
- Complete User Profile
- Add Edit action button in user profile
- Complete Recruiter Job posted action button to view all the posted job by that recruiter

</details>

<details>
<summary>Day-31-Job Portal Project Time Challenge (04-05-2024)</summary>

## Day 31 Topics:
- Job Portal Project Time Challenge
    - Field Requirement
- Model hidden field/attribute notes

### Job Portal Project Time Challenge
- Challenge: Finish the project within 2 Hours
    > It took around 2 hours for me
- Field Requirement
    - Signup (12 field)
        - Profile Photo
        - First Name
        - Last Name
        - Username
        - Password
        - Confirm Password
        - Age
        - Gender
        - City
        - Country
        - Blood Group (4 types)
        - User types (Recruiter,Seeker)
    - Add Job (11 field)
        - Company logo
        - Job title
        - Job description
        - Job location
        - Requirements
        - Qualifications
        - Job types (Full time, Part time)
        - Workplace (Remote, On-site)
        - Salary
        - Experience
        - Deadline
    - Recruiter Profile (3 field)
        - Company name
        - Company location
        - Recruiter Name
    - Seeker Profile (3 field)
        - Qualification
        - Experience
        - Skills

### Model hidden field/attribute notes
- While working on signup, we have to create the `CustomUserModel` using `AbstractUser`
- While working on Add Job, we have to create the `JobModel` with an extra field `Created_by` which will create relationship with `CustomUserModel` using `ForeignKey`; Make sure to add `on_delete` so that when that user is deleted , it's created job will also get deleted
- While working on Recruiter Profile, we have to create the `RecruiterProfileModel` with an extra field `user` which will create relationship with `CustomUserModel` using `OneToOneField`; In here we also have to add `on_delete` with `related_name`
- Similarly in Seeker Profile, `SeekerProfileModel` will also have `user` field with `OneToOneField` relationship with `CustomUserModel` including `on_delete` and `related_name`
- Now while accessing user data from `CustomUserModel` in html pages, we can use `{{user.field_name_in_model}}`; But while accessing `RecruiterProfileModel` or `SeekerProfileModel` we have to access it through `related_name`: `{{user.related_name.field_name_in_model}}`

</details>

<details>
<summary>Day-32-Job Portal More Profile Info & Template Mastering (05-05-2024)</summary>

## Day 32 Topics:
- Job Portal Project Profile
    - More model in profile
    - Connect the Custom user data to other created model while signup
    - Template Mastering in Profile page

### More model in profile
- We will add more model which will be displayed in our profile page, and those model will have `OneToOneField` relationship

- Model for Recruiter
    - `RecruiterBasicInfoModel`
    - `RecruiterContactModel`
- Model for Seeker
    - `SeekerBasicInfoModel`
    - `SeekerContactModel`
    - `SeekerEducationModel`
    - `SeekerWorkExModel`
    > Each model has `OneToOneField` relationship with `CustomUserModel`

### Connect the Custom user data to other created model while signup
- Modify the `signup` function in `views.py` 
    ```python
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
                return redirect('signin')
            else:
                return redirect('signup')
        return render(request,'signup.html')
    ```
    - Here after checking the user type we pass the `user` in `user` of other created model; e.g: `RecruiterProfileModel.objects.create(user = user)`

### Template Mastering in Profile page
- To show the newly created model data we will do template mastering in profile page
    - First separate the current content in a div in another html file
    - `profile.html`
        ```html
        <div class="profile-container">
                <h3>Profile Photo</h3>    
                <div class="profile-photo">
                    <img src="/{{user.profile_photo}}" width="100px" alt="">
                </div>

                {% include 'info_button.html' %}
                
                {% block info %}

                {% endblock info %}
        </div>
        ```
        - Here we also separate the button too 
            > which is not mandatory
        - As it will be our master template for profile so the block content is empty ; now the name of block content is `block info` because we already used the `block content`
    - Now Extend the `profile.html` in the newly created `profiles_info.html` page
    - Make sure to create the `function` and `url` too for this `profiles_info.html`
    - Similarly we created other html pages for showing other model info in a specific block on the `profile.html` page

</details>

<details>
<summary>Day-33-Django Messages (06-05-2024)</summary>

## Day 33 Topics:
- Job Portal Project Profile Edit
    - Auto selected of the current one (In select option edit)
- Django Messages
- Task

### Auto selected of the current one (In select option edit)
- We can use the condition inside option tag to auto select the current on in edit page
    ```html
    <label for="lname">Gender</label>
    <select id="country" name="gender">
        <option value="male" {% if user.gender == "male" %} selected {% endif %}>Male</option>
        <option value="female"{% if user.gender == "female" %} selected {% endif %} >Female</option>
    </select> <br> <br>
    ```
### Django Messages
- We can show the user messages after an operation is passed or failed
- Django available messages:
    | Constant | Purpose                                                                                   | Tag     |
    |----------|-------------------------------------------------------------------------------------------|---------|
    | DEBUG    | Development-related messages that will be ignored (or removed) in a production deployment | debug   |
    | INFO     | Informational messages for the user                                                       | info    |
    | SUCCESS  | An action was successful, e.g. “Your profile was updated successfully”                    | success |
    | WARNING  | A failure did not occur but may be imminent                                               | warning |
    | ERROR    | An action was not successful or some other failure occurred                               | error   |

    - Usages:
        ```python
        messages.debug(request, "%s SQL statements were executed." % count)
        messages.info(request, "Three credits remain in your account.")
        messages.success(request, "Profile details updated.")
        messages.warning(request, "Your account expires in three days.")
        messages.error(request, "Document deleted.")
        ```
    - Or we can define a dictionary to organize all the messages
        ```python
        all_messages = {
            ('debug_message' : '%s SQL statements were executed.'),
            ('info_message' : 'Three credits remain in your account.'),
            ('success_message' : 'Profile details updated.'),
            ('warning_message' : 'Your account expires in three days.'),
            ('error_message' : 'Document deleted.'),
        }
        # Now we can use those like this:
        messages.debug(request, all_messages['debug_message'])
        messages.info(request, all_messages['info_message'])
        messages.success(request, all_messages['success_message'])
        messages.warning(request, all_messages['warning_message'])
        messages.error(request, all_messages['error_message'])
        ```
    - Now to show this in html pages, we can create a `messages.html`
        ```jinja
        {% if messages %}
        {% for message in messages %}
            {% if message.tags == 'success' %}
            <p class="message success">{{ message }}</p>
            {% elif message.tags == 'warning' %}
            <p class="message warning">{{ message }}</p>
            {% endif %}
        {% endfor %}
        {% endif %}
        ```
    - Include this `messages.html` in the place where we want to show the message
### Task
- Show the required messages in signup / signin form

### Show the required messages in signup form
- We created a dictionary
    ```python
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
    ```
    - Now to show any warning from this we can access it like this: `messages.warning(request, all_messages['first_name_warning'])`
- Everytime page get redirect it refreshed and all data erased, so we are rendering it with the preserve data which we get from the form and send it back as dictionary data and showing it in `value attribute` below `signin` function we send the `context` which is preserving the data we get from the form
    ```python
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
    ```

</details>

<details>
<summary>Day-34-Python Day 07 & Database Discussion (07-05-2024)</summary>

## Day 33 Topics:
- Python Day 7
- Database discussion
### Python Day 7
- Exam 02
- If...else in single line
- Python ternary operation
- While loop

### Exam 02
How would you decrement n by 4 using a shorthand operator?
 - [ ] n -=4
 - [ ] n =- 4
 - [ ] n = n - 4
 - [ ] Both A and C

Which of the following is not a valid Python increment operation?
 - [ ] x += 1
 - [ ] x = x + 1
 - [ ] x++
 - [ ] x +=- 1

What is the output of the following nested condition?
```python
x = 5
y = 10
if x > y:
    if x > 10:
        print("A")
    else:
        print("B")
else:
    if y < 20:
        print("C")
    else:
        print("D")
```
 - [ ] A
 - [ ] B
 - [ ] C
 - [ ] D

Choose the correct way to declare a variable x with the value 100.
 - [ ] int x = 100
 - [ ] x = 100
 - [ ] var x = 100
 - [ ] x == 100

```python
if not False:
    print("Hello World")
else:
    print("Goodbye World")
```
 - [ ] Hello World
 - [ ] Goodbye World
 - [ ] Nothing, it's an error
 - [ ] Both A and B

Which condition will be true when x = 3 and y = 5?
```python
if x > y:
    print("X")
elif y > x:
    print("Y")
else:
    print("Equal")
```
 - [ ] X
 - [ ] Y
 - [ ] Equal
 - [ ] NONE

```python
x = 4
x *= 2
```
 - [ ] 8
 - [ ] 2
 - [ ] 6
 - [ ] 4

```python
x = 4
y = 15
print(x % y)
```
 - [ ] 4
 - [ ] 11
 - [ ] 3
 - [ ] 0

What is the output of the following code if a = 10 and b = 20?
```python
if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("A and B are equal")
```
 - [ ] A is greater
 - [ ] B is greater
 - [ ] A and B are equal
 - [ ] None of the above

Evaluate the following logical expression when x = True and y = False:
```python
if x and not y:
    print("True")
else:
    print("False")
```
 - [ ] True
 - [ ] False
 - [ ] Error
 - [ ] None

```python
a = 5
a *= 2
```
 - [ ] Subtracts 2 from a
 - [ ] Adds 2 to a
 - [ ] Divides a by 2
 - [ ] Multiplies a by 2
 - [ ] Other:___________

Which operator is used for integer division that discards the remainder?
 - [ ] **
 - [ ] //
 - [ ] /
 - [ ] %

```python
a = 8
b = '4'
print(a + b)
```
 - [ ] 8'4'
 - [ ] 12
 - [ ] 84
 - [ ] Error

If a = 10, what is the value of a after a //= 3?
 - [ ] 3
 - [ ] 3.33
 - [ ] 7
 - [ ] 4

print(2 + 3 * 4)
 - [ ] 20
 - [ ] 14
 - [ ] 5
 - [ ] 24

### If else in single line
- We can write if..else in single line
    ```python
    a=300
    b=100

    if a>b:print("a is greater") else: print("b is greater")
    ```

### Python ternary operation
- Which is greater between a,b 
    ```python
    a=300
    b=100

    print("a is greater")if a>b else print("b is greater")
    ```
- Which is greater between a,b,c
    ```python
    a=100
    b=200
    c=300

    print("a greater")if (a>b and a>c) else print("b is greater") if b>c else print("c is greater")
    ```
- Which is greater between a,b,c,d
    ```python
    a=100
    b=200
    c=300
    d=400

    print("a is greater") if (a>b and a>c and a>d) else print("b is greater") if b>c and b>d else print("c is greater") if c>d else print("d is greater")
    ```
- Which is greater between a,b,c,d,e
    ```python
    a=100
    b=200
    c=300
    d=400
    e=500

    print("a is greater") if (a>b and a>c and a>d and a>e) else print("b is greater") if b>c and b>d and b>e else print("c is greater") if c>d and c>e else print("d is greater") if d>e else print("e is greater")
    ```

### While loop
- It will run until the condition is false
    ```python
    i=1
    while i<6:
        print(i)
        i+=1
    ```

### Database discussion
- Field (Table head)
- Object (Table data)
- Query (SQL Query)
- ORM vs SQL query
    - ORM :arrow_right: `model_name.objects.get(id=id)`
    - SQL :arrow_right: `SELECT * FROM table_name WHERE id = 1;`
- Entities and Attributes
    | Entities |              Attributes                        |
    |----------|------------------------------------------------|
    |Student   | Student_ID (Primary Key), Name, Age, Gender    |
    |Book      | ISBN (Primary Key), Title, Author, Publish_Date|
    |Employee  | Employee_ID (Primary Key), Name, Department    |

</details>

<details>
<summary>Day-35-Python Day 08 Python Bkash App (08-05-2024)</summary>

## Python Bkash App (Options)

### Main Options
1. Send Money
2. Send Money to Non-Bkash User
3. Mobile Recharge
4. Payment
5. Cash Out
6. Pay Bill
7. Microfinance
8. Download Bkash App
9. My Bkash
10. Reset Pin

### Send Money Options
- Enter Personal Bkash Number
    - Enter Amount
    - Enter Your Bkash PIN
    - Success message

### Send Money to Non-Bkash User
- Enter receiver number
    - Enter amount
    - Enter pin
    - Success message

### Mobile Recharge
- Choose Operator:
    1. Robi
    2. Airtel
    3. Banglalink
    4. Grameenphone
    5. Teletalk
        - Enter mobile number
        - Enter recharge amount
        - Enter pin
        - Success message
### Payment
- Enter merchant number
    - Enter amount
    - Enter pin
    - Success message

### Cash Out
- Choose an option:
    1. From Agent
    2. From ATM
    3. Priyo Agent Numbers
        - Enter number
        - Enter amount
        - Enter pin
        - Success message

### Pay Bill
- Choose an option:
    1. Electricity (Prepaid)
    2. Electricity (Postpaid)
    3. Gas
    4. Water
    5. Internet & Phone
    6. TV
    7. City Services
    8. Education
    9. Financial Services
    10. Others
        - Enter bill number
        - Enter amount
        - Enter pin
        - Success message

### Microfinance
- Enter Your Microfinance Type
    - BRAC
    - UDDIPAN
    - SHAKTI
    - Managed saved accounts
        - Enter Your Pay Loan Amount
        - Enter Your ID or Number
        - Enter Your PIN
        - Success message

###  Download Bkash App
- Download Bkash App

### My Bkash
- Check Balance 
- Request Statement
- Change PIN
- Priyo Numbers
- Save Bill
- Update MNP
- Confirm iPhone Login
- iPhone PIN Reset
- Helpline
- Main Menu

</details>

<details>
<summary>Day-36-Profile Update & Change Password (09-05-2024)</summary>

## Day 36 Topics:
- Job portal project
    - Profile Update
    - Change Password

### Profile Update
- We created `updateprofile` function in `views.py`
    ```python
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
    ```
    - Here first we get the profile data
    - Then we update it using `request.user` which we stored in `current_user`
    - Before we update we have to verify that the user is authenticate, So we checked password using `from django.contrib.auth.hashers import check_password` if password match then the update will proceed
    - To update custom user model which we created from abstract user we use `request.user`
    - To update other model we use their related name `request.user.recruiterprofilemodel`
    - To show warning message we define those message in a dictionary and show them using `from django.contrib import messages`
        ```python
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
        ```

### Change Password
- We define `changepassword` function in `views.py`
    ```python
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
    ```
    - First we get the value then check the password using `from django.contrib.auth.hashers import check_password` 
        - Here check_password(cu_password,request.user.password)
            - `cu_password` is the password which we get from the form
            - `request.user.password` is the password which we get from the user who logged in; if both match it will be `True`
        - Then we checked new password and confirm new password; if it matched then we set the new password using `request.user.set_password(n_password)`
        - After changing password it will log out the user; So we used `from django.contrib.auth import update_session_auth_hash`
            - In `update_session_auth_hash` arguments are
                - request --> request
                - user --> request.user (which is current logged in user)
            - It update the session with new password

</details>

<details>
<summary>Day-36-Job Portal Project Recap 2</summary>

## Job Portal Project Recap 2

- Sign Up page
    - Each field with django messages
        - Profile photo
        - First name
        - Last name
        - Username
        - Password
        - Confirm password
        - Age
        - Gender
        - City
        - Country
        - Blood group
        - User type (Seeker,Recruiter)
            - Seeker extra info model
                - Seeker Profile (Qualification,Experience,Skills,Last education)
                - Education (name,year,institute)
                - Work Experience (Position,Company name,Duration)
            - Recruiter extra info model
                - Recruiter Profile (Company name,Company_location,Preferred communication)
            - Common info model 
                - Basic Info (Father Name,Mother name,Hobby,Languages)
                - Contact Info (Mobile number,Email,Address)
    - Warning message if user exists
- Sign In page
    - Each field with django messages
        - Username
        - Password
    - Sign in success message
    - Login failed warning message
- Dashboard page (Template mastering) - Include django messages in necessary places
    - Navbar with
        - Dashboard
        - Profile page (Template mastering)
            - View full profile info
            - Edit / Update Profile (success message on update profile)
            - Change Password (password change success message or warning if failed)
                - Current password
                - New password
                - Confirm New password
        - Log out
            - Log out success message
        - Seeker
            - Applied Job
            - Recent Job
        - Recruiter
            - Add Job (With below field)
                - Job title
                - Company name
                - Address
                - Company description
                - Job description
                - Qualification
                - Salary information
                - Deadline
                - Designation
                - Experience
            - Add job success message
        - View All Job
            - A table with action (view,delete,edit)
                - Seeker can only view
                - Recruiter will have all three action
            - Edit success message
            - Delete success message

### Notes

1. **While creating our CustomUserModel we have to import AbstractUser**
    - `from django.contrib.auth.models import AbstractUser`

2. **Add the CustomUserModel in `settings.py`**

    - `AUTH_USER_MODEL="JobApp.CustomUserModel"`
3. **Import `authenticate`,`login`,`logout` for user authentication and logout**

    - `from django.contrib.auth import authenticate,login,logout`

4. **To prevent a view without login Import login_required**
    - `from django.contrib.auth.decorators import login_required`

5. **To show messages import messages**

    - `from django.contrib import messages`

6. **Verify user to edit profile data by checking user current password using check_password**

    - `from django.contrib.auth.hashers import check_password`

7. **To make the user logged in after editing password use update_session_auth_hash**

    - `from django.contrib.auth import update_session_auth_hash`

8. **While creating JobModel add extra field `Created_by` using `ForeignKey` relationship**

    - `Created_by = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)`

9. **Create One To One relationship while creating related user info model using `OneToOneField` and include `related_name`; this related name will be very useful for updating,accessing model data****

    - `user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='recruiterprofilemodel')`

</details>

<details>
<summary>Day-37-Django MCQ Exam (11-05-2024)</summary>

## Day 37 Topics:
- Django MCQ Exam

### Django MCQ Exam

What is the purpose of the forms.ModelForm class in Django?

 - [ ] Define a form without a model
 - [ ] Create a form for a Django model
 - [ ] Specify form validation rules
 - [ ] Configure the form's display format and layout

    > [Answer](# "Create a form for a Django model")

Which Django command is used to create a new Django application?

 - [ ] python manage.py startapp
 - [ ] python createapp
 - [ ] django startproject
 - [ ] django createapp

    > [Answer](# "python manage.py startapp")

Which Django setting is used to specify the default database for the application?

 - [ ] DATABASE_ENGINE
 - [ ] DB_ENGINE
 - [ ] DATABASES
 - [ ] DEFAULT_DB
    > [Answer](# "DATABASES")

How do you include another app's URL patterns in your Django project's urls.py file?

 - [ ] include('app.urls')
 - [ ] add('app.urls')
 - [ ] import app.urls
 - [ ] use('app.urls')
    > [Answer](# "include('app.urls')")

What is the purpose of the HttpResponseRedirect class in Django?

 - [ ] Render HTML templates
 - [ ] Redirect to another URL
 - [ ] Redirect to another function
 - [ ] Handle form submissions

    > [Answer](# "Redirect to another URL")

What is the purpose of the STATIC_URL setting in settings.py?

 - [ ] Define the URL for static files
 - [ ] Specify the default static file storage backend
 - [ ] Configure static file compression
 - [ ] Set the root directory for static files

    > [Answer](# "Define the URL for static files")

In Django, what is the purpose of the middleware in the settings.py file?

 - [ ] Define middleware functions for the project
 - [ ] Configure global middleware settings
 - [ ] Enable or disable specific middleware components
 - [ ] Specify URL patterns for middleware
    > [Answer](# "Enable or disable specific middleware components")

How do you define a one-to-many relationship between two Django models?

 - [ ] ForeignKey
 - [ ] OneToManyField
 - [ ] RelationshipField
 - [ ] ManyToOneField

    > [Answer](# "ForeignKey")

What is the purpose of the choices option in a Django model field?

 - [ ] Define available options for the field
 - [ ] Set default choices for the field
 - [ ] Specify a default value for the field
 - [ ] Configure the display format for the field

    > [Answer](# "Define available options for the field")

In Django, which command is used to apply database migrations?

 - [ ] python manage.py makmigrations
 - [ ] python manage.py runmigrations
 - [ ] python manage.py migrate
 - [ ] django applymigrations
    > [Answer](# "python manage.py migrate")

What is the purpose of the blank option in a Django model field?

 - [ ] Allow the field to be blank in forms
 - [ ] Set a default value for the field
 - [ ] Define a blank option for select fields
 - [ ] Require the field to be blank in forms

    > [Answer](# "Allow the field to be blank in forms")

In Django, what is the purpose of the MEDIA_ROOT setting in settings.py?

 - [ ] Define the root URL for media files
 - [ ] Specify the default media storage backend
 - [ ] Define the root directory for uploaded media files
 - [ ] Configure media file permissions

    > [Answer](# "Define the root directory for uploaded media files")

Which of the following is used to define a URL pattern for a Django app's admin views?

 - [ ] admin_url()
 - [ ] path('admin/', admin.site.urls)
 - [ ] url('admin/', admin.site.urls)
 - [ ] admin.pattern()

    > [Answer](# "path('admin/', admin.site.urls)")

How do you customize the display of a model in the Django admin interface?

 - [ ] Override the __str__ method in the model
 - [ ] Use the list_display attribute in the model's admin class
 - [ ] Define a custom admin template
 - [ ] Specify the display option in the model's Meta class

    > [Answer](# "Use the list_display attribute in the model's admin class")

In Django, what is the purpose of the auto_now and auto_now_add options in a DateTimeField?

 - [ ] Specify the default date and time for the field
 - [ ] Automatically update the field to the current date and time
 - [ ] Set the field to be read-only
 - [ ] Define the format for displaying the date and time
    > [Answer](# "Automatically update the field to the current date and time")

What is the purpose of the AUTHENTICATION_BACKENDS setting in Django's settings.py?

 - [ ] Define the authentication method for the application
 - [ ] Specify the order of authentication backends to use
 - [ ] Configure user roles and permissions
 - [ ] Enable or disable user registration

    > [Answer](# "Specify the order of authentication backends to use")

How can you handle file uploads in Django forms?

 - [ ] Using the FileField in the form
 - [ ] Specifying upload_to attribute in the model's FileField
 - [ ] Defining a handle_upload method in the form
 - [ ] Configuring the UPLOAD_DIR setting in settings.py

    > [Answer](# "Using the FileField in the form")

Which Django module is used for creating forms in a Django application?

 - [ ] django.models.forms
 - [ ] django.forms
 - [ ] forms.py
 - [ ] models.forms

    > [Answer](# "django.forms")

What is the purpose of the settings.py file in a Django project?

 - [ ] Define application-specific settings
 - [ ] Configure project-wide settings
 - [ ] Specify URL patterns
 - [ ] Implement view functions

    > [Answer](# "Configure project-wide settings")

How do you create a superuser in Django's admin interface from the command line?

 - [ ] python manage.py createsuperuser
 - [ ] python manage.py superuser
 - [ ] django createsuperuser
 - [ ] django manage.py createsuperuser

    > [Answer](# "python manage.py createsuperuser")

Which of the following is used to define a URL pattern in urls.py for a Django view?

 - [ ] link()
 - [ ] url()
 - [ ] route()
 - [ ] path()

    > [Answer](# "path()")

Which Django template tag is used for URL reversing in a template?

 - [ ] {% url %}
 - [ ] {% reverse %}
 - [ ] {% navigate %}
 - [ ] {% redirect %}

    > [Answer](# "{% url %}")

In Django, what does the reverse() function do?

 - [ ] Reverse the order of elements in a list
 - [ ] Reverse the order of characters in a string
 - [ ] Generate a URL for a given view name
 - [ ] Reverse the order of items in a queryset

    > [Answer](# "Generate a URL for a given view name")

Which Django template tag is used to iterate through a list in a template?

 - [ ] {% loop %}
 - [ ] {% for %}
 - [ ] {% iterate %}
 - [ ] {% repeat %}

    > [Answer](# "{% for %}")

How can you perform database queries using raw SQL in Django?

 - [ ] Using the raw() method on a model's manager
 - [ ] Utilizing the queryset attribute in the model's Meta class
 - [ ] Creating a custom manager with a raw_query method
 - [ ] Configuring the USE_RAW_SQL setting in settings.py

    > [Answer](# "Using the raw() method on a model's manager")

How do you set a default value for a Django model field?

 - [ ] Using the default attribute in the model's field definition
 - [ ] Specifying a default value in the Meta class
 - [ ] Using the default parameter in the model's constructor
 - [ ] Setting the default value in the forms.py file

    > [Answer](# "Using the default attribute in the model's field definition")

What is the purpose of the on_delete parameter in a ForeignKey field in a Django model?

 - [ ] Specify the default value
 - [ ] Define the related model
 - [ ] Set the on-delete behavior for the relationship
 - [ ] Configure the field's display format

    > [Answer](# "Set the on-delete behavior for the relationship")

In Django, what is the primary purpose of the admin.py file?

 - [ ] Define database models
 - [ ] Configure the Django admin interface
 - [ ] Define URL patterns for the admin section
 - [ ] Implement view functions

    > [Answer](# "Configure the Django admin interface")

What does the login_required decorator do in Django?

 - [ ] Forces users to log out before accessing a view
 - [ ] Requires users to log in before accessing a view
 - [ ] Checks if a user has administrative privileges
 - [ ] Ensures that only superusers can access a view

    > [Answer](# "Requires users to log in before accessing a view")

What is the purpose of the related_name attribute in a Django model's ForeignKey field?

 - [ ] Specify the name of the related model
 - [ ] Define a reverse relationship from the related model
 - [ ] Set the order of related objects
 - [ ] Determine the default sorting for the ForeignKey field

    > [Answer](# "Define a reverse relationship from the related model")

</details>

<details>
<summary>Day-38-Python Day 09 While recap & For loop (12-04-2024)</summary>

## Day 38 Topics:
- Python Day 09

### Python day 09
- While recap & problem solving
- Array in python
- For loop

### problem solving
- Natural numbers from 10-1 in reverse
    ```python
    # i=10
    user_input=int(input("Input N: "))
    i=user_input-1
    print('Natural numbers from 10-1 in reverse: ')
    while i<=user_input:
        if i==0:
            break
        print(f'{i}',end=", ")
        i-=1
    ```

### Array in python
There are four types of array
- List
- Set
- Tupple
- Dictionary

List
- `x=[1,2]`

Set
- `x={1,2}`

Tupple
- `x=(1,2)`

Dictionary
- `x = {"key1": value1, "key2": value2}`

### For loop

```python
list_1 = ['apple', 'banana', 'cherry']
index = 0

for item in list_1:
    print(f"Index: {index}, Item: {item}")
    index += 1
```

</details>

<details>
<summary>Day-39-Python Day 10 Screen Recorder & For loop, List (13-05-2024)</summary>

## Day 39 Topics:
- Python Day 10
    - Screen Recorder with python
    - For loop & List

### Screen Recorder with python
- Screen recorder using pyautogui and open cv in `screenrecorder1.py`
    ```python
    import cv2
    import pyautogui
    from win32api import GetSystemMetrics
    import numpy as np
    import time

    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    dim = (width, height)
    # f = cv2.VideoWriter_fourcc(*"avc1") # best
    # f = cv2.VideoWriter_fourcc(*"H264") # medium
    f = cv2.VideoWriter_fourcc(*"mp4v") # normal
    file_name=input("Enter video file name: ")
    output = cv2.VideoWriter(f"{file_name}.mp4", f, 30.0, dim)
    now_start_time = time.time()
    dur = 5
    end_time = now_start_time + dur

    while True:
        image = pyautogui.screenshot()
        frame_1 = np.array(image)
        frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
        output.write(frame)
        c_time = time.time()
        if c_time > end_time:
            break
    output.release()
    print("__END__")
    ```
    - Here `avc1` and `H264` codec required `openh264-1.8.0-win64.dll` which can be downloaded from [openh264](https://github.com/cisco/openh264/releases/tag/v1.8.0)
    - More modification is done in `screenrecorder2.py` where pyqt5 added with start,pause,stop button

### For loop & List
- Skip a from the given string
    ```python
    fruit = "banana"
    for x in fruit:
        if x=="a":
            continue
        print(x,end=" ")
    else:
        print("\nEnded")
    ```
- Only print the `banana`
    ```python
    fruit = "bananajtjtrdfseefes"
    for x in fruit:
        if x=="j":
            break
        print(x,end=" ")
    else:
        print("\nEnded")
    ```
- Print `apple` & `cherry` only
    ```python
    fruits = ['apple','banana','cherry']
    for x in fruits:
        if x=="banana":
            continue
        print(x,end=" ")
    else:
        print("\nEnded")
    ```
- Print the nested list in normal text
    ```python
    fruits = [['alahi','almin','tansen'],'banana','cherry']
    for x in fruits:
        if isinstance(x, list):  # Check if the item is a list
            for i in x:
                print(i)
        else:
            print(x)
    ```
- Print each character from the nested list
    ```python
    fruits = [['tansen','alahi','almin'],'banana','cherry']
    for x in fruits:
        for i in x:
            for j in i:
                print(j)
    else:
        print("\nEnded")
    ```
- For loop with range
    ```python
    for x in range(0,100,10):
        print(x)
    ```

</details>

<details>
<summary>Day-40-Python Day 11 List Operations & Problem Solving (14-05-2024)</summary>

## Day 40 Topics:
- Django MCQ Exam 2
- Python Day 11
- Task

### Django MCQ Exam 2

Which of the following fields is used to represent a date and without time in Django models?

 - [ ] DateField
 - [ ] DateTimeField
 - [ ] TimeField
 - [ ] TimestampField

    > [Answer](# "DateField")

How do you represent an integer field that increments automatically with each new object created?

 - [ ] IntegerField with auto_increment=True
 - [ ] AutoField
 - [ ] IntegerField with auto_increment
 - [ ] PrimaryKeyField

    > [Answer](# "AutoField")

Which field type in Django models is used for storing large text content?

 - [ ] CharField
 - [ ] TextField
 - [ ] EmailField
 - [ ] URLField

    > [Answer](# "TextField")

In Django models, how do you define a primary key field explicitly?

 - [ ] primary_key=True
 - [ ] primary=True
 - [ ] pk=True
 - [ ] id=True

    > [Answer](# "primary_key=True")

Which attribute in a Django model is used to define the default ordering for queries?

 - [ ] order_by
 - [ ] default_order
 - [ ] ordering
 - [ ] default_sort

    > [Answer](# "ordering")

Which of the following is true regarding the null attribute in Django models?

 - [ ] It allows NULL values in the database for the field.
 - [ ] It forces the field to have a non-NULL value in the database.
 - [ ] It specifies a default value for the field.
 - [ ] It automatically generates a unique value for the field.

    > [Answer](# "It allows NULL values in the database for the field.")

How do you define a primary key field in Django models?

 - [ ] Using PrimaryKeyField.
 - [ ] Using AutoField.
 - [ ] Using IntegerField with primary_key=True
 - [ ] Using CharField with primary_key=True.

    > [Answer](# "Using AutoField.")

In Django ORM, what does the filter() method do?

 - [ ] Retrieves a single object by its primary key
 - [ ] Adds a WHERE clause to the SQL query
 - [ ] Orders the queryset by a specified field
 - [ ] Counts the number of objects in a queryset

    > [Answer](# "Adds a WHERE clause to the SQL query")

How do you represent a  precision  decimal number field in Django models?

 - [ ] FloatField
 - [ ] DecimalField
 - [ ] IntegerField
 - [ ] NumberField

    > [Answer](# "DecimalField")

How do you represent a time field in Django models?

 - [ ] DateField
 - [ ] DateTimeField
 - [ ] TimeField
 - [ ] TimestampField

    > [Answer](# "TimeField")

Which method is used to create a new object in the database using Django models?

 - [ ] insert()
 - [ ] new()
 - [ ] Save()
 - [ ] create()

    > [Answer](# "create()")

In Django models, how can you order a queryset in descending order based on a field?

 - [ ] sort('field')
 - [ ] order_by('-field')
 - [ ] order('field')
 - [ ] order_by('field')

    > [Answer](# "order_by('-field')")

Which of the following is a correct way to create a new instance of a Django model?

 - [ ] Model.create()
 - [ ] Model.objects.new()
 - [ ] Model.objects.create()
 - [ ] Model.new_instance()

    > [Answer](# "Model.objects.create()")

Which of the following statements is true regarding the unique attribute in Django models?

 - [ ] It ensures that the field's value is unique across all instances.
 - [ ] It enforces uniqueness only within the same model instance.
 - [ ] It specifies a unique constraint on the database level.
 - [ ] It automatically generates a unique value for the field.

    > [Answer](# "It ensures that the field's value is unique across all instances.")


Which method in a Django model is called when you want to delete an object?

 - [ ] delete()
 - [ ] remove()
 - [ ] destroy()
 - [ ] erase()

    > [Answer](# "delete()")

What does the CASCADE option of the on_delete parameter do?

 - [ ] Deletes the related object and all its dependencies.
 - [ ] Sets the foreign key value to NULL.
 - [ ] Raises an error if the related object is deleted.
 - [ ] Ignores the deletion of the related object.

    > [Answer](# "Deletes the related object and all its dependencies.")

How can you define a default value for a field in a Django model?

 - [ ] Using the value attribute.
 - [ ] Using the initial attribute
 - [ ] Using the default attribute.
 - [ ] Using the default_value attribute.

    > [Answer](# "Using the default attribute.")

Which field type in Django models is used for storing Boolean (true/false) values?

 - [ ] BooleanField
 - [ ] CharField
 - [ ] IntegerField
 - [ ] FloatField

    > [Answer](# "BooleanField")

What is the purpose of the verbose_name attribute in Django models?

 - [ ] It sets a custom name for the field in the admin interface.
 - [ ] It defines the maximum length of the field.
 - [ ] It specifies a help text for the field.
 - [ ] It specifies the type of data the field holds.

    > [Answer](# "It sets a custom name for the field in the admin interface.")

What does the editable attribute specify in Django models?

 - [ ] It allows the field to be edited in forms.
 - [ ] It forces the field to be read-only in forms.
 - [ ] It specifies a default value for the field.
 - [ ] It renames the field in the database.

    > [Answer](# "It allows the field to be edited in forms.")

### Python Day 11
- List operations

### List operations
- Length
   ```python
   my_list=['apple','banana','orange']
   print(len(my_list))
   ```
- Accesing list items from last index
   ```python
   my_list=['apple','banana','orange','juice','kiwi','melon']
   print(my_list[-6:-2])
   ```
- Append list items
   ```python
   my_list=['apple','banana','orange','juice','kiwi','melon']
   my_list[2]='cake'
   print(my_list)
   ```
- Append list items using insert
   ```python
   my_list=['apple','banana','orange','juice','kiwi','melon']
   my_list.insert(4,'mango')
   print(my_list)
   ```
- Append list items using append
   ```python
   my_list=['apple','banana','orange','juice','kiwi','melon']
   my_list.append('mango')
   print(my_list)
   ```
- Appending lists
   ```python
   my_list1=['apple','banana','orange']
   my_list2=['juice','kiwi','melon']

   concat_list=my_list2+my_list1
   my_list1.extend(my_list2)
   print(my_list1)
   print(concat_list)
   ```
- Appending list and tupple
   ```python
   my_list1=['apple','banana','orange']
   my_list2=('juice','kiwi','melon')

   my_list1.extend(my_list2)
   print(my_list1)
   ```
   > This will also converted to list

### Task
- Problem 01
   ```python
   myList=['Apple','Banana','Cherry','Pineapple']
   List1=['Orange','Purple','Lavender','Black','White']
   ```
   - Insert an item in the end of myList
   - Extend myList with List1
   - Append a new item on myList
   - Print only the fruits name when character start with a or A
- Problem 02
   - Input n numbers item(positive integer) in a list
   - Separate Even numbers from the list and store it in Even_List then sum the Even list number
   - Separate Odd numbers from the list and store it in Odd_List then sum the Odd list number
   - Summation the main_list
   - Check main_list summation == Even_list + Odd_list summation
   - If Equal print Hello.

### Solution 01
- Insert an item in the end of myList
   ```python
   myList.insert(len(myList),'Kiwi')
   ```
- Extend myList with List1
   ```python
   myList.extend(List1)
   ```
- Append a new item on myList
   ```python
   myList.append('Mango')
   ```
- Print only the fruits name when character start with a or A
   ```python
   for x in myList:
      if x[0]=='a' or x[0]=='A':
         print(x)
   ```

### Solution 02
- Solution of the problem 02
    ```python
    # main_list=[1,2,3,4,5]
    # print(f"Main List: {main_list}")

    main_list=[]
    Even_List=[]
    Odd_List=[]
    Main_List_Sum=0
    Even_List_Sum=0
    Odd_List_Sum=0

    user_input_count = int(input("How many positive integer number you want to input: "))

    for x in range(user_input_count):
        user_in = int(input("Enter list item: "))
        if user_in>=0:
            main_list.append(user_in)
        else:
            print(f"Only input positive integer, {user_in} is not positive integer")

    print(f"Main List: {main_list}")

    for x in main_list:
        if x%2==0:
            Even_List.append(x)
        else:
            Odd_List.append(x)
    print(f"Stored Even List: {Even_List}")
    print(f"Stored Odd List: {Odd_List}")

    for x in Even_List:
        Even_List_Sum+=x
    print(f"Sum of Even List: {Even_List_Sum}")

    for x in Odd_List:
        Odd_List_Sum+=x
    print(f"Sum of Odd List: {Odd_List_Sum}")

    Even_Odd_Sum = Even_List_Sum+Odd_List_Sum
    print(f"Sum of Even & Odd: {Even_Odd_Sum}")

    for x in main_list:
        Main_List_Sum+=x
    print(f"Sum of Main List: {Main_List_Sum}")

    if Main_List_Sum == Even_Odd_Sum:
        print("Hello")
    ```

- Solution of the problem 02 using only one for loop
    ```python
    # main_list=[1,2,3,4,5]
    # print(f"Main List: {main_list}")

    main_list=[]
    Even_List=[]
    Odd_List=[]
    Main_List_Sum=0
    Even_List_Sum=0
    Odd_List_Sum=0

    user_input_count = int(input("How many positive integer number you want to input: "))
    for x in range(user_input_count):
        user_in = int(input("Enter list item: "))
        if user_in>=0:
            main_list.append(user_in)
            if user_in%2==0:
                Even_List.append(user_in)
                Even_List_Sum+=user_in
            else:
                Odd_List.append(user_in)
                Odd_List_Sum+=user_in
            Even_Odd_Sum = Even_List_Sum+Odd_List_Sum
            Main_List_Sum+=user_in
        else:
            print(f"Only input positive integer, {user_in} is not positive integer")
    print(f"Main List: {main_list}")
    print(f"Stored Even List: {Even_List}")
    print(f"Stored Odd List: {Odd_List}")
    print(f"Sum of Even List: {Even_List_Sum}")
    print(f"Sum of Odd List: {Odd_List_Sum}")
    print(f"Sum of Even & Odd: {Even_Odd_Sum}")
    print(f"Sum of Main List: {Main_List_Sum}")
    if Main_List_Sum == Even_Odd_Sum:
        print("Hello")
    else:
        print("Not Equal")
    ```

</details>

<details>
<summary>Day-41-Python Day 12 & Motivational Session (15-05-2024)</summary>

## Day 41 Topics:
- Django MCQ Exam 3
- Python Day 12
- Motivational Session

### Django MCQ Exam 3

What is the purpose of the distinct() method in Django?

 - [ ] To remove duplicate objects from a queryset.
 - [ ] To select distinct fields from a queryset.
 - [ ] To ensure that a queryset is not empty.
 - [ ] To order the queryset in descending order.

    > [Answer](# "To remove duplicate objects from a queryset.")

You want to retrieve all books that are available for purchase. Which query would you use?

 - [ ] Book.objects.filter(available=True)
 - [ ] Book.objects.filter(availability=True)
 - [ ] Book.objects.filter(available="Yes")
 - [ ] Book.objects.filter(status="Available")

    > [Answer](# "Book.objects.filter(available=True)")

You want to retrieve all books that have been published in the years 2018, 2019, or 2020. Which query would you use?

 - [ ] Book.objects.filter(published_year=2018, published_year=2019, published_year=2020)
 - [ ] Book.objects.filter(published_year__in=[2018, 2019, 2020])
 - [ ] Book.objects.filter(published_year=[2018, 2019, 2020])
 - [ ] Book.objects.filter(published_year__range=(2018, 2020))

    > [Answer](# "Book.objects.filter(published_year__in=[2018, 2019, 2020])")

You want to retrieve all books whose title contains the word "Python". Which query would you use?

 - [ ] Book.objects.filter(title___contains="Python")
 - [ ] Book.objects.filter(title__like="Python")
 - [ ] Book.objects.filter(title__icontains="Python")
 - [ ] Book.objects.filter(title__ilike="Python")

    > [Answer](# "Book.objects.filter(title__icontains='Python')")

What does the exists() method do in Django?

 - [ ] Checks if a queryset is empty.
 - [ ] Checks if a queryset exists in the database.
 - [ ] Checks if a specific object exists in a queryset.
 - [ ] Checks if a specific field exists in a model.

    > [Answer](# "Checks if a queryset is empty.")

You want to retrieve the sum of all ratings for books in the database. Which method would you use?

 - [ ] Book.objects.sum('rating')
 - [ ] Book.objects.aggregate(Sum('rating'))
 - [ ] Book.objects.rating__sum()
 - [ ] Book.objects.aggregate(Total('rating'))

    > [Answer](# "Checks if a queryset is empty.")

You want to retrieve all books that are either available for purchase or have a rating of more than 4.5. Which query would you use?

 - [ ] Book.objects.filter(available=True || rating__gt=4.5)
 - [ ] Book.objects.filter(Q(available=True) | Q(rating__gt=4.5))
 - [ ] Book.objects.filter(available=True).filter(rating__gt=4.5)
 - [ ] Book.objects.filter(available=True | rating__gt=4.5)

    > [Answer](# "Book.objects.filter(Q(available=True) | Q(rating__gt=4.5))")

Suppose you have a Django model Book with fields title and author. What is the correct way to retrieve all books written by "John Doe"?

 - [ ] Book.objects.filter(author="John Doe")
 - [ ] Book.objects.get(author="John Doe")
 - [ ] Book.objects.all(author="John Doe")
 - [ ] Book.objects.find(author="John Doe")

    > [Answer](# "Book.objects.filter(author='John Doe')")

You need to retrieve all books published after the year 2000. Which query would you use?

 - [ ] Book.objects.filter(published_year__gt=2000)
 - [ ] Book.objects.filter(published_year__gte=2000)
 - [ ] Book.objects.filter(published_year__lt=2000)
 - [ ] Book.objects.filter(published_year__lte=2000)

    > [Answer](# "Book.objects.filter(published_year__gt=2000)")

Which method is used to perform an OR query in Django?

 - [ ] or_filter()
 - [ ] Q()
 - [ ] or()
 - [ ] filter_or()

    > [Answer](# "Q()")

Which method is used to retrieve the last object from a queryset in Django?

 - [ ] last_get()
 - [ ] get_last()
 - [ ] reverse().first()
 - [ ] order_by('-id').first()

    > [Answer](# "order_by('-id').first()")

In Django, what is the purpose of the values() method in a queryset?

 - [ ] To return a list of field values for each object in the queryset.
 - [ ] To return a single value from the queryset.
 - [ ] To filter the queryset based on specific values.
 - [ ] To sort the queryset in ascending order.

    > [Answer](# "To return a list of field values for each object in the queryset.")

Which method would you use to retrieve a random object from a Django model queryset?

 - [ ] random()
 - [ ] get_random()
 - [ ] order_by('?').first()
 - [ ] random_object()

    > [Answer](# "order_by('?').first()")

You want to retrieve all books that are authored by "John Doe" and published after the year 2015. Which query would you use?

 - [ ] Book.objects.filter(author="John Doe").filter(published_year__gt=2015)
 - [ ] Book.objects.filter(author="John Doe" && published_year__gt=2015)
 - [ ] Book.objects.filter(author="John Doe" & published_year__gt=2015)
 - [ ] Book.objects.filter(Q(author="John Doe") & Q(published_year__gt=2015))

    > [Answer](# "Book.objects.filter(Q(author='John Doe') & Q(published_year__gt=2015))")

You want to retrieve the first ten books from a queryset in Django. Which method would you use?

 - [ ] first(10)
 - [ ] limit(10)
 - [ ] slice(10)
 - [ ] [:10]

    > [Answer](# "[:10]")

Which method would you use to retrieve the last ten objects from a queryset in Django?

 - [ ] last(10)
 - [ ] tail(10)
 - [ ] reverse()[:10]
 - [ ] order_by('-id')[:10]

    > [Answer](# "order_by('-id')[:10]")

You want to retrieve the average rating of all books in the database. Which method would you use?

 - [ ] Book.objects.average('rating')
 - [ ] Book.objects.aggregate(Avg('rating'))
 - [ ] Book.objects.avg('rating')
 - [ ] Book.objects.rating__avg()

    > [Answer](# "Book.objects.aggregate(Avg('rating'))")

Which method is used to count the number of objects in a queryset in Django?

 - [ ] size()
 - [ ] length()
 - [ ] count()
 - [ ] total()

    > [Answer](# "count()")

You want to retrieve all books that have either been published by "Publisher A" or "Publisher B". Which query would you use?

 - [ ] Book.objects.filter(publisher="Publisher A" | "Publisher B")
 - [ ] Book.objects.filter(publisher="Publisher A").filter(publisher="Publisher B")
 - [ ] Book.objects.filter(Q(publisher="Publisher A") | Q(publisher="Publisher B"))
 - [ ] Book.objects.filter(publisher="Publisher A" || publisher="Publisher B")

    > [Answer](# "Book.objects.filter(Q(publisher='Publisher A') | Q(publisher='Publisher B'))")

You want to retrieve all books that have been published between the years 2010 and 2020. Which query would you use?

 - [ ] Book.objects.filter(published_year__gte=2010).filter(published_year__lte=2020)
 - [ ] Book.objects.filter(published_year__gte=2010, published_year__lte=2020)
 - [ ] Book.objects.filter(published_year__range=(2010, 2020))
 - [ ] Book.objects.filter(published_year__gt=2010, published_year__lt=2020)

    > [Answer](# "Book.objects.filter(published_year__range=(2010, 2020))")

### Python Day 12
- List remove method
    ```python
    fruits = ['apple', 'banana', 'cherry']
    fruits.remove("banana")
    print(fruits)
    ```
- List pop method
    ```python
    fruits = ['apple', 'banana', 'cherry']
    fruits.pop()
    print(fruits)
    ```
- Del statement
    ```python
    fruits = ['apple', 'banana', 'cherry']
    del fruits[1]
    print(fruits)
    ```
- List clear method
    ```python
    fruits = ['apple', 'banana', 'cherry']
    fruits.clear()
    print(fruits)
    ```
### Motivational Session
- Wrong direction
    - Mobile
    - Non-interested direction
- Right direction
    - Study
        - Problems (not actually)
            - Focus
            - Concentration
            - Distraction
            - Time management 
        - Problem (main) - Interest
            - No strong reason
    - Life purpose (Everyday)
    - A strong reason (With emotion)
    - BEST (`B`elief, `E`xecution, `S`kills, `T`ransformation)
        - Belief System
            - Quote from **British olympic coach (Harry Andrews) - 1903**
            - For 53 years this quote remain true
                - Four Minute Mile break 1956
                - 22k person break it after `Four Minute Mile break`
                - `3.43 second` current record
            - After 1971 (oneday match - 60 overs - run average 200..250..300)
                - It was belief that a single person can't make double century
                - But Sachin break it then Birendra Shahbag..then another...then another...
        - Belief system create Attitude (Positive)
            - Even though lion is the king but it does not have:
                - Speed
                - Power
        - Knowledge is power (no actually)
        - Execution of knowledge is power!
            - Start with small execution
                - Virat Kohli story (mirror self ask)
        - Skills
            - Madness
            - Hunger
            - Anger
            - Example:
                - Elon Musk madness on selling paypal and going on rent
                - T. A. Edison trying 9999 times and succeed on 10000
                - Jack Ma - Tried to become KFC waiter, Now he is the founder of alibaba
                - Sachin first debut story (16 years old)
        - Transformation
            - Through training
                - Trainer (personal development) meets his friend story (tennis training)
        - Task
            - Loudly say `I AM HAPPY`
            - Three task (Next 30 Days)
                - Affirmation (What you want in life , find the reason - give yourself time)
                - Life Goal (After 1 month where you want to see yourself)
                    - Note 2 task that you want to complete everyday
                - Gratification - Thankful to the creator (Allah)
    > NO ONE CAN STOP YOU BUT YOURSELF

</details>

<details>
<summary>Day-41-Practise Django Project Question</summary>

## Project Name: Blog Project
- **Sign Up page**
    - Profile Pic
    - Name
    - Username
    - Password
    - Confirm password
    - User Type (Author,Reader)
    > - Name should only contain character
    > - Password must be combined with (character,number,special character) - **Optional**
    > - Warning message if user already exists
- **Models**:
    - **Custom User Model**
        - Add field according to signup page
    - **Common info model**
        - Basic Info (Father Name,Mother name,Languages)
        - Contact Info (Mobile number,Email,Address)
    - **Reader extra info model**
        - Reader Profile Model(Hobby,Last education)
        - Interest Model(Interest_name,description,category)
    - **Author extra info model**
        - Author Profile (biography,social_media,writing_category)
    - **Blog Model**
        - Add field according to below requirement
    - **Contact Us Model**
        - Add field according to below requirement
- **Sign In page**
    - Username
    - Password
    > - Username not found warning message
    > - Login failed warning message
    > - Sign in success message
- **Dashboard page (Template mastering)**
    - **Navbar**:
        - **Dashboard**
        - **Profile page (Template mastering)**
            - View full profile info
            - Edit / Update Profile
            - Change Password
                - Current password
                - New password
                - Confirm New password
            > - Password not match warning
            > - Password change success message
            > - New and Confirm password not match
            > - Profile update success message
        - **Log out**
            - Log out
            > - Log out success message
        - **Blog**
            - Create new post
                - Title
                - Content
            - Edit post
            - Delete post
            - View single post
        - **View All blog post**
        - **Contact Us**
            - Name
            - Email
            - Message
            > - Success message after form submission (submitted data will be stored in database)

> [!CAUTION]
> 
> **Do Not use Chatgpt**
>
> **Use W3school (For frontend pages) / Django Documentation**

> [!TIP]
> 1. **While creating our CustomUserModel we have to import AbstractUser**
> 2. **Add the CustomUserModel in `settings.py`**
> 3. **Import `authenticate`,`login`,`logout` for user authentication and logout from `django.contrib.auth`**
> 4. **To prevent a view without login Import `login_required`**
> 5. **To show messages import `messages` from `django.contrib`**
> 6. **Verify user to edit profile data by checking user current password using `check_password` from `django.contrib.auth.hashers`**
> 7. **To make the user logged in after editing password use `update_session_auth_hash` from `django.contrib.auth`**
> 8. **While creating BlogModel add extra field `Created_by` using `ForeignKey` relationship**
> 9. **Create One To One relationship while creating related user info model using `OneToOneField` and include `related_name`; this related name will be very useful for updating,accessing model data**

</details>

<details>
<summary>Day-42-Python Day 13, Python MCQ Exam & Problem solving (16-05-2024)</summary>

## Day 42 Topics:
- Python MCQ Exam
- Python Day 13
- Problem Solving
- Task

### Python MCQ Exam

What is the output of the following code?
```python
list = [1, 2, 3, 4, 5]
print(list[2])
```

 - [ ] 1
 - [ ] 2
 - [ ] 3
 - [ ] 4

    > [Answer](# "3")

What is the output of the following code?
```python
list = [0, 1, 2, 3, 4]
print(list[1:3])
```

 - [ ] [0, 1, 2]
 - [ ] [1, 2, 3]
 - [ ] [1, 2]
 - [ ] [2, 3]

    > [Answer](# "[1, 2]")

What is the output of the following code?
```python
for i in range(3):
    for j in range(3):
        if i == j:
            print(i, j)
```

 - [ ] 1 1 2 2
 - [ ] 0 0 1 1
 - [ ] 0 1 2
 - [ ] 0 0 1 1 2 2

    > [Answer](# "0 0 1 1 2 2")

Which of the following is true about nested loops?

 - [ ] Only for loops can be nested
 - [ ] Only while loops can be nested.
 - [ ] for and while loops can be nested within each other.
 - [ ] Loops cannot be nested.

    > [Answer](# "for and while loops can be nested within each other.")

What is the output of the following code?
```python
list = [1, 2, 3, 4]
new_list = [x*2 for x in list]
print(new_list)
```

 - [ ] [1, 4, 9, 16]
 - [ ] [2, 4, 6, 8, 10]
 - [ ] [1, 2, 3, 4]
 - [ ] [2, 4, 6, 8]

    > [Answer](# "[2, 4, 6, 8]")

What is the output of the following code?
```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

 - [ ] 0 0 0 1 1 0 1 1 2
 - [ ] 0 1 1 0
 - [ ] 0 0 1 1 1 0 1 1
 - [ ] 0 0 0 1 1 0 1 1

    > [Answer](# "0 0 0 1 1 0 1 1")

Which statement is true about lists in Python?

 - [ ] Lists are immutable.
 - [ ] Lists are mutable
 - [ ] Lists can only contain elements of the same type.
 - [ ] Lists cannot contain other lists.

    > [Answer](# "Lists are mutable")

What is the output of the following code?
```python
for i in range(2):
    for j in range(2):
        print(i, j, end=' ')
```

 - [ ] 0 0 0 1 1 0 1 1
 - [ ] 0 0 1 0 1 1
 - [ ] 0 1 1 0
 - [ ] 0 0 0 1 1 0 1 01

    > [Answer](# "0 0 0 1 1 0 1 1")

Which method removes the last element from a list?

 - [ ] list.remove()
 - [ ] list.pop()
 - [ ] list.delete()
 - [ ] list.discard()

    > [Answer](# "list.pop()")

How do you append an element to a list in Python?

 - [ ] list.append(4)
 - [ ] list.add(4)
 - [ ] list = {1, 2, 3}
 - [ ] list = 1, 2, 3

    > [Answer](# "list.append(4)")

What is the correct syntax for a for loop in Python?

 - [ ] for i in 1 to 10:
 - [ ] for i in range(10):
 - [ ] for (i=0; i<10; i++):
 - [ ] for i from 1 to 10:

    > [Answer](# "for i in range(10):")

Which statement will correctly check if a number is even in a nested if condition?

 - [ ] if num % 2 = 0:
 - [ ] if num % 2 == 0:
 - [ ] if (num % 2) == 0
 - [ ] Both b and c

    > [Answer](# "if num % 2 == 0:")

What is the output of the following code?
```python
list = [1, 2, 3, 4]
for i in range(len(list)):
    list[i] *= 2
print(list)
```

 - [ ] [1, 4, 9, 16]
 - [ ] [2, 4, 6]
 - [ ] [2, 4, 6, 8]
 - [ ] [1, 2, 3, 4]

    > [Answer](# "[2, 4, 6, 8]")

What is the output of the following code?
```python
for i in range(3):
    print(i)
```

 - [ ] 0 1 2
 - [ ] 0 1 2 3
 - [ ] 1 2 3
 - [ ] None of them

    > [Answer](# "0 1 2")

What is the output of the following code?
```python
for i in range(3):
    if i == 1:
        continue
    print(i)
```

 - [ ] 0 1 2
 - [ ] 0 2
 - [ ] 1 2
 - [ ] 0 1

    > [Answer](# "0 2")

Which of the following is a valid list comprehension?

 - [ ] [x for x in range(5)]
 - [ ] [x in range(5)]
 - [ ] [for x in range(5)]
 - [ ] [x range(5)]

    > [Answer](# "[x for x in range(5)]")

What is the output of the following code?
```python
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
```

 - [ ] 1 2 3
 - [ ] 0 1 2
 - [ ] 0 1 2 3
 - [ ] 0 1 2 3 4

    > [Answer](# "0 1 2")

What is the output of the following code?
```python
i = 0
while i < 3:
    print(i)
    i += 1
```

 - [ ] 0 1 2
 - [ ] 1 2 3
 - [ ] 0 1 2 3
 - [ ] 1 2

    > [Answer](# "0 1 2")

How do you check if an element is in a list?

 - [ ] if 3 in list:
 - [ ] if list.has(3):
 - [ ] if list.contains(3):
 - [ ] if 3 inside list:

    > [Answer](# "if 3 in list:")

What is the output of the following code?
```python
list = [1, 2, 3, 4]
for i in range(len(list)):
    for j in range(i):
        print(list[j], end=' ')
    print()
```

 - [ ] 1 1 2 1 2 3 1 2 3 4
 - [ ] 1 2 1 2 3 1 2 3 4
 - [ ] 1 1 2 2 3 3 4 4
 - [ ] 1 2 1 2 3 1 2 3

    > [Answer](# "1 2 1 2 3 1 2 3 4")

Which of the following creates a list in Python?

 - [ ] list = [1, 2, 3]
 - [ ] list = (1, 2, 3)
 - [ ] list = {1, 2, 3}
 - [ ] list = 1, 2, 3

    > [Answer](# "list = [1, 2, 3]")

### Python day 13
- Loop lists
    ```python
    thislist = ["apple", "banana", "cherry"]
    [print(x) for x in thislist]
    ```
- Appending item to new list
    ```python
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []
    for x in fruits:
        if "a" in x:
            newlist.append(x)
    print(newlist)
    ```
- Appending item to new list (with list comprehension)
    ```python
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print(newlist)
    ```
- Taking list item from user
    ```python
    total_user_input = int(input("How many number you want to input: "))
    userList = []
    for x in range(total_user_input):
        user_input = int(input())
        userList.append(user_input)
    print(userList)
    ```
- Counting list items
    ```python
    myList = [0, 1, 2, 6, 3, 4, 3, 3, 6]
    counts = {}

    for item in myList:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for item, count in counts.items():
        print(f"{item}: {count}")
    ```
### Problem Solving
- Problem 01 (Searching a specific item in a list)
    ```python
    myList=[0,1,2,6,3,4,3,3,6]
    ```
    > In the given list if 5 number item occur 3 times print hello
- Problem 02
    ```python
    myList=[0,1,2,6,3,4,3,3,6]
    ```
    > In the given list if 5 number item is equal to the length of list print hello
- Problem 03
    ```python
    myList=[0,1,2,6,3,4,3,3,6]
    ```
    > In the given list remove duplicate

- Solution to Problem 01
    ```python
    myList=[0,1,2,6,3,4,3,3,6]
    count=0
    fifth_item = myList[5-1]
    for x in myList:
        if fifth_item==x:
            count+=1
            if count >= 3:
                print("Hello")
    ```
- Solution to Problem 02
    ```python
    '''
    myList=[0,1,2,6,3,4,3,3,6]
    In the given list if 5 number item is equal to the length of list print hello
    '''

    myList=[0,1,2,6,3,4,3,3,6]

    fifth_item=myList[5-1]
    print(f"Fifth item is: {fifth_item}")

    list_length=len(myList)
    print(f"List length is: {list_length}")

    if fifth_item==list_length:
        print("hello")
    else:
        print(f"Fifth item: {fifth_item} is not equal to list length {list_length}")
    ```
- Solution to Problem 03
    ```python
    '''
    myList=[0,1,2,6,3,4,3,3,6]
    In the given list remove duplicate
    '''
    myList=[0,1,2,6,3,4,3,3,6]
    index = 0
    while index<len(myList):
        item = myList[index]
        for duplicate_index in range(index + 1, len(myList)):
            if myList[duplicate_index] == item:
                myList.pop(duplicate_index)
                break
        else:
            index += 1
    print("List with duplicates removed:", myList)
    ```

### Task
- Solve HackerRank basic problem

### HackerRank (Easy)
- HackerRank 01 (Easy): Say "Hello, World!" With Python
    ```python
    if __name__ == '__main__':
        print("Hello, World!")
    ```
- HackerRank 02 (Easy): Python If-Else
    ```python
    import math
    import os
    import random
    import re
    import sys

    if __name__ == '__main__':
        n = int(input().strip())
        if n%2!=0:
            print("Weird")
        else:
            if 2<=n<=5:
                print("Not Weird")
            elif 6<=n<=20:
                print("Weird")
            elif n>20:
                print("Not Weird")
    ```

</details>

<details>
<summary>Day-43-Python Day 14 Problem Solving (18-05-2024)</summary>

## Day 43 Topics:
- Python Day 14
    - List of problem
    - Problem solution

### List of problem
- Searching from list
- Summation list value
- Reverse list item
- Maximum number and minimum number from list
- Prime number
- Prime number series
- Factorial
- Digit reverse
- Palindrome number
- Armstrong number
- Armstrong number series
- Leap year
- Pattern
- Find the sequence of numbers
- Fibonacci series
- Geomatric series
- Arithmatic series
- Bubble sort (Any sorting algorithm)

### Question:
- Programming contest:
  - Solve 10 problem in 3 hour
- Exam:
  - Write the output of the given program

### Problem solution
- Searching from list
    ```python
    # Searching from list
    myList=[1,2,3,5,3,4,4,6,2,1,1]
    search = 2
    count=0
    for item in myList:
        if search == item:
            count+=1
    print(f"Item {search} found {count} times")
    ```
- Summation list value
    ```python
    # Summation list value
    myList=[1,2,3,5,3,4,4,6,2,1,1]
    sum=0
    for item in myList:
        sum+=item
    print(f"list summation: {sum}")
    ```
- Reverse list item
    ```python
    # list item reverse
    myList=[1,2,3,4,5,6,7,8,9]
    reverseList=[]
    for x in range(len(myList)):
        index=x+1
        reverseList.append(myList[-index])
    print(reverseList)
    ```
- Maximum number and minimum number from list
    ```python
    # Maximum number from list
    myList=[11,3,100,2,1,222,4,2]
    max=0
    for item in myList:
        if item>max:
            max=item
    print(max)
    ```
    ```python
    # Minimum number from list
    myList=[1,11,3,100,2,222,4,2]
    min=0
    for item in myList:
        temp=item
        for j in myList:
            if j<temp:
                min=j
    print(min)
    ```
- Prime number
    ```python
    # prime number check
    user_input = 29
    if user_input%2!=0:
        print(f"{user_input} is prime number")
    else:
        print(f"{user_input} is not a prime number")
    ```
- Prime number series
    ```python
    # prime number series
    user_input = 100
    prime_numbers=[]
    for x in range(user_input):
        if x%2!=0:
            if x==1:
                x+=1
            prime_numbers.append(x)
    print(prime_numbers)
    ```
- Factorial
    ```python
    # Factorial
    user_input=5
    fact=1
    for x in range(1,user_input+1):
        fact*=x
    print(fact)
    ```
- Digit reverse
    ```python
    # Digit reverse
    myDigit=324345
    digit_str=str(myDigit)
    digit_reverse=""
    for i in range(len(digit_str)):
        index=i+1
        digit_reverse += digit_str[-index]

    print(f"Original digit: {myDigit}")
    print(f"Reverse digit: {int(digit_reverse)}")
    ```
- Palindrome number
    ```python
    # palindrome check
    myDigit=323
    digit_str=str(myDigit)
    digit_reverse=""
    for i in range(len(digit_str)):
        index=i+1
        digit_reverse += digit_str[-index]
    if int(digit_reverse) == myDigit:
        print("It is a Palindrome number")
    print(f"Original digit: {myDigit}")
    print(f"Reverse digit: {int(digit_reverse)}")
    ```
- Armstrong number
    ```python
    # Armstrong number
    num = 8208
    sum=0
    for x in str(num):
        sum += int(x)**len(str(num))
    print(sum)
    ```
- Armstrong number series logic building
    ```python
    # logic building code for creating the series of armstrong number
    armstrong_series1=[407]
    for i in armstrong_series1:
        check_num = i
        sum=0
        for j in str(check_num):
            sum+=int(j)**len(str(check_num))
        if sum == check_num:
            print(check_num)
    ```
    - Before working with range I build the logic with single number first from a list
    ```python
    # armstrong series
    armstrong_series =[]
    for i in range(1000):
        check_num = i
        sum=0
        for j in str(check_num):
            sum+=int(j)**len(str(check_num))
        if sum == check_num:
            armstrong_series.append(check_num)
    print(armstrong_series)
    ```
- Leap year
    ```python
    # Leap year
    user_input=[2020, 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600]
    for x in user_input:
        if x%100==0:
            if x%400==0:
                print(f"{x} is leap year")
            else:
                print(f"{x} is not leap year")
        elif x%4==0:
            print(f"{x} is leap year")
        else:
            print(f"{x} is not leap year")
    ```
- Patterns
    ```python
    '''
    Right Half Pyramid
    *
    * *
    * * *
    * * * *     
    * * * * *
    '''
    for x in range(1,6):
        print(x*"*")
    ```
- Find the sequence of numbers,Geomatric,Arithmatic series
    ```python
    # sequence 2,4,6,8,10
    sequence=[]
    start=2
    for x in range(10):
        sequence.append(start)
        start+=2
    print(sequence)
    ```
- Fibonacci series
    ```python
    # Fibonacci series
    user_input = 10
    a = 0
    b = 1
    fibonacci = []
    for i in range(user_input):
        fibonacci.append(a)
        next_number = a + b
        a = b
        b = next_number
    print(fibonacci)
    ```

</details>

<details>
<summary>Day-44-Python Day 15 List Method Continues & Function Intro (19-05-2024)</summary>

## Day 44 Topics:
- Python Day 15
    - Insert instead of append
    - List Comprehension
    - List sorting
    - List copy
    - Function
    - Bubble sort

### Python Day 15
- Insert instead of append
    ```python
    # insert instead of append
    myList=["banana","mango","orange","kiwi"]
    newList=[]
    i=0
    for item in myList:
        if "a" in item:
            newList.insert(i,item)
            i+1
    print(newList)
    ```
- List Comprehension
    ```python
    # List comprehension
    myList = ["kiwi","orange"]
    newList = [x if "a" in x else "not present" for x in myList]
    newList = [x for x in myList if "a" in x]
    print(newList)
    newList = [x.upper() for x in myList if "a" in x]
    print(newList)
    ```
- List sorting
    ```python
    # List sorting
    myList = [2,5,3,1,6,9,6,5]
    # ascending
    myList.sort()
    print(myList)
    # decending
    myList.sort(reverse=True)
    print(myList)

    myList2=["banana","15","Kiwi","cherry"]
    myList2.sort(key=str.lower)
    print(myList2)
    ```
- List copy
    ```python
    # List copy
    myList = [2,5,3,1,6,9,6,5]
    newlist=myList.copy()
    print(newlist)
    ```
- Function
    ```python
    def my_function():
        print("Hello from my function")
        
    my_function()
    ```
- Bubble sort
    ```python
    # Define an array of numbers
    numbers = [67, 44, 82, 17, 20]

    # Get the total number of elements in the array
    total_numbers = len(numbers)

    # Print the array before sorting
    print("Array before Sorting:")
    print(numbers)

    # Iterate through each number in the array to sort them
    for i in range(total_numbers):
        # Keep track of whether any swaps occurred in this pass
        did_swap = False

        # Go through each pair of adjacent numbers in the array
        for j in range(0, total_numbers - i - 1):
            # Check if the current number is greater than the next number
            if numbers[j] > numbers[j + 1]:
                # If so, swap the positions of the numbers
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                did_swap = True  # Mark that a swap occurred

        # If no swaps occurred in this pass, the array is sorted
        if not did_swap:
            break

    # Print the array after sorting
    print("Array after Sorting:")
    print(numbers)
    ```

</details>

<details>
<summary>Day-45-Python Day 16 Function Class & Object (20-05-2024)</summary>

## Day 45 Topics:
- Python Day 15
    - Function recap
    - More usage of function
    - Class - Object

### More usage of function
- Arbitrary *kwargs
    ```python
    # Arbitrary *kwargs
    def my_function(*names):
        print(type(names))
        print(list(names))

    my_function("Mango","Orange")
    ```
- Problem: print all child name in single line
    ```python
    # print all child name in single line
    def my_function(*names):
        print("The youngest child are:",end=" ")
        for x in names:
            if x == names[-1]:
                print(x,end=".")
            else:
                
                print(x,end=",")

    my_function("Emil","Tobias","Linus")
    ```
- Arbitrary as dictionary **kwargs
    ```python
    # arbitrary as dictionary **kwargs
    def my_function(**kids):
        print(kids)
        print(type(kids))

    my_function(first="John",second="Doe")
    ```
- Function return
    ```python
    # Function return
    def my_function(x):
        return 5*x

    user_input=int(input("Enter a number: "))
    answer=my_function(3)
    print(answer)
    ```
- Problem: print each name later individually using nested loop
    ```python
    # print each name later individually using nested loop
    def my_function(fname,lname):
        for names in fname,lname:
            print(names)
            for j in names:
                print(j)

    my_function("Alahi","Tansennn")
    ```
- Problem: Print type of all arguments
    ```python
    # print type of all arguments
    def my_function(**food):
        # for key, value in food.items():
        #     print(f"Type: {type(value)}")
        #     print(value)
        for key, value in food.items():
            print(f"Type: {type(value)}")
            print(value)

    food_list=["Mango","Orange","Apple"]
    food_tuple=("Mango","Orange","Apple")
    food_set={"Mango","Orange","Apple"}
    food_dict={"food1":"Mango","food2":"Orange","food3":"Apple"}

    my_function(food_list=food_list)
    my_function(food_tuple=food_tuple)
    my_function(food_set=food_set)
    my_function(food_dict=food_dict)
    ```
- Class - Object
  - Inside class defined variable are attribute
  - Inside class function are called method
  - From class we get object
- Class object creation
    ```python
    # Class object creation
    class MyClass:
        x=5

    p1 = MyClass()
    print(p1.x)
    MyClass.x=80
    print(p1.x)
    p1.x=8
    print(p1.x)

    id = MyClass()
    age = MyClass()
    length = MyClass()

    id.x=1
    print(id.x)
    age.x=22
    print(age.x)
    length.x=100
    print(length.x)
    ```

</details>

<details>
<summary>Day-46-Python Day 17 Recursion Lambda (21-05-2024)</summary>

## Day 46 Topics:
- Python Day 17
    - Recursion
    - Recursion problem
    - Lambda Intro

### Recursion
- Recursion - A function that can call itself
    ```python
    # recursion
    def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

    print("\n\nRecursion Example Results")
    tri_recursion(1)
    ```
- Recursion problem: sum of given number
    ```python
    # recursion problem: sum of given number
    def sum(num):
    if num>0:
        summation = num+sum(num-1)
    else:
        summation=0
    return summation
    print(sum(10))
    ```
- Lambda Intro
    ```python
    x = lambda a: a + 10
    print(x(5))

    x = lambda a,b: a + b
    print(x(5,10))
    ```
    - A small anonymous function
    - Can take any number of arguments, but can only have one expression

</details>

<details>
<summary>Day-46-Day-46-Job Portal Project Recap 3</summary>

## Job Portal Project Recap 3

- Sign Up page
    - Each field with django messages
        - Profile photo
        - First name
        - Last name
        - Username
        - Password
        - Confirm password
        - Age
        - Gender
        - City
        - Country
        - Blood group
        - User type (Seeker,Recruiter)
            - Seeker extra info model
                - Seeker Profile (Qualification,Experience,Skills,Last education)
                - Education (name,year,institute)
                - Work Experience (Position,Company name,Duration)
            - Recruiter extra info model
                - Recruiter Profile (Company name,Company_location,Preferred communication)
            - Common info model 
                - Basic Info (Father Name,Mother name,Hobby,Languages)
                - Contact Info (Mobile number,Email,Address)
    - Warning message if user exists
- Sign In page
    - Each field with django messages
        - Username
        - Password
    - Sign in success message
    - Login failed warning message
- Dashboard page (Template mastering) - Include django messages in necessary places
    - Navbar with
        - Dashboard
        - Profile page (Template mastering)
            - View full profile info
            - Edit / Update Profile (success message on update profile)
            - Change Password (password change success message or warning if failed)
                - Current password
                - New password
                - Confirm New password
        - Log out
            - Log out success message
        - Seeker
            - Applied Job
            - Recent Job
        - Recruiter
            - Add Job (With below field)
                - Job title
                - Company name
                - Address
                - Company description
                - Job description
                - Qualification
                - Salary information
                - Deadline
                - Designation
                - Experience
            - Add job success message
        - View All Job
            - A table with action (view,delete,edit)
                - Seeker can only view
                - Recruiter will have all three action
            - Edit success message
            - Delete success message

### Solution
- Create project : `django-admin startproject jobProject`
- Create app:
    - Go to project directory: `cd jobroject`
    - Now create app: `py manage.py startapp jobApp`
- Add app name in `settings.py`
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'jobApp',
    ]
    ```
> Previously in this step we did migration but as we gonna create custom user from `AbstractUser` so we will create that model first then we will do the migration step
- Create user model using the given field in `signup` page
    - First create `signup.html` page
    - Create a folder `templates` in project directory where `manage.py` exists
    - Add this `templates` in `TEMPLATES`'s `DIRS`
        - `'DIRS': [BASE_DIR, "templates"],`
        - Now we will create all the required `.html` file in `templates` directory
    - Signup page:
        - Now create `signup.html` with the mentioned fields
            - Profile photo
            - First name
            - Last name
            - Username
            - Password
            - Confirm password
            - Age
            - Gender
            - City
            - Country
            - Blood group
            - User type (Seeker,Recruiter)
        - Now create a file `views.py` in project directory
            - Create a function `signup`
                ```python
                from django.shortcuts import render,redirect

                def signup(request):
                    return render(request,"signup.html")
                ```
            - Add url path for `signup` in `urls.py`
                ```python
                from django.contrib import admin
                from django.urls import path
                from jobProject.views import signup

                urlpatterns = [
                    path('admin/', admin.site.urls),
                    path('signup/',signup,name='signup'),
                ]
                ```
        - Now we will be able to see `signup` page live in browser
        - Now let's update the `signup` function to receive the info given by user to store it in model. Now we need the model so let's create it first then update the `signup` function
        - Create `CustomUserModel` in `models.py`
            ```python
            from django.db import models
            from django.contrib.auth.models import AbstractUser
            # Create your models here.
            class CustomUserModel(AbstractUser):
                profilePhoto = models.ImageField(upload_to='static/user_profile')
                age=models.CharField(max_length=100)
                GENDER=[
                    ('male','Male'),
                    ('female','Female'),
                    ('others','Others'),
                ]
                gender=models.CharField(choices=GENDER,max_length=100)
                city=models.CharField(max_length=100)
                country=models.CharField(max_length=100)
                bloodGroup=models.CharField(max_length=100)
                USER_TYPE=[
                    ('seeker','Job Seeker'),
                    ('recruiter','Job Recruiter'),
                ]
                userType = models.CharField(choices=USER_TYPE,max_length=100)
                
                def __str__(self):
                    return self.username
            ```
            - while creating model we know that there is image to save and show, in order to make it work we have to add `MEDIA_URL` and `STATICFILES_DIRS`. First add `STATICFILES_DIRS` in `settings.py`
                ```python
                STATICFILES_DIRS = [
                    BASE_DIR / "static",
                ]
                ```
            - Now in `urls.py` add `MEDIA_URL`
                ```python
                from django.conf import settings
                from django.conf.urls.static import static

                urlpatterns = [
                    # ... the rest of your URLconf goes here ...
                ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                ```
        - Register `CustomUserModel` in `admin.py`
            ```python
            from django.contrib import admin
            from jobApp.models import CustomUserModel
            # Register your models here.
            class CustomUserModelDisplay(admin.ModelAdmin):
                list_display=['username','user']
            admin.site.register(CustomUserModel,CustomUserModelDisplay)
            ```
            - We extra added `CustomUserModelDisplay` class to see the `CustomUserModel` in a formatted way where `userType`,`user`
        - Add `CustomUserModel` in `settings.py`
            - `AUTH_USER_MODEL = 'jobApp.CustomUserModel'`
        - Now we will migrate
            - `py manage.py makemigrations jobApp`
            - `py manage.py migrate jobApp`
            - `py manage.py makemigrations`
            - `py manage.py migrate`
        - Now let's create superuser
            - `py manage.py createsuperuser`
        - Now modify the `signup` function to get the form data and save it in `CustomUserModel`
            ```python
            from django.shortcuts import render,redirect
            from jobApp.models import CustomUserModel

            def signup(request):
                if request.method == "POST":
                    profilePhoto = request.FILES.get('profilePhoto')
                    first_name = request.POST.get('first_name')
                    last_name = request.POST.get('last_name')
                    username = request.POST.get('username')
                    password = request.POST.get('password')
                    confirmPassword = request.POST.get('confirmPassword')
                    age = request.POST.get('age')
                    gender = request.POST.get('gender')
                    city = request.POST.get('city')
                    country = request.POST.get('country')
                    bloodGroup = request.POST.get('bloodGroup')
                    userType = request.POST.get('userType')
                    
                    if password==confirmPassword:
                        user = CustomUserModel.objects.create_user(
                            profilePhoto=profilePhoto,
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            password=password,
                            age=age,
                            gender=gender,
                            city=city,
                            country=country,
                            bloodGroup=bloodGroup,
                            userType=userType,
                        )
                        user.save()
                        return redirect('signin')
                return render(request,"signup.html")
            ```
            - Here before we save it in our model we checked if `password` and `confirmPassword` matched or not
            - After successful signup it will redirect to `signin` page; Now our next step is creating the `signin` page
    - Signin page:
        - Create `signin.html` page using below field
            - username
            - password
        - Create `signin` function in `views.py`
            ```python
            def signin(request):
                return render(request,'signin.html')
            ```
        - Add url path for `signin` in `urls.py`
            ```python
            path('',signin,name='signin'),
            ```
        - Now modify the `signin` function to work
            ```python
            def signin(request):
                if request.method == "POST":
                    username=request.POST.get('username')
                    password=request.POST.get('password')
                    
                    user = authenticate(
                        username=username,
                        password=password
                    )
                    if user:
                        login(request,user)
                        return redirect('dashboard')
                return render(request,'signin.html')
            ```
            - Here `authenticate`, `login` is imported:
                - `from django.contrib.auth import authenticate,login`
    - Dashboard page:
        - While creating dashboard we will do template mastering
            - Create a `base.html`
                - This will contain the base html contain and every time we create another html page we will extends it
                - It will include the content which is repeated. e.g:`navbar.html`
            - Create `navbar.html`
                - This will have the navbar contain only and will be include in `base.html`
            - Create `dashboard.html`
                - This will `extends` the `base.html` 
                - Inside block contain it will have its own content
        - Create `dashboard` function in `views.py`
            ```python
            def dashboard(request):
                return render(request,'dashboard.html')
            ```
        - Add `dashboard` path in `urls.py`'s `urlpatterns`
            ```python
            path('dashboard/',dashboard,name='dashboard'),
            ```
    - Logout:
        - First create a function `logoutpage`
            > We can't name it `logout` as it is already a function which we import
            ```python
            def logoutpage(request):
                logout(request)
                return redirect('signin')
            ```
            - Here `logout` is imported
                - `from django.contrib.auth import logout`
        - Add url path for `logoutpage` in `urls.py`
            ```python
            path('logoutpage/',logoutpage,name='logoutpage'),
            ```
        - Add `logoutpage` in `navbar.html`
        ```html
        <li style="float:right"><a href="{% url 'logoutpage' %}">Logout</a></li>
        ```
        - Now there is a problem when logout we can still access dashboard path. To solve it let's make the user needed to be log in to access it by using `required_login`
            ```python
            @login_required
            def dashboard(request):
                return render(request,'dashboard.html')
            ```
            - Here we used `@login_required` which is imported:
                - `from django.contrib.auth.decorators import login_required`
        - Now we have to add the login url in `settings.py`
            `LOGIN_URL='signin'`
    - Profile page:
        - First create `profile.html` page 
        - Now create `profile` function in `views.py`
            ```python
            def profile(request):
                return render(request,'profile.html')
            ```
        - Add url path for `profile` in `urls.py`
            ```python
            path('profile/',profile,name='profile'),
            ```
        - Add `profile` in `navbar.html`
            ```html
            <li style="float:right"><a class="active" href="{% url 'profile' %}">Profile</a></li>
            ```
        - Now in `profile.html` page we will access the data from the model using `{{user.field_name_from_the_model}}` e.g: `{{user.profilePhoto}}`
        - Now we will do template mastering where `profile.html` will be master template for profile and cut the part where others info will be shown and make it `block profileinfo` to show the specific content on that part. we will create below pages where `profile.html` will be extends and `block profileinfo` will hold their specific contents
            - `profileinfo.html` - To show profile info which user fill up in signup and access those using `{{user.field_name_from_the_model}}` - Here Model is `CustomUserModel`
            - `recruiterprofile.html` - This will show the content from the `RecruiterProfileModel` where will will access the data `{{user.related_name.field_name_from_the_model}}`
            - `seekerprofile.html` - This will show the content from the `SeekerProfileModel` where will will access the data `{{user.related_name.field_name_from_the_model}}`
            - `seekereducation.html` - This will show the content from the `SeekerEducationModel` where will will access the data `{{user.related_name.field_name_from_the_model}}`
            - `seekerworkex.html` - This will show the content from the `SeekerWorkExModel` where will will access the data `{{user.related_name.field_name_from_the_model}}`
            - `basicinfo.html` - This will show the content from the `BasicInfoModel` where will will access the data `{{user.related_name.field_name_from_the_model}}`
            - `contactinfo.html` - This will show the content from the `ContactModel` where will will access the data `{{user.related_name.field_name_from_the_model}}`
        - Profile edit:
            - To edit profile we will create a form page `editprofile.html` where we will add all the model data there which we created for profile
            - While editing we will access the data in our function as below
                - `request.user.field_name_from_the_model` - This is for `CustomUserModel`
                - `request.user.related_name.field_name_from_the_model` - Others model data will be update using this where related name is important to write
                - Every time data is assigned we will save that
    - Add job & Create job:
        - To add job we will create a directory `recruiter` where we will create `addjob.html` form which will contain below fields:
            - Job title
            - Company name
            - Address
            - Company description
            - Job description
            - Qualification
            - Salary information
            - Deadline
            - Designation
            - Experience
        - While creating `editjob.html` we will do the same
        - Now to make it work we will do that same as others where a function,url etc will be created just like others
    - Delete,Edit,View:
        - This functionalities will be created based on `id` , by getting specific id we implement that
    - Messages:
        - To add messages we will create `messages.html` where message will be shown and it will be included where we need to show the message
        - In `views.py` we will import the `messages` from `from django.contrib import messages`
        - Now create a dictionaries of messages
            ```python
            all_messages ={
                "signup_success":"Successfully signed up",
                "signin_success":"Successfully signed in",
                "name_warning":"Name can only contain letters",
                "username_warning":"username can only contain letters and number",
                "username_warning2":"Username Already exists",
                "password_warning":"Password and confirm password not matched!",
                "age_warning":"You need to be 18 Years or above",
                "signin_warning":"Credentials not match",
                "username_warning3":"Username does not exists",
                "addjob_success":"Job added successfully",
                "editjob_success":"Job updated successfully",
                "logout_success":"Log out successful",
            }
            ```
        - This message will be accessed using `messages.success(request,all_messages['signup_success'])`
    - Change Password:
        - To change password we will create a `changepassword.html` form and include below field
            - Current Password
            - New Password
            - Confirm New Password
        - Just like other this page will be rendered and create the url
        - Now in function we will first check the current password with logged in user password using `check_password`
        - Then we will check if New Password and Confirm New Password is same or not
        - If both are same then we will change the password by setting the password to the current user: `request.user.set_password(new_password)` then save it `request.user.save()`
        - Now as password change it will auto log out in order to prevent it we can use `update_session_auth_hash` which is imported from `from django.contrib.auth` and to use it we update the current user session `update_session_auth_hash(request,request.user)` and show the success message

</details>

<details>
<summary>Day-47-Python Day 18 Lambda, Class Object (23-05-2024)</summary>

## Day 47 Topics:
- Python Day 18
  - Lambda
  - Tuple methods
  - Dictionary methods
  - Class Object 
    - Object are instance
    - Inheritance
    - Multi level Inheritance
    - Multiple Inheritance
    - constructor - a method which is called automatically when class is called

### Lambda
- Creating a normal function then converting it to lambda
  ```python
  # normal function

  def x(a):
      return a*3
  result = x(5)
  print(result)

  # Lambda
  x =lambda a: a*3
  result = x(5)
  print(result)
  ```
- Lambda problem 1: sum of 5 number
  ```python
  # Lambda problem 1: sum of 5 number
  x = lambda a,b,c,d,e: a+b+c+d+e
  result = x(1,2,3,4,5)
  print(result)
  ```
- Lambda Anonymous function inside another function
  ```python
  # Lambda Anonymous function inside another function
  def myfunc(n):
    return lambda a : a * n

  mydoubler = myfunc(2)
  mytripler = myfunc(3)

  print(mydoubler(11)) 
  print(mytripler(11))
  ```
- Lambda problem 2 : Sum of 3 number using Lambda
  ```python
  # Lambda problem 2 : Sum of 3 number using Lambda
  def myfunc(x,y,z):
    return lambda a,b,c : a+b+c+x+y+z

  mydoubler = myfunc(1,1,1)
  mytripler = myfunc(2,2,2)

  print(mydoubler(1,2,3)) 
  print(mytripler(4,5,6))
  ```
### Tuple methods
- problem 3: what is the index of 8 when it occur 2nd time
  ```python
  # problem: what is the index of 8 when it occur 2nd time
  thistuple = (1, 3, 4, 8, 4, 3, 2, 4, 8, 4, 3)
  count = 0
  i=0
  for x in thistuple:
      if x == 8:
          i += 1
      if x==8 and i == 2:
          print(count)
      count+=1
  ```
- problem 3: what is the index of 8 when it occur 2nd time (another approach)
  ```python
  # problem: what is the index of 8 when it occur 2nd time (another approach)
  thistuple = (1,3,4,8,4,3,2,4,8,4,3,8,2,5,6,8,5,3,4,8)
  count = 0
  for i in range(len(thistuple)):
      if thistuple[i] == 8:
          count+=1
      if thistuple[i]==8 and count == 5:
          print(i)
  ```
### Dictionary methods
- Dictionary in one line 
  ```python
  # dictionary in one line
  thisdict = dict(name = "tansen",age = 23,country = "Bangladesh")
  print(thisdict)
  ```
### Class Object 
- creating class and object
  ```python
  # creating class and object
  class myClass():
      x=5
  p1 = myClass()
  p1.x=10
  print(p1.x)
  ```
- Normal Inheritance
  ```python
  # normal Inheritance
  class a:
      x=10
  class b(a):
      pass
  obj1 = b()
  print(obj1.x)
  ```
- Multi level Inheritance
  ```python
  # Multi level Inheritance
  class c:
      y=20
  class a(c):
      x=10
  class b(a):
      pass
  obj1 = b()
  print(obj1.x)
  print(obj1.y)
  ```
- Multiple Inheritance
  ```python
  # Multiple Inheritance
  class c():
      y=20
  class a():
      x=10
  class b(a,c):
      pass
  obj1 = b()
  print(obj1.x)
  print(obj1.y)
  ```
- Python constructor
  ```python
  # python constructor
  class Person:
      def __init__(s):
          print("I will be called auto")
      def another(s):
          print("I won't be call auto")

  obj1=Person()
  obj1.another()
  print(obj1)
  ```

</details>

<details>
<summary>Day-48-Rest API Framework, Serializer (25-05-2024)</summary>

## Day 48 Topics:
- API
- Serialization of API
- Django Shell
- Brainstorming
- Task
- Signup using terminal

### API
- `API` : Application Programming Interface
- `MVC` : Model View Controller
- `MVT` : Model View Template where it is related to MVC --> Model, View(Template), Controller(View)
- URL ⇔ Template ⇔ View(controller) ⇔ Database
- Serializers is used to convert the data in api json format
- API are made on models
- Django Rest Framework Quickstart
  - [django-rest-framework-quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)

### Serialization of API
- Create project and app
- Now by following the quickstart
  - install django rest framework: `pip install djangorestframework`
  - Include `'rest_framework'` in `settings.py` file `INSTALLED_APPS`
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'myApp',
    ]
    ```
  - In `models.py` create a model:
    ```python
    from django.db import models

    # Create your models here.
    class StudentModel(models.Model):
        name=models.CharField(max_length=100)
        department=models.CharField(max_length=100)
        email=models.EmailField(max_length=100)
        
        def __str__(self):
            return self.name
    ```
  - Create `serializers.py` file in app directory
  - Now add those code
    ```python
    from django.contrib.auth.models import Group, User
    from rest_framework import serializers
    from .models import StudentModel

    class StudentSerializer(serializers.Serializer):
        name=serializers.CharField(max_length=100)
        department=serializers.CharField(max_length=100)
        email=serializers.EmailField(max_length=100)

        def create(self, validated_data):
            return StudentModel.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.email)
            instance.department = validated_data.get('department', instance.content)
            instance.email = validated_data.get('email', instance.created)
            instance.save()
            return instance
    ```
    - This code is from the [Django Rest Framework Documentation Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/) and [Django Rest Framework Serializers](https://www.django-rest-framework.org/api-guide/serializers/#saving-instances)
### Django Shell
- Now using shell to create new object; First open shell
- `py manage.py shell`
  - `from myApp.models import StudentModel`
  - `from myApp.serializers import StudentSerializer`
  - `from rest_framework.renderers import JSONRenderer`
  - `from rest_framework.parsers import JSONParser`
  - `s=StudentModel(name="Tansen",department="CSE",email="aatansen@gmail.com")`
  - `s.save()`
Now let's view the data:
- `serializer=StudentSerializer(s)`
- `serializer.data`
- `objs=StudentModel.objects.all()`
- `objs`
  ```python
  for i in objs:
    print(i.name,i.department,i.email)
  ```

### Brainstorming
- In Dhaka City at Dhanmondi. There are 4 friends. They have to go home. They need to cross Dhanmondi bridge but bridge structure is weak. At a time 2 people can cross the road. For crossing the road they have a one torch. Torch can not be thrown
- Ranajit can cross the bridge 1 min
- Rejoine can cross the bridge 2 min
- Mamun can cross the bridge 5 min
- Jessica can cross the bridge 10 min
    > Solve it in a lowest time (17 minutes)

### Task
- Preskool template setup in Django

### Signup using terminal
- `py manage.py shell`
  - `from lawApp.models import CustomUserModel`
  - `CustomUserModel.objects.create_user(username='tansen',password='123')`

</details>

<details>
<summary>Day-49-Preskool Project Template Mastering & CRUD (26-05-2024)</summary>

## Day 49 Topics:
- School project template mastering recap
- fieldsets in `admin.py`

### School project template mastering recap
- > It is done similar way of resume project 

### fieldsets in `admin.py`
- We can modify the view of admin page 
    ```python
    from django.contrib import admin
    from schoolApp.models import *
    # Register your models here.

    class CustomUserModelDisplay(admin.ModelAdmin):
        list_display=['username','user_type']
        search_fields=['username','user_type']
        fieldsets=[
        ( 
                "User",
                {"fields":["username","email","user_type"],}
            ),
        ]

    admin.site.register(CustomUserModel,CustomUserModelDisplay)
    ```

</details>

<details>
<summary>Day-50-Python Day 19 Exam, Preskool Project 02 Add student (27-05-2024)</summary>

## Day 50 (27-05-2024) Topics:
- Python Day-19
  - [Loop and functions MCQ Exam](#loop-and-functions-mcq-exam)
  - [Class, Object and Inheritance MCQ Exam](#class-object-and-inheritance-mcq-exam)
- [Preskool Project 02 Add student](#preskool-project-02-add-student)

### Loop and functions MCQ Exam

What is the purpose of the return statement in a function?

 - [ ] To end the function execution
 - [ ] To specify the output of the function
 - [ ] To pass control to the caller
 - [ ] All of the above

    > [Answer](# "All of the above")

How do you call a function named myFunc in Python?

 - [ ] myFunc
 - [ ] myFunc[]
 - [ ] myFunc()
 - [ ] call myFunc

    > [Answer](# "myFunc()")

How can you exit an infinite loop in Python?

 - [ ] Using exit()
 - [ ] Using break
 - [ ] Using continue
 - [ ] Using return

    > [Answer](# "Using break")

How can you exit an infinite loop in Python?

 - [ ] Using exit()
 - [ ] Using break
 - [ ] Using continue
 - [ ] Using return

    > [Answer](# "Using break")

What is the output of the following code?
```python
def greet(name):
    return "Hello, " + name
print(greet("Alice"))
```

 - [ ] name
 - [ ] Hello Alice
 - [ ] Hello, Alice
 - [ ] Hello

    > [Answer](# "Hello, Alice")

Which function is used to generate a sequence of numbers in Python for loops?

 - [ ] generate()
 - [ ] loop()
 - [ ] range()
 - [ ] sequence()

    > [Answer](# "range()")

Which of the following is the correct way to define a function in Python?

 - [ ] myFunc() = def
 - [ ] def myFunc():
 - [ ] def myFunc:
 - [ ] function myFunc():

    > [Answer](# "def myFunc():")

What is the output of the following code?
```python
def add(a, b):
    return a + b
print(add(2, 3))
```

 - [ ] 2 + 3
 - [ ] 23
 - [ ] 5
 - [ ] None

    > [Answer](# "5")

Which of the following statements is true about functions in Python?

 - [ ] Functions can be defined inside loops
 - [ ] Functions cannot have default arguments
 - [ ] Functions can return multiple values
 - [ ] Functions must return a value

    > [Answer](# "Functions can return multiple values5")

What is the output of the following code?
```python
for i in range(1, 10, 3):
    print(i, end=' ')
```

 - [ ] 1 3 6 9
 - [ ] 1 4 7 10
 - [ ] 1 4 7
 - [ ] 1 2 3 4 5 6 7 8 9

    > [Answer](# "1 4 7")

How do you specify that a function does not return any value?

 - [ ] def myFunc():
 - [ ] def myFunc(): return
 - [ ] def myFunc(): None
 - [ ] def myFunc(): pass

    > [Answer](# "def myFunc():")

What is the output of the following code?
```python
def func(a, b):
    return a * b
print(func(2, 3))
```

 - [ ] 6
 - [ ] 5
 - [ ] 23
 - [ ] 8

    > [Answer](# "6")

What is the output of the following code?
```python
i = 0
while i < 3:
    print(i)
    i += 2
```

 - [ ] 0 1 2
 - [ ] 0 2
 - [ ] 0 1
 - [ ] 0 2 4

    > [Answer](# "0 2")

What is the output of the following code?
```python
def test():
    return "test"
result = test()
print(result)
```

 - [ ] result
 - [ ] error
 - [ ] None
 - [ ] test

    > [Answer](# "test")


Which method can be used to loop through both keys and values of a dictionary?

 - [ ] dict.items()
 - [ ] dict.values()
 - [ ] dict.keys()
 - [ ] dict.all()

    > [Answer](# "dict.items()")

What is the output of the following code?
```python
def func(x):
    print(x + 1)
func(5)
```

 - [ ] 6
 - [ ] 5
 - [ ] 4
 - [ ] None

    > [Answer](# "6")

What is the output of the following code?
```python
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
    print(i)
```

 - [ ] 1 2
 - [ ] 1 2 3
 - [ ] 1 2 4 5
 - [ ] 1 2 3 4 5

    > [Answer](# "1 2")

Which of the following is true about functions in Python?

 - [ ] They must return a value
 - [ ] They cannot return any values
 - [ ] They can only return one value
 - [ ] They can return multiple values

    > [Answer](# "They can return multiple values")

What is the output of the following code?
```python
def func(x, y=2, z=3):
    return x + y + z
print(func(1, z=4))
```

 - [ ] 5
 - [ ] 10
 - [ ] 7
 - [ ] 8

    > [Answer](# "7")

What is the output of the following code?
```python
def myFunc(a, b=2):
    return a + b
print(myFunc(3))
```

 - [ ] 3
 - [ ] 5
 - [ ] 2
 - [ ] Error

    > [Answer](# "5")

What is the correct way to define a function with two parameters in Python?

 - [ ] def myFunc[a, b]:
 - [ ] def myFunc(a, b):
 - [ ] def myFunc(a; b):
 - [ ] def myFunc(a b):

    > [Answer](# "def myFunc(a, b):")

What is the output of the following code?
```python
for i in range(2, 5):
    print(i, end=' ')
```

 - [ ] 2 3 4
 - [ ] 2 3 4 5
 - [ ] 3 4 5
 - [ ] 2 3

    > [Answer](# "2 3 4")

What is the output of the following code?
```python
x = 10
while x > 0:
    x -= 3
    if x == 4:
        break
print(x)
```

 - [ ] 4
 - [ ] 1
 - [ ] 10
 - [ ] 7

    > [Answer](# "4")

Which of the following statements about functions is true?

 - [ ] Functions in Python cannot be called within other functions
 - [ ] Functions in Python cannot return a value
 - [ ] Functions in Python can have no parameters
 - [ ] Functions in Python must have parameters

    > [Answer](# "Functions in Python can have no parameters")

What is the output of the following code?
```python
for i in range(3):
    print(i)
```

 - [ ] 0 1 2 3 4
 - [ ] 0 1 2
 - [ ] 1 2 3
 - [ ] 0 1 2 3

    > [Answer](# "0 1 2")

How can you iterate over a list in Python?

 - [ ] for i in length(myList):
 - [ ] for i in range(myList):
 - [ ] while i in myList:
 - [ ] for i in myList:

    > [Answer](# "for i in myList:")

[⬆️ Go to top](#day-50-27-05-2024-topics)

### Class, Object and Inheritance MCQ Exam

How do you access attributes of an object in Python?

 - [ ] object(attribute)
 - [ ] object->attribute
 - [ ] object.attribute
 - [ ] object

    > [Answer](# "object.attribute")

How do you call the parent class constructor explicitly in the child class constructor?

 - [ ] parentclass.init()
 - [ ] super().init()
 - [ ] base.init()
 - [ ] parent.init()

    > [Answer](# "super().init()")

Which of the following is true about multiple inheritance in Python?

 - [ ] Multiple inheritance causes an error.
 - [ ] A class can inherit from only one parent class.
 - [ ] A class can inherit from multiple parent classes.
 - [ ] Python does not support multiple inheritance.

    > [Answer](# "A class can inherit from multiple parent classes.")

Which method should be overridden to define custom behavior for the addition operator (+) in a class?

 - [ ] addition()
 - [ ] sum()
 - [ ] add()
 - [ ] plus()

    > [Answer](# "add()")

What keyword is used to inherit from a parent class in Python?

 - [ ] inherits
 - [ ] derives
 - [ ] superclass
 - [ ] class

    > [Answer](# "class")

What is the output of the following code?
```python
class Base:
    def __init__(self):
        self.a = "Base"

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.b = "Derived"

obj = Derived()
print(obj.a, obj.b)
```

 - [ ] Derived Base
 - [ ] Base Derived
 - [ ] Derived Derived
 - [ ] Base Base

    > [Answer](# "Base Derived")

Which function is used to determine the type of an object in Python?

 - [ ] gettype()
 - [ ] object_type()
 - [ ] type()
 - [ ] what_type()

    > [Answer](# "type()")

What is the output of the following code?
```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

obj = B()
obj.method()
```

 - [ ] A method
 - [ ] B method
 - [ ] Error
 - [ ] None

    > [Answer](# "B method")

Which of the following statements is used to create an object in Python?

 - [ ] obj = Object()
 - [ ] obj = class()
 - [ ] obj = MyClass()
 - [ ] obj = create(MyClass)

    > [Answer](# "obj = MyClass()")

How can you call a method from a parent class in Python?

 - [ ] super().method
 - [ ] super().method()
 - [ ] base.method()
 - [ ] parent.method()

    > [Answer](# "super().method()")

What is the output of the following code?
```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

c = Child()
c.greet()
```

 - [ ] Error
 - [ ] Hello from Child
 - [ ] Hello from Parent
 - [ ] Nothing

    > [Answer](# "Hello from Parent")

What is the output of the following code?
```python
class MyClass:
    class_var = 0
    def __init__(self):
        MyClass.class_var += 1

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.class_var)
```

 - [ ] 1
 - [ ] 2
 - [ ] 0
 - [ ] Error

    > [Answer](# "2")

Which method can be overridden to provide custom behavior for object string representation in Python?

 - [ ] string()
 - [ ] reprstr()
 - [ ] repr()
 - [ ] str()

    > [Answer](# "str()")

What is the output of the following code?
```python
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(5)
print(obj.value)
```

 - [ ] 5
 - [ ] 0
 - [ ] None
 - [ ] Error

    > [Answer](# "5")

What is the output of the following code?
```python
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(5)
print(obj.value)
```

 - [ ] 5
 - [ ] 0
 - [ ] None
 - [ ] Error

    > [Answer](# "5")

What is the term used to describe a blueprint for creating objects in Python?

 - [ ] Package
 - [ ] Module
 - [ ] Class
 - [ ] Function

    > [Answer](# "Class")

What is the output of the following code?
```python
class MyClass:
    def __init__(self, x=1):
        self.x = x

    def set_x(self, x):
        self.x = x

obj = MyClass()
obj.set_x(5)
print(obj.x)
```

 - [ ] 1
 - [ ] 5
 - [ ] None
 - [ ] Error

    > [Answer](# "5")

What is the output of the following code?
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()
```

 - [ ] Animal speaks
 - [ ] Error
 - [ ] Dog barks
 - [ ] Nothing

    > [Answer](# "Dog barks")

Which of the following statements is true about the super() function?

 - [ ] It is used to modify the base class.
 - [ ] It is used to delete the parent class.
 - [ ] It is used to call methods of the base class from the derived class.
 - [ ] It returns an instance of the base class.

    > [Answer](# "It is used to call methods of the base class from the derived class.")

What does the pass keyword do in a class definition?

 - [ ] It exits from a method
 - [ ] It allows you to create an empty class or method.
 - [ ] It skips the execution of a method.
 - [ ] It defines a method

    > [Answer](# "It allows you to create an empty class or method.")

Which method is called when an instance of a class is created?

 - [ ] init()
 - [ ] create()
 - [ ] new()
 - [ ] start()

    > [Answer](# "init()")

What is the special method in Python that is used for initializing objects?

 - [ ] new()
 - [ ] create()
 - [ ] init()
 - [ ] start()

    > [Answer](# "init()")

What does the term 'inheritance' imply in object-oriented programming?

 - [ ] It implies that an object can be converted to another object.
 - [ ] It implies that classes can contain multiple objects.
 - [ ] It implies that a new class can inherit properties and behaviors from an existing class.
 - [ ] It implies that objects can contain other objects.

    > [Answer](# "It implies that a new class can inherit properties and behaviors from an existing class.")

Which of the following is not a valid method to use with a Python class?

 - [ ] add
 - [ ] str
 - [ ] init
 - [ ] delete

    > [Answer](# "delete")

Which keyword is used to define a method in a Python class?

 - [ ] class
 - [ ] function
 - [ ] method
 - [ ] def

    > [Answer](# "def")

Which of the following is true about instance variables and class variables?

 - [ ] Class variables are unique to each method of a class.
 - [ ] Instance variables are unique to each instance of a class.
 - [ ] Class variables are unique to each instance of a class.
 - [ ] Instance variables are shared among all instances of a class.

    > [Answer](# "Instance variables are unique to each instance of a class.")

[⬆️ Go to top](#day-50-27-05-2024-topics)

### Preskool Project 02 Add student
- To add student we created a form `studentadd.html` where required fields are taken
- Create a custom model `CustomUserModel` to save the user login information with user type
- According to the fields in `studentadd.html` create a model `StudentAddModel`
- This model will have all the required info including a relational field with custom model which is `user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)`
- Now after getting data from the form in `studentadd` function first we have to save the `username`,`password` and `user_type` in `CustomUserModel`
- Save other info in `StudentAddModel` along with `user`
    ```python
    def studentadd(request):
        department =DepartmentAddModel.objects.all()
        sessions =SessionAddModel.objects.all()
        dept_sessDict={
            'department':department,
            'sessions':sessions,
        }
        if request.method=="POST":
            First_Name=request.POST.get('First_Name')
            Last_Name=request.POST.get('Last_Name')
            Email=request.POST.get('Email')
            Gender=request.POST.get('Gender')
            Date_of_Birth=request.POST.get('Date_of_Birth')
            Department_Name=request.POST.get('Department_Name')
            Religion=request.POST.get('Religion')
            Mobile_Number=request.POST.get('Mobile_Number')
            Session_Name=request.POST.get('Session_Name')
            Student_Image=request.FILES.get('Student_Image')
            Father_Name=request.POST.get('Father_Name')
            Father_Occupation=request.POST.get('Father_Occupation')
            Father_Mobile=request.POST.get('Father_Mobile')
            Father_Email=request.POST.get('Father_Email')
            Mother_Name=request.POST.get('Mother_Name')
            Mother_Occupation=request.POST.get('Mother_Occupation')
            Mother_Mobile=request.POST.get('Mother_Mobile')
            Mother_Email=request.POST.get('Mother_Email')
            Present_Address=request.POST.get('Present_Address')
            Permanent_Address=request.POST.get('Permanent_Address')
            Username=request.POST.get('Username')
            Password=request.POST.get('Password')
            CPassword=request.POST.get('CPassword')
            
            if Password==CPassword:
                student_custom=CustomUserModel.objects.create_user(
                    username=Username,
                    password=Password,
                    user_type="3"
                )
                student_custom.save()
                student=StudentAddModel.objects.create(
                    First_Name=First_Name,
                    Last_Name=Last_Name,
                    Email=Email,
                    Gender=Gender,
                    Date_of_Birth=Date_of_Birth,
                    Department_Name=Department_Name,
                    Religion=Religion,
                    Mobile_Number=Mobile_Number,
                    Session_Name=Session_Name,
                    Student_Image=Student_Image,
                    Father_Name=Father_Name,
                    Father_Occupation=Father_Occupation,
                    Father_Mobile=Father_Mobile,
                    Father_Email=Father_Email,
                    Mother_Name=Mother_Name,
                    Mother_Occupation=Mother_Occupation,
                    Mother_Mobile=Mother_Mobile,
                    Mother_Email=Mother_Email,
                    Present_Address=Present_Address,
                    Permanent_Address=Permanent_Address,
                    user = student_custom
                )
                student.save()
                return redirect('studentlist')
        return render(request,'student/studentadd.html',dept_sessDict)
    ```
    - Here notice `user = student_custom` which is important to understand; It is saving user login information

[⬆️ Go to top](#day-50-27-05-2024-topics)

</details>

<details>
<summary>Day-51-Preskool 03 Subject,Student,Teacher,department (28-05-2024)</summary>

## Day 51 (28-05-2024) Topics:
- [In Subject add section of html page add department field](#in-subject-add-section-of-html-page-add-department-field)
- [Add Student department field correction](#add-student-department-field-correction)
- [Teacher Model relationship with Department model](#teacher-model-relationship-with-department-model)
- [Student - Teacher count in Department dashboard](#student---teacher-count-in-department-dashboard)
- [Task](#task)

### In Subject add section of html page add department field
- In pre-template there are many unnecessary fields. So we need to clean some of the fields
- As per requirement we need to add the department field in subject section

### Add Student department field correction
- In add student model Make foreign key relationship with department model
- As department model will be in student model so need to create the department model first
- Create `DepartmentAddModel`
    ```python
    class DepartmentAddModel(models.Model):
        Department_Name=models.CharField(max_length=100)
        Head_of_Department=models.CharField(max_length=100)
        created_at=models.DateField(auto_now=True)
        updated_at=models.DateField(auto_now_add=True)
        
        def __str__(self):
            return self.Department_Name
    ```
- Now create `StudentAddModel`
    ```python
    class StudentAddModel(models.Model):
        user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
        First_Name=models.CharField(max_length=100)
        Last_Name=models.CharField(max_length=100)
        Email=models.EmailField(max_length=100)
        Student_Id=models.CharField(max_length=100)
        GENDER={
            ("male","Male"),
            ("female","Female"),
            ("others","Others"),
        }
        Gender=models.CharField(max_length=100,choices=GENDER)
        SECTION={
            ('1','A'),
            ('2','B'),
            ('3','C'),
            ('4','D'),
        }
        Section=models.CharField(choices=SECTION,max_length=100)
        Date_of_Birth=models.DateField()
        Religion=models.CharField(max_length=100)
        Mobile_Number=models.CharField(max_length=100)
        SESSION_OPTION={
            ('1',"Summer Session"),
            ('2',"Fall Session"),
            ('3',"Spring Session"),
        }
        Session_Year=models.CharField(choices=SESSION_OPTION,max_length=100)
        Student_Image=models.ImageField(upload_to='static/Student_Image')
        Father_Name=models.CharField(max_length=100)
        Father_Occupation=models.CharField(max_length=100)
        Father_Mobile=models.CharField(max_length=100)
        Father_Email=models.EmailField(max_length=100)
        Mother_Name=models.CharField(max_length=100)
        Mother_Occupation=models.CharField(max_length=100)
        Mother_Mobile=models.CharField(max_length=100)
        Mother_Email=models.EmailField(max_length=100)
        Present_Address=models.TextField()
        Permanent_Address=models.TextField()
        
        myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)
        
        def __str__(self):
            return self.First_Name
    ```
    - Here `myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)` is the ForeignKey relationship with department model
    - `on_delete=models.DO_NOTHING` means when department is deleted student won't be effected

[⬆️ Go to top](#day-51-28-05-2024-topics)

### Teacher Model relationship with Department model
- Create `TeacherAddModel` model
    ```python
    class TeacherAddModel(models.Model):
        user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
        teacher_id=models.CharField(max_length=100)
        name=models.CharField(max_length=100)
        GENDER={
            ("male","Male"),
            ("female","Female"),
            ("others","Others"),
        }
        gender=models.CharField(max_length=100,choices=GENDER)
        mobile=models.CharField(max_length=100)
        joining_date=models.DateField()
        QUALIFICATION={
            ("bsc","BSc. in CSE"),
            ("msc","MSc. in CSE"),
        }
        qualification=models.CharField(max_length=100,choices=QUALIFICATION)
        experience=models.CharField(max_length=100)
        myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)
        profile_image=models.ImageField(upload_to='static/teacher_img')
        present_address=models.CharField(max_length=100)
        permanent_address=models.CharField(max_length=100)
    ```
    - Here similarly we make a relationship with department model `myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)`

[⬆️ Go to top](#day-51-28-05-2024-topics)

### Student - Teacher count in Department dashboard
- In `departmentslist` function we implement the count
    ```python
    def departmentslist(request):
        department=DepartmentAddModel.objects.all()
        departmentList=[]
        for i in department:
            student_count = StudentAddModel.objects.filter(myDepartment=i).count()
            teacher_count = TeacherAddModel.objects.filter(myDepartment=i).count()
            print(student_count)
            
            departmentList.append(
                {
                    'Department_Name':i.Department_Name,
                    'Head_of_Department':i.Head_of_Department,
                    'student_count':student_count,
                    'teacher_count':teacher_count,
                    'id':i.id,
                }
            )
            
        departmentDict={
            'departmentList':departmentList,
        }
        return render(request,'department/departmentslist.html',departmentDict)
    ```
    - To count the number of student in that department we filter through each department and student model 
    - Similar thing done while counting teacher in each department
    - Note that we created a relationship earlier which helping us to do this

[⬆️ Go to top](#day-51-28-05-2024-topics)

### Task
- Teacher Add and count

</details>

<details>
<summary>Day-52-Preskool 04 Session correction,add,view,count (29-05-2024)</summary>

## Day 52 (29-05-2024) Topics:
- [Student model session correction](#student-model-session-correction)
- [Session year add,view,count](#session-year-addviewcount)

### Student model session correction 
- Create `SessionAddModel` model separately like department model
    ```python
    class SessionAddModel(models.Model):
        Session_Year=models.CharField(max_length=100)
        created_at=models.DateField(auto_now=True)
        updated_at=models.DateField(auto_now_add=True)
        
        def __str__(self):
            return self.Session_Year
    ```
- Now in student model make a relationship with session model
    ```python
    class StudentAddModel(models.Model):
        mySessionYear=models.ForeignKey(SessionAddModel,on_delete=models.DO_NOTHING)
        user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
        myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)
        Student_Id=models.CharField(max_length=100)
        GENDER={
            ("male","Male"),
            ("female","Female"),
            ("others","Others"),
        }
        Gender=models.CharField(max_length=100,choices=GENDER)
        SECTION={
            ('1','A'),
            ('2','B'),
            ('3','C'),
            ('4','D'),
        }
        Section=models.CharField(choices=SECTION,max_length=100)
        Date_of_Birth=models.DateField()
        Religion=models.CharField(max_length=100)
        Mobile_Number=models.CharField(max_length=100)
        Student_Image=models.ImageField(upload_to='static/Student_Image')
        Father_Name=models.CharField(max_length=100)
        Father_Occupation=models.CharField(max_length=100)
        Father_Mobile=models.CharField(max_length=100)
        Father_Email=models.EmailField(max_length=100)
        Mother_Name=models.CharField(max_length=100)
        Mother_Occupation=models.CharField(max_length=100)
        Mother_Mobile=models.CharField(max_length=100)
        Mother_Email=models.EmailField(max_length=100)
        Present_Address=models.TextField()
        Permanent_Address=models.TextField()
    ```
    - Here `mySessionYear=models.ForeignKey(SessionAddModel,on_delete=models.DO_NOTHING)` is used to creating the relationship

### Session year add,view,count
- Add session 
    ```python
    def sessionadd(request):
        if request.method=="POST":
            Session_Year=request.POST.get('Session_Year')
            session=SessionAddModel.objects.create(
                Session_Year=Session_Year
            )
            session.save()
            return redirect('sessionlist')
            
        return render(request,'sessions/sessionadd.html')
    ```
    - In this `sessionadd` function we add the session in our session model
- View and count the student in that session
    ```python
    def sessionlist(request):
        session=SessionAddModel.objects.all()
        session_list=[]
        
        for i in session:
            student_count=StudentAddModel.objects.filter(mySessionYear=i).count()
            
            session_list.append(
                {
                    'id':i.id,
                    'student_count':student_count,
                    'Session_Year':i.Session_Year,
                }
            )
            
        
        sessionDict={
            'session_list':session_list,
        }
        
        return render(request,'sessions/sessionlist.html',sessionDict)
    ```
    - In `sessionlist` function we count the total student in that session where we used filter and count method
    - It is possible due to relationship we created in our model
    - Finally we return the dictionary in `sessionlist.html` page to view it

</details>

<details>
<summary>Day-53-Preskool 05 Subject add,view,count (30-05-2024)</summary>

## Day 53 (30-05-2024) Topics:
- [Subject Add,View](#subject-addview)
  - Count per department how many subject
- [Relationship](#relationship)
  - One to many
  - Many to one
  - Foreign Key
  - Many to many

### Subject Add,View
- Subject model
  ```python
  class SubjectModel(models.Model):
      sub_id=models.CharField(max_length=100)
      sub_name=models.CharField(max_length=100)
      myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)
      
      def __str__(self):
          return self.sub_name
  ```
  - Here we make a `ForeignKey` relationship with department

- To add subject create `subjectsadd` function
  ```python
  def subjectsadd(request):
      department=DepartmentAddModel.objects.all()
      deptDict={
          'department':department
      }
      
      if request.method=="POST":
          sub_id=request.POST.get('sub_id')
          sub_name=request.POST.get('sub_name')
          Department_ID=request.POST.get('Department_ID')
          
          dept=DepartmentAddModel.objects.get(id=Department_ID)
          
          subject=SubjectModel.objects.create(
              sub_id=sub_id,
              sub_name=sub_name,
              myDepartment=dept,
          )
          subject.save()
          return redirect('subjectslist')
  ```
  - Here after getting data from user we used `.create` to create that subject in the model and save it
- To count and view the subject we loop through the department and count the subject in that specific department.
  ```python
  def departmentslist(request):
      department=DepartmentAddModel.objects.all()
      departmentList=[]
      for i in department:
          student_count = StudentAddModel.objects.filter(myDepartment=i).count()
          teacher_count = TeacherAddModel.objects.filter(myDepartment=i).count()
          subject_count = SubjectModel.objects.filter(myDepartment=i).count()
          print(student_count)
          
          departmentList.append(
              {
                  'Department_Name':i.Department_Name,
                  'Head_of_Department':i.Head_of_Department,
                  'student_count':student_count,
                  'teacher_count':teacher_count,
                  'subject_count':subject_count,
                  'id':i.id,
              }
          )
          
      departmentDict={
          'departmentList':departmentList,
      }
      return render(request,'department/departmentslist.html',departmentDict)
  ```
  - Here we used filter which will filter out all the match result in the loop and after counting it we append it

### Relationship
- One to many:
  - A university has many departments.
  - A zoo has many animals.
  - A company has many employees.
  - A blog post can have many comments.
  - A teacher teaches multiple students. 
  - A manufacturer produces many products.
  - A parent has many children.
  - A manager oversees many employees.
  - A country has many cities.
  - A playlist contains many songs. 

- Many to one:
  - Many employees work for one CEO.
  - Many students belong to one class.
  - Many cities are in one country.
  - Many tasks report to one project manager.
  - Many products are manufactured by one company. 
  - Many ingredients are used in one recipe.
  - Many messages are sent to one recipient.
  - Many tasks are assigned to one team leader.
  - Many transactions are processed by one bank.
  - Many purchases are made by one customer. 

- Foreign Key:
  - In a bookstore database, the 'author_id' in a 'books' table referencing the 'id' in an 'authors' table.
  - In a school database, the 'teacher_id' in a 'students' table referencing the 'id' in a 'teachers' table.
  - In a banking database, the 'account_holder_id' in a 'bank_accounts' table referencing the 'id' in a 'account_holders' table.
  - In an e-commerce database, the 'category_id' in a 'products' table referencing the 'id' in a 'categories' table.
  - In a hospital database, the 'doctor_id' in a 'patients' table referencing the 'id' in a 'doctors' table. 
  - In a social media database, the 'user_id' in a 'posts' table referencing the 'id' in a 'users' table.
  - In an inventory management system, the 'supplier_id' in a 'products' table referencing the 'id' in a 'suppliers' table.
  - In a hotel reservation system, the 'room_type_id' in a 'rooms' table referencing the 'id' in a 'room_types' table.
  - In a movie database, the 'director_id' in a 'movies' table referencing the 'id' in a 'directors' table.
  - In a music streaming service database, the 'artist_id' in a 'songs' table referencing the 'id' in an 'artists' table. 

- Many to many:
  - A student can enroll in many courses, and a course can have many students.
  - Actors can play in many movies, and movies can have many actors.
  - A user can belong to many groups, and a group can have many users.
  - A book can be categorized under multiple genres, and each genre can have multiple books.
  - A recipe can have multiple ingredients, and an ingredient can be used in multiple recipes.
  - A student can participate in many extracurricular activities, and an activity can have many students.
  - Many authors can contribute to one anthology, and an author can contribute to many anthologies.
  - A customer can order many products, and a product can be ordered by many customers.
  - Many users can be part of one chat group, and a user can be part of many chat groups.
  - A doctor can be associated with many patients, and a patient can have consultations with many doctors.

</details>

<details>
<summary>Day-54-Job Portal Project Recap 04 Each field validation (01-06-2024)</summary>

## Day 54 (01-06-2024) Topics:
- Job Portal recap 04
    - [Signup page each field validation](#signup-page-each-field-validation)

### Signup page each field validation
- Username validation pattern we used is `r'^[a-z0-9]+$'`
    - This pattern means only accepts a to z lowercase alphabet and number
    ```python
    # username validate 
    pattern = r'^[a-z0-9]+$'
    if not re.match(pattern, username):
        messages.warning(request,message_box['username_warning'])
        return redirect('signup')
    ```
- Password validation pattern we used is `r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[a-zA-Z0-9@$!%*?&#]+$'`
    - This long patterns contains many pattern inside it
        - Contains at least one lowercase letter (`a-z`).
        - Contains at least one uppercase letter (`A-Z`).
        - Contains at least one digit (`0-9`).
        - Contains at least one special character from the set `@$!%*?&#`.
        - Consists solely of characters from the combined set of lowercase, uppercase letters, digits, and specified special characters.
    - This is very hard combination of strong password checking pattern
- City name validation pattern we used is `r'^[a-zA-Z]+$'`
    - This pattern only accepts lowercase and uppercase letter for naming
    ```python
        # city name validate 
        pattern = r'^[a-zA-Z]+$'
        if not re.match(pattern, city):
            messages.warning(request,message_box['city_warning'])
            return redirect('signup')
    ```
- profile image validation we used size limit
    ```python
        # profile image validate 
        max_size_bytes = 5 * 1024 * 1024
        profile_picture.seek(0, 2)  # Move to the end of the file
        file_size = profile_picture.tell()  # Get the current position, which is the file size
        if file_size > max_size_bytes:
            messages.warning(request, message_box['picture_warning'])
            return redirect('signup')
    ```
    - It means only file which is less than 5mb will be accepted

</details>

<details>
<summary>Day-55-Summative Assessment 01 (02-06-2024)</summary>

## Day 55 (02-06-2024) Topics:
- [Summative Assessment 01](#summative-assessment-01)

### Summative Assessment 01
- **Project Name**: Job Portal Project
    - **Authentication for both Recruiters and Job Seekers**
        - **Task**: Create the registration and login functionalities for Recruiters and Job Seekers. Ensure secure password storage using hashing.
        - **Requirements**:
            - A registration form that collects username,password,Confirm Password and role(Recruiter or Job Seeker), City, Gender, Profile Picture and Email.
            - A login form that verifies the credentials and starts a session. (Username and Password)
            - Every user can logout from their portal. Without authentication they can't login.
    - **Role-Based Access Control (RBAC)**
        - **Task**: Implement role-based access control to differentiate between Recruiters and Job Seekers
        - **Requirements**:
            - Ensure Recruiter can create, read, update, and delete job postings.
            - Ensure Job Seekers can only view job postings.
    - **Create Job Posting Functionalities for Recruiters**
        - **Task**: Allow Recruiters to create job postings
        - **Requirements**:
            - A form to collect job details such as Job title, Company Description, Company Logo, Company name, Company Location, Qualifications, Deadline and Salary.
            - Store the job details in a database.
    - **View Job Postings**
        - **Task**: Implement a feature for all users (including unauthenticated visitors) to view job postings
        - **Requirements**:
            - Display a list of job postings with details like job title, description, salary, deadline and company name
            - Ensure proper routing to handle unauthenticated access.
    - **Profile Management**
        - **Task**: Allow users to update their profile information
        - **Requirements**:
            - For Recruiters, include basic information and contact details.
            - For Job Seekers, include basic information, educational qualifications and work experience must show as resume style
    - **Password Change Functionality**
        - **Task**: Implement the ability for users to change their password
        - **Requirements**:
            - Verify the old password before allowing a new password to be set.
            - Ensure that the session remains active after the password is changed.
    - **Display Posted Jobs in Recruiter Profile**
        - **Task**: Display a list of jobs posted by the Recruiter on their profile page.
        - **Requirements**:
            - Fetch and display the job postings associated with the logged-in Recruiter.
            - Ensure the Recruiter can view and manage their job posts from this page.
    - **Job Seeker Profile with Education and Work Experience**
        - **Task**: Allow Job Seekers to add and update their educational qualifications and work experience.
        - **Requirements**: 
            - Forms to add educational qualifications and work experience.
            - Display this information on the Job Seeker's profile page.
> Everything was implemented well but at the last point it was confusing to me to create separate model for seeker education and work experience which ruined the timing. Thus profile edit not implemented and final score I got 100/80

</details>

<details>
<summary>Day-56-Rest API Framework, Serializer 02 (03-06-2024)</summary>

## Day 56 (03-06-2024) Topics:
- Initial setup
- Working with model serializers
- Creating Object using Shell
- Class based view
- Update / Delete objects

### Initial setup
- Install Django & Django Rest Framework in virtual environment
    - `pip install django djangorestframework`
- Create Project & App
- `django-admin startproject myProject`
    - `cd myProject`
    - `py manage.py startapp myApp`
    - In `settings.py` add app name `myApp` and `rest_framework` in `INSTALLED_APPS`
        ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'rest_framework',
            'myApp'
        ]
        ```
- Create model in `models.py` 
    ```python
    from django.db import models

    class StudentModel(models.Model):
        name=models.CharField(max_length=100)
        dept=models.CharField(max_length=100)
        city=models.CharField(max_length=100)
        def __str__(self):
            return self.name
    ```
- Register the model in `admin.py`
    ```python
    from django.contrib import admin
    from .models import *
    # Register your models here.
    admin.site.register(StudentModel)
    ```
- Migrate the database
    - `py manage.py makemigrations`
    - `py manage.py migrate  `
- Create superuser
    - `py manage.py createsuperuser`

### Working with model serializers
- Create a file `serializers.py` in app directory
    - Go to [django-rest-framework-serialization documentation](https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers) and copy the code snippet
        ```python
        class SnippetSerializer(serializers.ModelSerializer):
            class Meta:
                model = Snippet
                fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        ```
    - In the copied code snippet `serializers` import is missing which must be imported
        - `from rest_framework import serializers`
    - Here `class SnippetSerializer` will be modified as our model which is student--> `class StudentModelSerializer` 
    - `model = Snippet` will be modified to `model = StudentModel`
    - `fields` attribute will be modified to our model one which is `fields = ['id', 'name', 'dept', 'city']`
    - After modify we will be our serializer as below
        ```python
        from rest_framework import serializers
        from .models import *

        class StudentModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = StudentModel
                fields = ['id', 'name', 'dept', 'city']
        ```

### Creating Object using Shell
- Now we will create object using shell
    - Go to terminal/cmd and start the shell
        - `py manage.py shell`
    - Import `StudentModel`
        - `from myApp.models import StudentModel`
    - Creating object
        - `obj=StudentModel()`
    - Now let's assign value in created object's model attribute
        ```shell
        obj.name="Tansen" 
        obj.dept="CSE"
        obj.city="Dhaka"
        ```
    - Finally save it
        - `obj.save()`
        > We can create object in my ways
    - Now simply enter object name and enter `obj` we can see the created object
    - To delete an object we can do `obj.delete()`
    - Also we can view it in the admin panel
    - We can view the serializers too using `repr()`
        ```shell
        from myApp.serializers import StudentModelSerializer
        s = StudentModelSerializer()
        print(repr(s))
        ```
- Now let's view the serializer in browser
    - Go to [django-rest-framework-writing-regular-django-views-using-our-serializer documentation](https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer) and copy the code snippet to `views.py` in app directory
        ```python
        from django.shortcuts import render
        from django.http import HttpResponse, JsonResponse
        from django.views.decorators.csrf import csrf_exempt
        from rest_framework.parsers import JSONParser
        from .models import StudentModel
        from .serializers import StudentModelSerializer

        @csrf_exempt
        def snippet_list(request):
            """
            List all code snippets, or create a new snippet.
            """
            if request.method == 'GET':
                snippets = Snippet.objects.all()
                serializer = SnippetSerializer(snippets, many=True)
                return JsonResponse(serializer.data, safe=False)

            elif request.method == 'POST':
                data = JSONParser().parse(request)
                serializer = SnippetSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
        ```
        - In this code snippet all we have to do is replace the model and serializer name. Here is the modified one
        ```python
        from django.shortcuts import render
        from django.http import HttpResponse, JsonResponse
        from django.views.decorators.csrf import csrf_exempt
        from rest_framework.parsers import JSONParser
        from .models import StudentModel
        from .serializers import StudentModelSerializer

        @csrf_exempt
        def StudentApiView(request):
            """
            List all code snippets, or create a new snippet.
            """
            if request.method == 'GET':
                snippets = StudentModel.objects.all()
                serializer = StudentModelSerializer(snippets, many=True)
                return JsonResponse(serializer.data, safe=False)

            elif request.method == 'POST':
                data = JSONParser().parse(request)
                serializer = StudentModelSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
        ```
    - Now create url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from myApp.views import StudentApiView

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('StudentApiView/',StudentApiView,name='StudentApiView')
        ]
        ```
        - Now we can view it in `http://127.0.0.1:8000/StudentApiView/` route
- Class based view
    - Go to [django-rest-framework-class-based-view documentation](https://www.django-rest-framework.org/tutorial/3-class-based-views/#tutorial-3-class-based-views) and copy the code snippet to `views.py` in app directory
        ```python
        from snippets.models import Snippet
        from snippets.serializers import SnippetSerializer
        from django.http import Http404
        from rest_framework.views import APIView
        from rest_framework.response import Response
        from rest_framework import status

        class SnippetList(APIView):
            """
            List all snippets, or create a new snippet.
            """
            def get(self, request, format=None):
                snippets = Snippet.objects.all()
                serializer = SnippetSerializer(snippets, many=True)
                return Response(serializer.data)

            def post(self, request, format=None):
                serializer = SnippetSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```
        - Similarly in this code snippet all we have to do is replace the model and serializer name. Here is the modified one
        ```python
        from .models import StudentModel
        from .serializers import StudentModelSerializer
        from django.http import Http404
        from rest_framework.views import APIView
        from rest_framework.response import Response
        from rest_framework import status


        class StudentApiView2(APIView):
            """
            List all snippets, or create a new snippet.
            """
            def get(self, request, format=None):
                snippets = StudentModel.objects.all()
                serializer = StudentModelSerializer(snippets, many=True)
                return Response(serializer.data)

            def post(self, request, format=None):
                serializer = StudentModelSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```
    - Now add url in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from myApp.views import StudentApiView,StudentApiView2

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('StudentApiView/',StudentApiView,name='StudentApiView'),
            path('StudentApiView2/',StudentApiView2.as_view(),name='StudentApiView2'),
        ]
        ```
    - Now we can view it in `http://127.0.0.1:8000/StudentApiView2/` route

- Update, Delete 
    - Go to [django-rest-framework-class-based-view-update-delete documentation](https://www.django-rest-framework.org/tutorial/3-class-based-views/#rewriting-our-api-using-class-based-views) and copy the code snippet to `views.py` in app directory
        ```python
        class SnippetDetail(APIView):
            """
            Retrieve, update or delete a snippet instance.
            """
            def get_object(self, pk):
                try:
                    return Snippet.objects.get(pk=pk)
                except Snippet.DoesNotExist:
                    raise Http404

            def get(self, request, pk, format=None):
                snippet = self.get_object(pk)
                serializer = SnippetSerializer(snippet)
                return Response(serializer.data)

            def put(self, request, pk, format=None):
                snippet = self.get_object(pk)
                serializer = SnippetSerializer(snippet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def delete(self, request, pk, format=None):
                snippet = self.get_object(pk)
                snippet.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        ```
        - Also in this code snippet all we have to do is replace the model and serializer name. Here is the modified one
        ```python
        class StudentUpdateDelete(APIView):
            """
            Retrieve, update or delete a snippet instance.
            """
            def get_object(self, pk):
                try:
                    return StudentModel.objects.get(pk=pk)
                except StudentModel.DoesNotExist:
                    raise Http404

            def get(self, request, pk, format=None):
                snippet = self.get_object(pk)
                serializer = StudentModelSerializer(snippet)
                return Response(serializer.data)

            def put(self, request, pk, format=None):
                snippet = self.get_object(pk)
                serializer = StudentModelSerializer(snippet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def delete(self, request, pk, format=None):
                snippet = self.get_object(pk)
                snippet.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        ```
        - Now add url in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from myApp.views import StudentApiView,StudentApiView2,StudentUpdateDelete

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('StudentApiView/',StudentApiView,name='StudentApiView'),
            path('StudentApiView2/',StudentApiView2.as_view(),name='StudentApiView2'),
            path('StudentUpdateDelete/<int:pk>',StudentUpdateDelete.as_view(),name='StudentUpdateDelete'),
        ]
        ```
        - Here we can see `StudentUpdateDelete/<int:pk>` has `pk` which is primary key, as we are updating/deleting we need specific `id` to do that
        - Now we can update/delete in `http://127.0.0.1:8000/StudentUpdateDelete/1` route
            > Here pk which is id is important and it need to be valid

</details>

<details>
<summary>Day-57-Rest API Framework, Serializer 03 (04-06-2024)</summary>

## Day 57 Topics:
- API endpoint
  - Using shell
  - function based
  - Class based
  - Mixins
- Mixins
- API Authentication
    - Authentication
        - Token
        - Cookies
        - Email,SMS verification
        - OTP
        - Session
### API endpoint
- Using shell
- function based
- Class based
    > Covered in previous day

### Mixins
- Documentation: https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
- Generic view: https://www.django-rest-framework.org/api-guide/generic-views/
    > Django’s generic views... were developed as a shortcut for common usage patterns

- To use mixins , Go to : [django-rest-framework-mixins documentation](https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins) and copy the code snippet
    ```python
    from snippets.models import Snippet
    from snippets.serializers import SnippetSerializer
    from rest_framework import mixins
    from rest_framework import generics

    class SnippetList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
    ```
    - Modify the model and serializer name, Here is the modified code:
    ```python
    from .models import StudentModel
    from .serializers import StudentModelSerializer
    from rest_framework import mixins
    from rest_framework import generics

    class StudentList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
        queryset = StudentModel.objects.all()
        serializer_class = StudentModelSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
    ```
    - Now add the url in `urls.py`
    ```python
    from django.contrib import admin
    from django.urls import path
    from myApp.views import StudentList,StudentDetail

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('studentlist/',StudentList.as_view(),name='StudentList'),
    ]
    ```
- Update / Delete using mixins
  - Go to [django-rest-framework-mixins documentation](https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins) and copy the code snippet
    ```python
    class SnippetDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
    ```
    - Modify the model and serializer name, Here is the modified code:
    ```python
    class StudentDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
        queryset = StudentModel.objects.all()
        serializer_class = StudentModelSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
    ```
    - Add url in `urls.py`
    ```python
    from django.contrib import admin
    from django.urls import path
    from myApp.views import StudentList,StudentDetail

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('studentlist/',StudentList.as_view(),name='StudentList'),
        path('StudentDetail/<int:pk>',StudentDetail.as_view(),name='StudentDetail'),
    ]
    ```
### API Authentication:
- API Authentication documentation: [API Authentication](https://www.django-rest-framework.org/api-guide/authentication/) 
- Go to [django-rest-framework-setting-the-authentication documentation](https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme) and copy the code snippet
    ```python
    from rest_framework.authentication import SessionAuthentication, BasicAuthentication
    from rest_framework.permissions import IsAuthenticated
    from rest_framework.response import Response
    from rest_framework.views import APIView

    class ExampleView(APIView):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]

        def get(self, request, format=None):
            content = {
                'user': str(request.user),  # `django.contrib.auth.User` instance.
                'auth': str(request.auth),  # None
            }
            return Response(content)
    ```
    - From this snippet we will copy the import of `SessionAuthentication`, `BasicAuthentication` and `IsAuthenticated`
    - And add the below code in our own view class
        ```python
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]
        ```
    - Final modified code will be
        ```python
        from django.shortcuts import render
        from rest_framework.authentication import SessionAuthentication, BasicAuthentication
        from rest_framework.permissions import IsAuthenticated

        # Create your views here.
        from .models import StudentModel
        from .serializers import StudentModelSerializer
        from rest_framework import mixins
        from rest_framework import generics

        class StudentList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
            queryset = StudentModel.objects.all()
            serializer_class = StudentModelSerializer
            authentication_classes = [SessionAuthentication, BasicAuthentication]
            permission_classes = [IsAuthenticated]

            def get(self, request, *args, **kwargs):
                return self.list(request, *args, **kwargs)

            def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)
        ```
- Authentication Token
    - Add `rest_framework.authtoken` in `settings.py`
        ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'rest_framework',
            'rest_framework.authtoken',
            'myApp',
        ]
        ```
    - Now migrate it `py manage.py migrate`
    - Now go to : [django-rest-framework-token-authentication documentation](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
    - Import `from rest_framework.authentication import TokenAuthentication`
    - Add `authentication_classes = [TokenAuthentication]` and `permission_classes = [IsAuthenticated]` inside class; Here is the modified class
        ```python
        from django.shortcuts import render
        from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication 
        from rest_framework.permissions import IsAuthenticated

        # Create your views here.
        from .models import StudentModel
        from .serializers import StudentModelSerializer
        from rest_framework import mixins
        from rest_framework import generics

        class StudentList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
            queryset = StudentModel.objects.all()
            # serializer_class = StudentModelSerializer
            # authentication_classes = [SessionAuthentication, BasicAuthentication]
            authentication_classes = [TokenAuthentication]
            permission_classes = [IsAuthenticated]

            def get(self, request, *args, **kwargs):
                return self.list(request, *args, **kwargs)

            def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)
        ```
    - Now we can assign an user under token in admin page
    - To test it we can use [Postman](https://www.postman.com/) or [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)
    - Add `Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b` in Thunder Client header and then send the request

</details>

<details>
<summary>Day-58-Job Portal Project Apply Job (05-06-2024)</summary>

## Day 58 (05-06-2024) Topics:
- Job portal project recap
  - [Apply job](#apply-job)

### Apply job
- First create `ApplyJobModel` model
  ```python
  class ApplyJobModel(models.Model):
      applicant=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,related_name='applicantinfo')
      applied_job=models.ForeignKey(JobModel,on_delete=models.CASCADE)
      skills=models.CharField(max_length=100)
      resume = models.FileField(upload_to='media/seeker_resume')
      seeker_profile_pic = models.ImageField(upload_to='media/seeker_profile_pic')
      qualifications = models.TextField()
      def __str__(self):
          return self.applicant.username
  ```
  - Here we can see two model relationship.
  - `applicant` for tracking who is applying
  - `applied_job` to get the job which he apply
- Now in `views.py` create `applyjob` function
  ```python
  @login_required
  def applyjob(request,jobid):
      job=get_object_or_404(JobModel,id=jobid)
      jobDict={
          'job':job
      }
      
      already_applied=ApplyJobModel.objects.filter(applicant=request.user,applied_job=job).exists()
      if already_applied:
          messages.warning(request,"Already applied")
          return redirect('viewjob')
      
      if request.method=="POST":
          skills=request.POST.get('skills')
          resume=request.FILES.get('resume')
          seeker_profile_pic=request.FILES.get('seeker_profile_pic')
          qualifications=request.POST.get('qualifications')
          
          job_apply=ApplyJobModel.objects.create(
              skills=skills,
              resume=resume,
              seeker_profile_pic=seeker_profile_pic,
              qualifications=qualifications,
              applicant=request.user,
              applied_job=job,
          )
          job_apply.save()
          return redirect('viewjob')
      jobDict['already_applied'] = already_applied
      return render(request,'seeker/applyjob.html',jobDict)
  ```
  - Here if user already applied to a job it will show `Already applied` message
  - `jobDict['already_applied'] = already_applied` is not working as expected so will find another way to do that
  - The main target is when a job is already applied it will show the button already applied but we are returning the value in `applyjob.html` but we have to return that to `viewjob.html` page then it will work
### Task
- Recruiter page upadte
  - List of Applied applicant
  - Approved and send message button to that applicant

</details>

<details>
<summary>Day-59-Job Portal Project Posted job,Applicant list, Applied job (06-06-2024)</summary>

## Day 59 (06-06-2024) Topics:
- Job portal project
  - Recruiter profile
    - [Posted job (specific job posted by recruiter)](#posted-job-specific-job-posted-by-recruiter)
    - [Applicant list](#applicant-list)
  - Seeker Profile
    - [Applied job](#applied-job)

### Posted job (specific job posted by recruiter)
- Create a function `specificjobpost` in `views.py`
    ```python
    @login_required
    def specificjobpost(request):
        current_user=request.user
        
        if current_user.user_type == "recruiter":
            jobs = JobModel.objects.filter(created_by=current_user)
            
            jobDict={
                'jobs':jobs
            }
        return render(request,'profile/specificjobpost.html',jobDict)
    ```
    - Here we filter out the job posted by the recruiter

### Applicant list
- Create `applicants` function in `views.py`
    ```python
    def applicants(request,jobid):
        job=JobModel.objects.get(id=jobid)

        applicants=ApplyJobModel.objects.filter(applied_job=job)
            
        jobDict={
            'applicants':applicants,
            'job':job,
        }
        return render(request,'recruiter/applicants.html',jobDict)
    ```
    - Here we filter out the applicant from the `ApplyJobModel` model

### Applied job
- Applied job list can be found in two ways
    ```python
    def appliedjob(request):
        jobs=JobModel.objects.all()
        all_applied_job=[]
        for job in jobs:
            appliedjob=ApplyJobModel.objects.filter(applied_job=job)
        
            if appliedjob:
                all_applied_job.append(job)
        jobDict={
             'all_applied_job':all_applied_job
         }
        return render(request,'seeker/appliedjob.html',jobDict)
    ```
    - Here we get it using the `applied_job` in `ApplyJobModel` model
    ```python
    def appliedjob(request):
    current_user=request.user
    appliedjob = ApplyJobModel.objects.filter(applicant=current_user)
    jobDict={
        'appliedjob':appliedjob
    }
    return render(request,'seeker/appliedjob.html',jobDict)
    ```
    - Here we get it using `applicant` in `ApplyJobModel` model

</details>

<details>
<summary>Day-60-Job Portal Project search option, Calorie Counter Exam, Idea on Django Form (08-06-2024)</summary>

## Day 60 Topics:
- Job Portal Project
  - When to use GET,POST
  - Search option
    - Using multi field search by `Q`
    - Using only one field filter search
- Calorie Counter Project (Sudden Exam)
- Idea on Django form

### When to use GET,POST
- `POST`: When it is used must use csrf-token, while getting the value must use if condition to get value in views
- `GET`: It will show in the url. No need to use csrf or if condition to get the value in views
- In search option we will use `GET`

### Search option
- Get a search bar from [external source](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_searchbar3) and replace the old navbar with this one. Search will work on `viewjob.html` page
- Now let's setup it
    - After adding search option in navbar we need to show the search result
    - As it will work on `viewjob` page and the result of search is just filtered version of that page
    - So we will create a `searchpage.html` and copy the content of `viewjob.html` page

  - Using only one field filter search
    - In the `searchpage` function in `views.py` we will filtered the search query and return the result in dictionary
      ```python
      def searchpage(request):

          # search option 
          search=request.GET.get('search')
          jobs = JobModel.objects.filter(job_title=search)

          # change apply button for seeker when already applied 
          job_filtered=[]
          for i in jobs:
              already_applied=ApplyJobModel.objects.filter(applicant=request.user,applied_job=i)
              job_filtered.append(
                  (i,already_applied),
              )
          jobDict={
              'job_filtered':job_filtered
          }
          return render(request,'common/searchpage.html',jobDict)
      ```
- Using multi field search by `Q`
    - In the `searchpage` function in `views.py` we will filtered the search query using `Q` and return the result in dictionary
        ```python
        def searchpage(request):
            
            # search option 
            search=request.GET.get('search')

            jobs = JobModel.objects.filter(
                Q(job_title__icontains=search)|
                Q(deadline__icontains=search)|
                Q(created_by__username__icontains=search)
                )
            # change apply button for seeker when already applied 
            job_filtered=[]
            for i in jobs:
                already_applied=ApplyJobModel.objects.filter(applicant=request.user,applied_job=i)
                job_filtered.append(
                    (i,already_applied),
                )
            jobDict={
                'job_filtered':job_filtered
            }
            return render(request,'common/searchpage.html',jobDict)
        ```
        - Here we use `Q` which is imported by `from django.db.models import Q`

### Calorie Counter Project (Sudden Exam)
- In this project BMR was calculated
- A dashboard to show the result

### Idea on Django form
- Initial idea was given on django form
- Tomorrow this topic will be covered briefly

</details>

<details>
<summary>Day-61-TodoList Project using Django Form, Admin page modify, Meta class in model (09-06-2024)</summary>

## Day 61 Topics:
- Meta class in model
- Admin page modify
- Django Form
- Task
- Solution

### Meta class in model
- Using meta class we can modify the model
    ```python
    class CustomUserModel(AbstractUser):
        city=models.CharField(max_length=100,null=True)
        profile_pic=models.ImageField(upload_to='media/profile_pic',null=True)
        USER_TYPE={
            ('user','User'),
            ('admin','Admin'),
        }
        user_type=models.CharField(choices=USER_TYPE,max_length=100,null=True)
        
        class Meta:
            ordering=['username']
            verbose_name = 'Custom User Model'
            db_table='my_todo_list_table'
            unique_together = ["email", "username"]
            verbose_name_plural = "Custom User Models"
        
        def __str__(self):
            return self.username
    ```
    - Here we modified the model using `Meta` which refers to `metadata`
    - More modification option can be found in [Official Django Documentation in Model Meta options](https://docs.djangoproject.com/en/5.0/ref/models/options/)

### Admin page modify
- In `admin.py` we can modify the view of a model table i admin page
    ```python
    class CustomUserModelDisplay(admin.ModelAdmin):
        list_display=['username','email','user_type','city']
        search_fields=['username','email','user_type','city']
        
        fieldsets=[
            (
                "This is my title",
                {
                'fields':['username','email','password']
                }
            ),
            (
                "Advanced options",
                {
                    'classes':['collapse'],
                    'fields':['first_name','last_name','city','profile_pic','user_type']
                }
            )
        ]

    admin.site.register(CustomUserModel,CustomUserModelDisplay)
    ```
    - Here `list_display` is used to show the main table with those fields
    - `search_fields` is used to search through those fields
    - `fieldsets` modified the view of a single table data. Inside that only those will be shown
    - More modification option can be found in [Official Django Documentation in The Django admin site](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#discovery-of-admin-files)

### Django Form
- Create a `forms.py` file inside project directory
- Utilize Django's built-in `UserCreationForm` and `AuthenticationForm` to create custom forms.
- Define the required fields inside the `Meta` class for each form.
    ```python
    from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
    from django import forms
    from todoApp.models import *

    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model=CustomUserModel
            fields=UserCreationForm.Meta.fields+('city','profile_pic','user_type','email','first_name','last_name')
            
    class CustomUserAuthenticationForm(AuthenticationForm):
        class Meta:
            model=CustomUserModel
            fields=['username','password']
    ```
    - Here two custom form created
    - First one is for signup `CustomUserCreationForm` which is created using `UserCreationForm`
    - Second one is for signin `CustomUserAuthenticationForm` which is created using `AuthenticationForm`
- Now in `views.py`
    ```python
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
    ```
    - Here in signup function we used `CustomUserCreationForm` where `request.POST`,`request.FILES`; It is important to write `request.FILES` otherwise images/files won't be received
    - Then we check if form is valid or not
    - In the else part we return the empty form `CustomUserCreationForm()` where user will fillup
- Add the url in `urls.py`
- Now the `signup.html`
    ```python
    <div>
    <form action="{% url 'signup' %}" method="POST" enctype="multipart/form-data">

        {% csrf_token %}

        {{form}}
        <input type="submit" value="Submit">
    </form>
    </div>
    ```
    - Here we write the `{{form}}` which is returned by the `signup` function in `view.py`
    - If any field missing here then we can add that in `forms.py` Meta class
        ```python
        class CustomUserCreationForm(UserCreationForm):
            class Meta:
                model=CustomUserModel
                fields=UserCreationForm.Meta.fields+('city','profile_pic','user_type','email','first_name','last_name')
        ```
        - Make sure those fields present in model, otherwise won't work
- Similarly we created the `signin.html` form, where `views.py` function is `signin`
    ```python
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
    ```
    - Here everything is similar except `CustomUserAuthenticationForm(request,data=request.POST)`; Where `data=request.POST` is used to get the data and then check if it is valid or not
    - If it is valid then we get the user data from `form.get_user()` and login using `login(request,user)`

### Task
- Create Signup / Signin normal form
- Signup / Signin with Django form

### Solution
- [Signup / Signin normal form](#signup--signin-normal-form)
- [Signup / Signin with Django form](#signup--signin-with-django-form)
- [Fields in signup form](#fields-in-signup-form)
- [Fields in signin form](#fields-in-signin-form)

### Signup / Signin normal form
- Get a form template from [external source](https://www.w3schools.com/css/css_form.asp)
- Modify it according to required fields
- Get the form data and add those data in the model

### Signup / Signin with Django form
- Create a `forms.py` file inside project directory
- Utilize Django's built-in `UserCreationForm` and `AuthenticationForm` to create custom forms.
- Define the required fields inside the `Meta` class for each form.

> After successful signin it will redirect to dashboard

> Also include logout, success/warning messages functionalities

### Fields in signup form
- First Name
- Last Name
- Username
- Email
- Password
- Confirm Password
- City
- Profile Picture
- User Type
    - User
    - Admin

### Fields in signin form
- Username
- Password

</details>

<details>
<summary>Day-62-TodoList Project Django Form CRUD Operations (10-06-2024)</summary>

## Day 62 (10-09-2024) Topics:

- [Model form](#model-form)
    - [Category form](#category-form)
    - [Task form with Widgets & Labels](#task-form-with-widgets--labels)
- [CRUD Operation using django form](#crud-operation-using-django-form)

### Model form
- Previously `forms.py` file we used `UserCreationForm` & `AuthenticationForm`
- Now to use Model Form we have to import forms by `from django import forms`

### Category form
- And create the required form for example category form
    ```python
    class CustomCategoryForm(forms.ModelForm):
        class Meta:
            model=CategoryModel
            fields=['category_name']
    ```
    - Here only one field `category_name` this will be shown in html form page

### Task form with Widgets & Labels
- Now in task form we will use widgets to modify the css & labels to modify the field name in html page
    ```python
    class CustomTaskForm(forms.ModelForm):
        class Meta:
            model=TaskModel
            fields=['task_name','task_description','task_status','task_priority','due_date','completed_date']
            
            widgets={
                'due_date':forms.DateInput(attrs={'type':'date', 'class':'date-field'}),
                'completed_date':forms.DateInput(attrs={'type':'date','class':'date-field'}),
                'task_description':forms.Textarea(attrs={'type':'text','class':'textarea-field'})
            }
            
            labels={
                "task_description":"Enter description",
        }
    ```
    - Here `widgets` & `labels` used to modify the field

### CRUD Operation using django form
- Create operation
    ```python
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
    ```
- Read Operation
    ```python
    @login_required
    def categorylist(request):
        cat=CategoryModel.objects.all()
        return render(request,'user/categorylist.html',{'cat':cat})
    ```
- Update Operation
    ```python
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
    ```
- Delete Operation
    ```python
    @login_required
    def categorydel(request,catid):
        cat=get_object_or_404(CategoryModel,id=catid)
        cat.delete()
        return redirect('categorylist')
    ```

</details>

<details>
<summary>Day-63-Django Form Exam on Job Portal Project (11-06-2024)</summary>

## Day 63 (11-06-2024) Topics:

- [Lab Exam on Job Portal Project using Django Form](#lab-exam)
- [Notes](#notes)
### Lab Exam
> Question: Develop a job portal using Django. In this project, you have to incorporate multiple recruiters and multiple job seekers from different domains on one platform. A single recruiter can post multiple job openings using his/her account. A single job seeker is able to manage their account using a profile manager. 

Job Specification Information:
- Create a project named Name_ID_JobPortal
- Develop a registration page using the following fields
    - Username
    - Display name
    - Email
    - Password
    - Confirm Password
    - User type
- Develop a login page using the following fields
    - Username
    - Password
- Develop a profile creation page based on user type
    - Recruiters
        - Company information
    - Job Seekers 
        - Skills set
        - Resume upload option
- Develop a job posting page for recruiters
    - Title
    - Number of openings
    - Category
    - Job description
    - Skills
- Develop a job applying page for Job Seeker
    - Search
- Develop a skill matching page for both recruiters and job seeker 
    - Dashboard for skill matched job
- Requirements:
    - Create a Django Project
        - Naming Convention: Name_ID_Project
    - Create a Database
    - Store the Database

### Notes
- Previously when using normal form and the `SeekerModel` or `RecruiterModel` has relationship with `CustomUserModel` we used this approach to assign the created custom user
    ```python
    def signup(request):
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            user_type=request.POST.get('user_type')
            city=request.POST.get('city')
            gender=request.POST.get('gender')
            profile_picture=request.FILES.get('profile_picture')
            email=request.POST.get('email')

            if password==confirm_password:
                user = CustomUserModel.objects.create_user(
                    username=username,
                    password=password,
                    user_type=user_type,
                    city=city,
                    gender=gender,
                    profile_picture=profile_picture,
                    email=email,
                )
                user.save()
                if user_type=="recruiter":
                    user_tp=RecruiterModel.objects.create(recruiter_user=user)
                if user_type=="seeker":
                    user_tp=SeekerModel.objects.create(seeker_user=user)
                user_tp.save()
                messages.success(request,message_box['signup_success'])
                return redirect('signin')
            else:
                messages.success(request,message_box['password_warning'])
                return redirect('signup')
        return render(request,'common/signup.html')
    ```
    - In this code snippet we first save data in `CustomUserModel` then assign that in other model according to their type

- Now in Django Form, there are few modification
    ```python
    def signup(request):
        if request.method=='POST':
            form=CustomUserForm(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                user.save()
                print(user.user_type)
                if user.user_type == 'recruiter':
                    user = RecruiterModel.objects.create(
                        user=user
                    )
                else:
                    user = SeekerModel.objects.create(
                        user=user
                    )
                return redirect('signin')
        else:
            form=CustomUserForm()
        return render(request,'common/signup.html',{'form':form})
    ```
    - Here we did the same first save the user where we get it before commit `user=form.save(commit=False)` then check `user_type` this checking can be done in another way like `form.cleaned_data['user_type']` 
    - `commit=False` allows us to manipulate the data before actually saving it to the database. It's useful when we need to perform some additional logic or set additional attributes on the model instance before saving it.
    - After checking `user_type` we assign the user according to their type in the model

</details>

<details>
<summary>Day-64-TodoList Project Using Django Form & Normal bootstrap form (12-06-2024)</summary>

## Day 64 (12-06-2024) Topics:
- [Complete TodoList Project](#complete-todolist-project)
- [Recreate TodoList Project using Bootstrap](#recreate-todolist-project-using-bootstrap)

### Complete TodoList Project
- Functionalities
    - There are two types of user
        - User
        - Admin
- User
    - User can create / update task
    - Can create categories
    - Can mark task as completed / in-completed
    - A dashboard to see progress
- Admin
    - Admin can see and delete the user

### Recreate TodoList Project using Bootstrap
- Bootstrap version 5 is used
- It will be done using normal form 
- It is still in progress
- Only Sign-up/in completed

</details>

<details>
<summary>Day-65-Final Exam Suggestion (13-06-2024)</summary>

## Day 65 (13-06-2024) Topics:
- [Final Exam QnA Suggestion](#final-exam-qna-suggestion)
- [Extra](#extra)

### Final Exam QnA Suggestion
- How to activate/deactivate python environment
- How to create superuser
- What Django app structure contains
- By default what app contains
- What admin.py used for
- Task of each files in project/app; e.g:
    - Task of `models.py`
    - Task of `views.py`
- How to setup static files
- How `forms.py` worked
- Where app installed
- What Middleware used for
- What template used for in settings.py
- Where database can be changed
- How to change timezone
- How custom user permission granted
- What `LOGIN_URL` used for
- What is Django by default database
- Why used `manage.py`
- Which types of queries do we commonly use in Django? (all, filter, get, count, __icontains, __gt, distinct) 
- Why used values in distinct (unique)
- Explain why __ is imported
- from where messages imported
- Why used `login_required`
- How many way you can create object in database
    - Create
    - Create user (only used in signup)
    - After getting object with `id` then using dot
    - Directly assign 
- Why used request.POST (form will work)
- Why used request.GET (form won't work, mainly used in search)
- Why used update_session_auth_hash
- How user password checked
- Why `Q` is used
- How data sent in template
- When `request.FILES` used
- Why authenticate used in signin (django used both auth and validation in authenticate)
- When used `render`,`redirect`
- Usage of `set_password`,`set_username`
- Usage of Django built in user
- Usage of `is_active`=True/False (used in email verification)
- Usage of `is_authenticated`
- Usage of `get_user`
- usage of `check_password`,`set_password`,`update session`
- How many parameter in `get_objects_or_404`
- What is `exists()` used for and what the field will became after using it
- Why `__icontains` used in search
- How many relationship used in job apply and why
- Usage of many to many
- Looping in many to many : `for subject in student.subject.all` 
- What is `class Meta` in `models.py`,`forms.py`
- How can you reduce code repetition in Django templates?
- Usage of `is_deleted` (it is default True)
- Importance of virtual environment setup for Django.
- Learn about django signal

### Extra
- Mandatory in custom user (`username`,`password`)
- Remember to use method correctly (`.save()`, `.delete()`)
- Use `print()` to find out bug/error
- Regular expression practice: [regex101](https://regex101.com/)
- Regular expression in url re_path: [Official docs](https://docs.djangoproject.com/en/5.0/topics/http/urls/#using-regular-expressions)
- Go through Model [instances documentation](https://docs.djangoproject.com/en/5.0/ref/models/instances/)
- Usage of [is_stuff](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/)
- Read through [Django Auth Documentation](https://docs.djangoproject.com/en/5.0/topics/auth/default/) more:  [here](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/)
- Search and read through: [Google search](https://www.google.com/search?q=interview+question+django) -  [Another Search](https://www.google.com/search?q=Django+100+interview+questions)
    - [turing](https://www.turing.com/interview-questions/django) 
    - [geeksforgeeks](https://www.geeksforgeeks.org/django-interview-questions/)
    - [interviewbit](https://www.interviewbit.com/django-interview-questions/)
    - [simplilearn](https://www.simplilearn.com/django-interview-questions-article)
    - [anywhere](https://anywhere.epam.com/en/blog/django-interview-questions) 
    - [edureka](https://www.edureka.co/blog/interview-questions/django-interview-questions/)
    - [tealhq](https://www.tealhq.com/interview-questions/python-django-developer)

</details>

<details>
<summary>Day-66-Final Project Assigned(22-06-2024)</summary>

## Day 66 (22-06-2024) Topics:
- [New 6 team created by sir for final project](#new-6-team-created-by-sir-for-final-project)
- [Projects lottery between 6 team](#projects-lottery-between-6-team)
- [Lottery result](#lottery-result)
- [All important days announced](#all-important-days-announced)
- [Django Project Ideas](#django-project-ideas)
- [Website templates](#website-templates)

### New 6 team created by sir for final project
- My team members:
    - Md. Alahi Almin Tansen (`DIPTI-ICT-WADP-L4-03-05`)
    - Tumpa Moni Mim (`DIPTI-ICT-WADP-L4-03-02`)
    - Dolonchapa Khan Urmi (`DIPTI-ICT-WADP-L4-03-14`)
    - Farhun Arif Hassan Chowdhury (`DIPTI-ICT-WADP-L4-03-04`)

- Md. Shakil team members:
    - Md. Shakil (`DIPTI-ICT-WADP-L4-03-17`)
    - Jessica Tithi Chakrabarty (`DIPTI-ICT-WADP-L4-03-19`)
    - Md. Fuad Hossain (`DIPTI-ICT-WADP-L4-03-20`)
    - Sheikh Tarek Mahmud (`DIPTI-ICT-WADP-L4-03-22`)

- Shamim Hossen team members:
    - Shamim Hossen (`DIPTI-ICT-WADP-L4-03-06`)
    - Md. Sajjad Hossain (`DIPTI-ICT-WADP-L4-03-03`)
    - Monira Akther (`DIPTI-ICT-WADP-L4-03-01`)
    - Moniruzzaman (`DIPTI-ICT-WADP-L4-03-15`)

- Md. Rejone Hossain team members:
    - Md. Rejone Hossain (`DIPTI-ICT-WADP-L4-03-09`)
    - Protikha Hira Tanwi (`DIPTI-ICT-WADP-L4-03-13`)
    - Sharmin Akter (`DIPTI-ICT-WADP-L4-03-18`)
    - Nazmul Hossain (`DIPTI-ICT-WADP-L4-03-07`)

- Sagor Mia team members:
    - Sagor Mia (`DIPTI-ICT-WADP-L4-03-11`)
    - Dipu Ray (`DIPTI-ICT-WADP-L4-03-12`)
    - Ranajit Chandra Das (`DIPTI-ICT-WADP-L4-03-10`)
    - Dheeman Chakma (`DIPTI-ICT-WADP-L4-03-24`)

- Md. Abdullah Al Mamun team members:
    - Md. Abdullah Al Mamun (`DIPTI-ICT-WADP-L4-03-16`)
    - Md. Naim Islam (`DIPTI-ICT-WADP-L4-03-21`)
    - M.A Hannan (`DIPTI-ICT-WADP-L4-03-08`)
    - Afsana Akter Mimi (`DIPTI-ICT-WADP-L4-03-23`)

### Projects lottery between 6 team
- News Portal + Blog combined
- Job portal + Resume Builder + Quiz System combined
- Hospital Management system
- School Management system
- Food recipe
- Fitness Tracker + Calorie Counter combined
- To-let + Blog combined
- TodoList + Blog + News Portal combined

### Lottery result
- My team get `To-let + Blog combined`
- Md. Shakil team get `School Management system` 
- Shamim Hossen team get `Job portal + Resume Builder + Quiz System combined`
- Md. Rejone Hossain team get `Hospital Management system`
- Sagor Mia team get `Fitness Tracker + Calorie Counter combined`
- Md. Abdullah Al Mamun team get `News Portal + Blog combined`

### All important days announced
- Presentation date:
  - 24-06-2024 (Monday)
- Project update date:
  - 26-06-2024 (Wednesday)

- Project update 2 date:
  - 29-06-2024

- Project submission date:
  - 30-06-2024 (Sunday)

### Django Project Ideas
- [Django project ideas for beginners](https://www.placementpreparation.io/blog/django-project-ideas-for-beginners/)

### Website templates
- [Uicookies](https://uicookies.com/free-real-estate-website-templates/)
- [Bootstrapmade](https://bootstrapmade.com/)
- [Startbootstrap](https://startbootstrap.com/themes)
- [Themefisher](https://themefisher.com/free-bootstrap-templates)
- [Creative tim](https://www.creative-tim.com/bootstrap-themes/free)
- [Mobirise](https://mobirise.com/bootstrap-template/)
- [Colorlib](https://colorlib.com/wp/cat/bootstrap/)
- [Bootswatch](https://bootswatch.com/)

</details>

<details>
<summary>Day-67-Written, MCQ Exam & Project update(23-06-2024)</summary>

## Day 67 (23-06-2024) Topics:
- Written and MCQ exam held, I got (written 11 and MCQ 14) total 25 out of 30.
- To-let project
  - Project update taken
  - I show the update using github project board table

</details>

<details>
<summary>Day-68-Project Pre-presentation & To-let Project Initial Template Mastering (24-06-2024)</summary>

## Day 68 (24-06-2024) Topics:
- To-let project
  - Presentation on project,  my team scored 24/30
  - Work on assigned project template mastering

</details>

<details>
<summary>Day-69-To-let Project Admin Dashboard Template Mastering (25-06-2024)</summary>

## Day 69 (25-06-2024) Topics:
- To-let project
  - Admin dashboard full template mastering

</details>

<details>
<summary>Day-70-To-let Project Add Property Multiple Image Integration (26-06-2024)</summary>

## Day 70 (26-06-2024) Topics:
- To-let project
  - Add property correction
    - Add property JavaScript integration
    - Multiple image selection and view

</details>

<details>
<summary>Day-71-Written, Oral Test Suggestion & Mock Oral Exam (27-06-2024)</summary>

## Day 71 (27-06-2024) Topics:
- Written and oral test suggestion
- Oral test where I scored 9/10. Mistake on django form example

</details>

<details>
<summary>Day-72-To-let issues, Index page,Image,Favourite,Property Views & Schedule, Review Added (29-06-2024)</summary>

## Day 72 (29-06-2024) Topics:
- To-let project
    - Solve many issue in to let project
    - Index page summary data view
    - Image/favourite/Property page view logic
    - Schedule / Review Added

</details>

<details>
<summary>Day-73-To-let Admin Dashboard, Issue Solved in Favourite / User review (30-06-2024)</summary>

## Day 73 (30-06-2024) Topics:
- To-let project
    - Worked on admin dashboard of to let project
    - New task (add notification)
    - Solved favourite / User review

</details>

<details>
<summary>Day-74-To-let Notification,Blog Added,Revamped Property List Page (01-07-2024)</summary>

## Day 74 (01-07-2024) Topics:
- To-let project
    - Notification Added
    - Blog added
    - Revamped property listing with agent image

</details>

<details>
<summary>Day-75-To-let Edit/Delete,Password Change Added, New Logo,Customized Template,Final Exam Date revealed (02-07-2024)</summary>

## Day 75 (02-07-2024) Topics:
- To-let project
    - Edit/delete added in blog,property,favourite
    - Customizing template a bit with new logo
    - Fixed mobile routes
    - Reworked on Editing multiple images
    - Password change added
- Final Exam date revealed (8th July,2024)

</details>

<details>
<summary>Day-76-To-let Final Project Submission(03-07-2024)</summary>

## Day 76 (03-07-2024) Topics:
- To-let project
    - Final Project Submission day

</details>

<details>
<summary>Day-77-Last Class, Party & Prize Giving Ceremony (04-07-2024)</summary>

## Day 77 (04-07-2024) Topics:
- Last class (Party and prize giving ceremony)
    - Md. Shakil team - School Management Project (`Champion`)
    - My team - To-let Project (`1st Runners-up`)
    - Md. Rejone Hossain team - Hospital Management Project (`2nd Runners-up`)

</details>

<details>
<summary>Day-78-Final Assessment Day (08-07-2024)</summary>

## Day 78 (08-07-2024) Topics:
- Final Assessment Day
    - Initial assessment start at 10:00 AM
    - Written Exam (MCQ and Short Question) start at 10:30 AM
    - Demonstration (Project) first 2 hours start at 11:30 AM and break at 01:30 PM
    - Last 2 hours start at 03:00 PM
    - Demonstration (Project) time ended at 05:00 PM
    - Oral test and project showcase started at 05:30 PM and ended at 7:10 PM
    - Final result at 08:15 PM
        - Total student = 24
        - Competent = 13
        - Not Yet Competent = 10
        - Absent = 1

<div align="center">
  <img src="https://github.com/aatansen/Web-Application-Development-with-Python-Level-04-Batch-03/blob/main/Day-65-Full%20Job%20Portal%20Project%20using%20Normal%20Form/jobProject/media/profile_picture/end.jpg" alt="end" width="400" />
</div>

</details>
