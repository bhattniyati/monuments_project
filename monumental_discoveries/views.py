from django.shortcuts import render,HttpResponseRedirect, redirect
from django.contrib import messages
from .models import User
from .utils import validate_data
from django.contrib.auth.hashers import make_password



# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):
    if request.POST:
        status, error_list = validate_data(request.POST)

        if status:
            hashed_password = make_password(request.POST["password"])
            User.objects.create(first_name=request.POST["fname"],last_name=request.POST["lname"],
                                email=request.POST["email"], phone_no=request.POST["phoneno"],
                                password=hashed_password, username=request.POST["uname"],
                                gender=request.POST["gender"]
                                )
            return redirect("home")

        if len(error_list) == 1:
            message = error_list[0]
        elif len(error_list) == 2:
            message = str(error_list[0]) + " and " + str(error_list[1])
        else:
            comma_separated = ", ".join(error_list[:-1])
            message = f"{comma_separated} and {error_list[-1]}"

        messages.error(request, message)
        return redirect('signup')

    return render(request, "registration.html")

def login(request):
    return render(request, "login.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def service(request):
    return render(request, "portfolio.html")
