from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Pay
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
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
    return render(request,'Projects/list.html',{
        "projects":projects
        })
    
@login_required
def detailOfProject(request,project_id):
    project = get_object_or_404(Project, id=project_id) 
    pay = Pay.objects.filter(project_id=project_id)
    return render(request,'projects/detail.html',{
        "project": project,
        "pay" : pay
    })

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

#anexo
@login_required
def pay(request):
    pays = Pay.objects.filter(user=request.user)#user
    return render(request,'pay/pay_list.html',{
        "pays": pays
    })

@login_required
def showCreatePayForm(request):
    # pays = Pay.objects.all()
    projects = Project.objects.all()
    return render(request,'pay/create.html',{
        "projects" : projects
    })

@login_required
def storePay(request):
    pay = Pay.objects.create(
        credit_num=request.POST['credit_num'],
        due_date=request.POST['due_date'],
        security_code=request.POST['security_code'],
        amount_paid=request.POST['amount_paid'],
        description=request.POST['description'],
        project_id=request.POST['project_id']
    )

    return redirect('pay.list')


@login_required
def showUpdatePayForm(request, pay_id):
    projects = Project.objects.all()#user
    pay = get_object_or_404(Pay, id=pay_id)
    return render(request,'pay/update.html',{
        "projects" : projects,
        "pay": pay
    })

@login_required
def updatePay(request,pay_id): 
    pay = get_object_or_404(Pay, id=pay_id)
    pay.credit_num=request.POST["credit_num"]
    pay.due_date=request.POST['due_date']
    pay.security_code=request.POST['security_code']
    pay.amount_paid=request.POST["amount_paid"]
    pay.description=request.POST['description'] 
   
    
    pay.save()
    return redirect('pay.list')

@login_required
def confirmDeletePay(request,pay_id):
    pay = get_object_or_404(Pay, id=pay_id)
    return render(request, "pay/delete.html", {
        "pay": pay
    })

@login_required
def destroyPay(request ,pay_id):#
    pay = get_object_or_404(Pay, id=pay_id)
    pay.delete()
    return redirect('pay.list')


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

@login_required
def showFormEditPay(request,Pay_id):
    pay = get_object_or_404(Pay, id = Pay_id)
    return render(request,'pay/edit.html',{
        'pay': pay
    })
@login_required
def pay_list(request):
    pays = Pay.objects.all()
    return render(request, 'pay/pay_list.html', {'pays': pays})
