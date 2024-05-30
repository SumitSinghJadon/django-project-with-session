from django.shortcuts import render
from django.core.mail import send_mail
from .models import *

# Create your views here.

def home(request):
    Username=request.session.get('Username')
    Email=request.session.get('Email')
    Password=request.session.get('Password')
    Id=request.session.get('Id')
    userdata={
        "username":Username,
        "email":Email,
        "id":Id,
        "password":Password  
    }
    return render(request,'home.html',{"userdata":userdata})

def about(request):
    Username=request.session.get('Username')
    Email=request.session.get('Email')
    Password=request.session.get('Password')
    Id=request.session.get('Id')
    userdata={
        "username":Username,
        "email":Email,
        "id":Id,
        "password":Password  
    }
    return render(request,'about.html',{"userdata":userdata})

def contact(request):
    Username=request.session.get('Username')
    Email=request.session.get('Email')
    Password=request.session.get('Password')
    Id=request.session.get('Id')
    userdata={
        "username":Username,
        "email":Email,
        "id":Id,
        "password":Password  
    }
    return render(request,'contact.html',{"userdata":userdata})

def registration(request):
    return render(request,'registration.html')

def dashboard(request):
    Username=request.session.get('Username')
    Email=request.session.get('Email')
    Password=request.session.get('Password')
    Id=request.session.get('Id')
    userdata={
        "username":Username,
        "email":Email,
        "id":Id,
        "password":Password  
    }
    return render(request,'dashboard.html',{"userdata":userdata})

def submit_registration(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    data=Regstration.objects.filter(Email=email)
    if data:
       msg="user already"
       return render(request,'registration.html',{'key':msg})
    else:
        if(password==cpassword):
            Regstration.objects.create(Username=username,
                                       Email=email,
                                       Password=password)
            msg="Regstration successfully"
            subject="New Regstration"
            message=username+email
            from_email="sumitjadon026@gmail"
            recipient_list=["vishaljadon144@gmail.com",]
            send_mail(subject,message,from_email,recipient_list)
            return render(request,'login.html',{'key':msg})
        else:
            msg="Password & Confirm password not match"
            return render(request,'registration.html',{'key':msg})
            
        

def login(request):
    return render(request,'login.html')

def submitlogin(request):
    print(request.POST)
    email=request.POST.get('email')
    password=request.POST.get('password')
    
    user=Regstration.objects.filter(Email=email)   
    if user:
        data=Regstration.objects.get(Email=email)
        Password=data.Password
        Username=data.Username
        Email=data.Email
        id=data.id
        if Password==password:
            request.session['Username']=Username
            request.session['Email']=Email
            request.session['Password']=Password
            request.session['Id']=id
            
            Username=request.session.get('Username')
            Email=request.session.get('Email')
            Password=request.session.get('Password')
            Id=request.session.get('Id')
            userdata={
                "username":Username,
                "email":Email,
                "id":Id,
                "password":Password  
            }
            return render(request,'dashboard.html',{"userdata":userdata}) 
        else:
            msg="Email & password not match"            
            return render(request,'login.html',{'key':msg})
    else:
        msg="enter vaild email" 
        return render(request,'login.html',{'key':msg})      

def logout(request):
    if request.session:
        request.session.flush()
        return render(request,'login.html')
  
def submitnote(request):
    Email=request.session.get('Email')
    if Email:
        title=request.POST.get('title')
        note=request.POST.get('note')
        email=request.POST.get('email')
        password=request.POST.get('password')
        Notes.objects.create(Title=title,
                                    Note=note,
                                    Email=email,
                                    Password=password)
        notedata=Notes.objects.filter(Email=email)
        Username=request.session.get('Username')
        Email=request.session.get('Email')
        Password=request.session.get('Password')
        Id=request.session.get('Id')
        userdata={
            "username":Username,
            "email":Email,
            "id":Id,
            "password":Password  
        }
        return render(request,'dashboard.html',{"userdata":userdata,"key":notedata})     
    else:
        msg="please login" 
        return render(request,'login.html',{'key':msg})  
        

def shownotes(request):
    email=request.POST.get('email') 
    Email=request.session.get('Email')
    if Email:
        notedata=Notes.objects.filter(Email=email)
        Username=request.session.get('Username')
        Email=request.session.get('Email')
        Password=request.session.get('Password')
        Id=request.session.get('Id')
        userdata={
            "username":Username,
            "email":Email,
            "id":Id,
            "password":Password  
        }
        return render(request,'dashboard.html',{"userdata":userdata,"key":notedata})     
    else:
        msg="please login" 
        return render(request,'login.html',{'key':msg})  

def delete(request,pk):
    email=request.POST.get('email')
    data=Notes.objects.filter(id=pk)
    Email=request.session.get('Email')
    if data:       
        datadel=Notes.objects.get(id=pk)
        datadel.delete()
    if Email:
        notedata=Notes.objects.filter(Email=email)
        Username=request.session.get('Username')
        Email=request.session.get('Email')
        Password=request.session.get('Password')
        Id=request.session.get('Id')
        userdata={
            "username":Username,
            "email":Email,
            "id":Id,
            "password":Password  
        }
        return render(request,'dashboard.html',{"userdata":userdata,"key":notedata})     

def Edit(request,pk):
    Email=request.session.get('Email')
    dataEdit=Notes.objects.get(id=pk)
    if Email:
        Username=request.session.get('Username')
        Email=request.session.get('Email')
        Password=request.session.get('Password')
        Id=request.session.get('Id')
        userdata={
            "username":Username,
            "email":Email,
            "id":Id,
            "password":Password  
        }
        return render(request,'dashboard.html',{"userdata":userdata,"dataEdit":dataEdit}) 
    
    
    

def updatenote(request,pk):
    updatedata=Notes.objects.get(id=pk)
    updatedata.Title=request.POST.get('title')
    updatedata.Note=request.POST.get('note')
    updatedata.save()
    email=request.POST.get('email')
    notedata=Notes.objects.filter(Email=email)
    Email=request.session.get('Email')
    if Email:
        Username=request.session.get('Username')
        Email=request.session.get('Email')
        Password=request.session.get('Password')
        Id=request.session.get('Id')
        userdata={
            "username":Username,
            "email":Email,
            "id":Id,
            "password":Password  
        }
        
        return render(request,'dashboard.html',{"userdata":userdata,"key":notedata}) 

    

def filter(request):
    email=request.POST.get('email')
    Startdate=request.POST.get('startdate')
    Enddate=request.POST.get('enddate')
    notedata=Notes.objects.filter(Email=email,Date__range=[Startdate,Enddate])
    Email=request.session.get('Email')
    if Email:
        Username=request.session.get('Username')
        Email=request.session.get('Email')
        Password=request.session.get('Password')
        Id=request.session.get('Id')
        userdata={
            "username":Username,
            "email":Email,
            "id":Id,
            "password":Password  
        }
        
        return render(request,'dashboard.html',{"userdata":userdata,"key":notedata}) 

    