from django.shortcuts import render,get_object_or_404 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from employee.forms import UserForm
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from ems.decorators import role_required,admin_only
from django.urls import reverse 

# Create your views here.
# 
@login_required(login_url="/login/")
def employee_list(request):
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employees'
    print( "role" , request.role)
    return render(request,"employee/index.html",context)

@login_required(login_url="/login/")
def employee_details(request,id=None):
    context = {}
    context['users'] = get_object_or_404( User,id=id)
    context['title'] = 'Employees'
    return render(request,"employee/details.html",context)

@login_required(login_url="/login/")
# @role_required(allowed_roles=['Admin','HR'])
@admin_only
def employee_add(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request,'employee/add.html' , {'user_form' : user_form})
    
    else:
        user_form = UserForm()
        return render(request,"employee/add.html" , {'user_form' : user_form} )

@login_required(login_url="/login/")
def  employee_edit(request,id=None):
    user = get_object_or_404(User, id=id)
    if request.method =="POST":
        user_form = UserForm(request.POST,instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request,'employee/edit.html' , {'user_form' : user_form})
        
    else:
        user_form = UserForm(instance=user)
        return render(request,"employee/edit.html" , {'user_form' : user_form} )

@login_required(login_url="/login/")
def employee_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'employee/delete.html', context)

    
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaa" , username)
        print("passwordpasswordpassword" , password)


        user = authenticate(request,username=username,password=password)
        if user:
            if request.GET.get('next' , None):
                return HttpResponseRedirect(request.GET['next'])
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
            login(request,user)
            return HttpResponseRedirect(reverse('success'))
        else:
            context["error"] = "Provide Valid Credential"
            return render(request,"auth/login.html" , context)
    else:
        return render(request,"auth/login.html" , context)

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('login'))

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request,"auth/success.html")

