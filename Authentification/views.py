from django.shortcuts import render
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from Authentification.forms import CreateUserForm
 
def signin (request):
    logout(request)
    if request.method == 'POST' :
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(request , username = username , password = password)
        #print(user.groups)
        if user is not None :
            login(request , user)
            print("User Authentificated succesfully")
            print(request.user.username)
            #return redirect ('Courses:home_admin')
        else:
            messages = "username or password is incorect"
            context = {'message' : messages} 
            return render(request , 'Authentification/signin.html' , context )
    return render(request , 'Authentification/signin.html' )

def signup(request):
    form = CreateUserForm()
    print("FORM")
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
     
    return render(request, 'Authentification/signup.html', {'f': form})