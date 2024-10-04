from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .form import RegisterUserForm
from django.contrib.auth import login, logout, authenticate
from .form import LoginUser
# Create your views here.
def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, "signup.html", {"form": form})

def login_user(request):
    if request.POST == "POST":
        form = LoginUser(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginUser()

    return render(request, 'login.html', {"form": form})