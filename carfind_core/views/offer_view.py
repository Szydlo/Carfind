from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from ..models import Make, Model, EngineType, Offer, OfferImage

def isNull(var):
    if var == "" or var is None:
        return True
    
    return False

@login_required
def offer_delete(request, offer_id):
    offer = Offer.objects.filter(user=request.user, pk=offer_id).first()

    if not offer:
        return HttpResponseRedirect(reverse("carfind_core:index"))

    offer.delete()

    return HttpResponseRedirect(reverse("carfind_core:user_account"))

@login_required
def offer_edit(request, offer_id):
    offer = Offer.objects.filter(user=request.user, pk=offer_id).first()

    if not offer:
        return HttpResponseRedirect(reverse("carfind_core:index"))
    
    make = request.POST.get("make")
    model = request.POST.get("model")
    price = request.POST.get("price")
    mileage = request.POST.get("mileage")
    power = request.POST.get("engine_power")
    displacement = request.POST.get("engine_displacement")
    engine_type = request.POST.get("engine_type")
    phone_number = request.POST.get("phone_number")
    description = request.POST.get("description")
    production_date = request.POST.get("prod_date")
    location = request.POST.get("location")

    model = Model.objects.filter(make=make, name=model).first()

    engine_type = EngineType.objects.filter(pk=engine_type).first()

    offer.model = model
    offer.engine_type = engine_type

    offer.price = price
    offer.mileage = mileage
    offer.engine_power = power
    offer.engine_size = displacement
    offer.phone_number = phone_number
    offer.description = description
    offer.production_date = production_date
    offer.location = location

    offer.save()

    return HttpResponseRedirect(reverse("carfind_core:user_account"))

@login_required
def user_edit_form(request, offer_id):
    offer = Offer.objects.filter(user=request.user, pk=offer_id).first()

    if not offer:
        return HttpResponseRedirect(reverse("carfind_core:index"))

    return render(request, "../templates/carfind/account/edit_offer.html", {
        "offer" : offer,
        "makes" : Make.objects.all(),
        "engine_types" : EngineType.objects.all(),
    })

def offer_preview(request, offer_id):
    offer = Offer.objects.filter(pk=offer_id).first()

    if not offer:
        return HttpResponseRedirect(reverse("carfind_core:index"))

    offerImgs = OfferImage.objects.filter(offer=offer)
    offer.thumbmail = OfferImage.objects.filter(offer=offer).first()

    return render(request, "../templates/carfind/preview.html", {
        "offer" : offer,
        "offerImgs" : offerImgs,
    })

@login_required
def add_offer(request):
    return render(request, "carfind/account/add_offer.html", {
        "makes" : Make.objects.all(),
        "engine_types" : EngineType.objects.all(),
    })

def add_offer_form(request):
    make = request.POST.get("make")
    model = request.POST.get("model")
    price = request.POST.get("price")
    mileage = request.POST.get("mileage")
    power = request.POST.get("engine_power")
    displacement = request.POST.get("engine_displacement")
    engine_type = request.POST.get("engine_type")
    phone_number = request.POST.get("phone_number")
    description = request.POST.get("description")
    production_date = request.POST.get("prod_date")
    location = request.POST.get("location")

    model = Model.objects.filter(make=make, name=model).first()
    engine_type = EngineType.objects.filter(pk=engine_type).first()

    offer = Offer(
        model = model,
        user = request.user,
        price = price,
        mileage = mileage,
        description = description,
        engine_size = displacement,
        engine_power = power,
        engine_type = engine_type,
        production_date = production_date,
        location = location,
        phone_number = phone_number,
    )

    offer.save()

    for f in request.FILES.getlist('file_images'):
        img = OfferImage()
        img.offer = offer
        img.image = f
        img.save()

    return HttpResponseRedirect(reverse("carfind_core:user_account"))