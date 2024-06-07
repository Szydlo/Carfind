from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from ..models import Offer, OfferImage
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse("carfind_core:index"))

def user_login(request):
    return render(request, "carfind/account/login.html")

def user_register(request):
    return render(request, "carfind/account/register.html")
    
def user_login_form(request):
    user = authenticate(username=request.POST["login"], password=request.POST["password"])

    if user is None:
        return render(request, "carfind/login.html", {"error_message" : "Wrong login or password"})

    login(request, user)

    return HttpResponseRedirect(reverse("carfind_core:index"))

def user_register_form(request):
    if (request.POST["password"] != request.POST["repeatpassword"]):
        return render(request, "carfind/register.html", {"error_message" : "Passwords don't match!"})

    user = User.objects.create_user(request.POST["login"], request.POST["email"], request.POST["password"])
    user.save()

    return HttpResponseRedirect(reverse("carfind_core:user_login"))


@login_required
def account(request):
    offers = Offer.objects.filter(user=request.user)

    for offer in offers:
        offer.thumbmail = OfferImage.objects.filter(offer=offer).first()

    return render(request, "carfind/account/dashboard.html", {
        "offers" : offers
    })