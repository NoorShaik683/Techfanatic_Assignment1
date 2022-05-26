from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from user.forms import UserImage 
from .models import UploadImage  

#################### index#######################################
def index(request):
	return render(request, 'index.html', {'title':'index'})

########### register here #####################################
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Registered.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name, last_name=last_name)
                user.save()
                print("User Created ")
                return redirect('index')
        else:
            messages.info(request,"Password Not matching")
            return redirect('register')
    else:
        return render(request, 'register.html')

################ Login ###################################################
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, f' wecome {username} !!')
            print("Hi")
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            print("ss")
            return redirect('login')
    return render(request, 'login.html')


################ Logout ###################################################
def logout(request):
    auth.logout(request)
    return redirect('/')


def image_request(request):  
    if request.method == 'POST':  
        form = UserImage(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
            print(img_object,request.user)
              
            return render(request, 'index.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImage()  
  
    return render(request, 'index.html', {'form': form})  

def editProfile(request):
    if request.method=="POST":
        username=request.POST['username']
        if request.username==username:
            print("Same User")
    return render(request,'edit.html')