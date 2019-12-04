from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Login Successful!')
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                #print("Username already present!")
                messages.info(request,"Username Already Taken!")
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                #print("Email already taken!")
                messages.info(request,"Email Already Taken!")
                return redirect('register')

            else:  
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstname, last_name=lastname)
                user.save()
                print('User Created!')
                #messages.info(request,"User Successfully Created!")
                return redirect('')
        else:
            # print('Password not matching!')
            messages.info(request,"Password and Confirm Password not matching!")
            return redirect('register')
        
    else:
        return render(request,'register.html')