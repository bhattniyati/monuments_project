from django.shortcuts import render,HttpResponseRedirect, redirect
from django.contrib import messages
from .models import *
from .utils import validate_data
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


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
    states = State.objects.all()
    return render(request, "services.html", context={'states': states})

def booking_service(request, name):
    context = {}
    if name:
        city = City.objects.filter(city_name__iexact=name).first()
        if city:
            if city.state_id.quote:
                context['quote'] = city.state_id.quote
            context['monuments'] = city.monuments_cities.all()

    return render(request, "booking_service.html", context)

def get_cities_view(request, state_id):
    state = get_object_or_404(State, pk=state_id)
    cities = state.cities.values_list('city_name', flat=True)  # Assuming the related name for cities is 'city_set'

    return JsonResponse(list(cities), safe=False)

