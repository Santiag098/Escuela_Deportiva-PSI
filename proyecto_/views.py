from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
#Metodos para renderizar
def inicio(requuest):
    return HttpResponse("Hola Django")

def landing(request):
    return render(request,'index.html')

# Metodos de Project
@login_required
def listProjects(request):
    projects = Project.objects.all()
    return render(request,'Projects/list.html',{"projects":projects})

@login_required
def showFormCreateProject(request):
    return render(request,'Projects/create.html')

@login_required
def storeProject(request):
    project = Project.objects.create(
        name=request.POST["name"],
        code=request.POST["code"],
        date=request.POST["date"],
        phone=request.POST["phone"]
    )
    
    project.save()
    return redirect('projects.list')

@login_required
def showFormEditProject(request,project_id):
    project = get_object_or_404(Project, id = project_id)
    return render(request,'Projects/edit.html',{
        'project': project
    })

@login_required
def updateProject (request, project_id):
    project = get_object_or_404(Project,id = project_id)
    project.name = request.POST["name"]
    project.date = request.POST["date"]
    project.code = request.POST["code"]
    project.phone = request.POST["phone"]
    
    project.save()
    return redirect('projects.list')

def showConfirmDelete(request, project_id):
    project = get_object_or_404(Project,id = project_id)
    return render(request,'Projects/delete.html',{
        'project': project
    })

@login_required
def destroyProject(request, project_id):
    project = get_object_or_404(Project,id = project_id)
    project.delete()
    return redirect('projects.list')

def showSignupForm(request):
    return render(request, 'users/signup-form.html')

def signup(request):
    if(request.POST['password'] == request.POST['password2']):
        try:
            user = User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"]
            )
            user.save()
            login(request, user)
            return redirect('projects.list')
        except:
            return HttpResponse("Something was wrong")
    else:
        return HttpResponse("The password fields don't watch")

def showLoginForm(request):
    return render(request, 'users/login-form.html')

def startSession(request):
    user = authenticate(
        request=request,
        username=request.POST["username"],
        password=request.POST["password"])

    if(user is None):
        messages.add_message(request=request, level=messages.ERROR, message= 'Wrong credentials, try again')
        return redirect('login-form')
    else:
        login(request, user)
        return redirect('projects.list')

@login_required
def finishSession(request):
    logout(request)
    return redirect('Home')
