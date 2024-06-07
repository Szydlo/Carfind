from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from ..models import Make, Model, EngineType, Offer, OfferImage

def index(request):
    return render(request, "../templates/carfind/index.html", {
        "makes" : Make.objects.all()
    })

def api_make(request, make_id):
    get_object_or_404(Make, pk=make_id)
    models = Model.objects.filter(make__pk = make_id)

    return JsonResponse(serializers.serialize("json", models), safe=False)

def isNull(var):
    if var == "" or var is None:
        return True
    
    return False

def list(request):
    offers = Offer.objects.all()

    # There has to better solution for this @ TODO

    make = request.GET.get("make")
    model = request.GET.get("model")

    price_from = request.GET.get("price_from")
    price_to = request.GET.get("price_to")

    mileage_from = request.GET.get("mileage_from")
    mileage_to = request.GET.get("mileage_to")
    
    power_from = request.GET.get("power_from")
    power_to = request.GET.get("power_to")

    displacement_from = request.GET.get("displacement_from")
    displacement_to = request.GET.get("displacement_to")

    engine_type = request.GET.get("engine_type")

    if (not isNull(make)):
        offers = offers.filter(model__make=make)
    if (not isNull(model)):
        offers = offers.filter(model__name=model)

    if (not isNull(price_from)): offers = offers.filter(price__gte=int(price_from))
    if (not isNull(price_to)): offers = offers.filter(price__lte=int(price_to))

    if (not isNull(mileage_from)): offers = offers.filter(mileage__gte=int(mileage_from))
    if (not isNull(mileage_to)): offers = offers.filter(mileage__lte=int(mileage_to))

    if (not isNull(power_from)): offers = offers.filter(engine_power__gte=int(power_from))
    if (not isNull(power_to)): offers = offers.filter(engine_power__lte=int(power_to))

    if (not isNull(displacement_from)): offers = offers.filter(engine_size__gte=int(displacement_from))
    if (not isNull(displacement_to)): offers = offers.filter(engine_size__lte=int(displacement_to))

    if (not isNull(engine_type)): offers = offers.filter(engine_type=int(engine_type))

    if (not isNull(make)): make = int(make)

    for offer in offers:
        offer.thumbmail = OfferImage.objects.filter(offer=offer).first()

    return render(request, "../templates/carfind/list/list.html", {
        "makes" : Make.objects.all(),
        "selectedMake" : make,
        "selectedModel" : model,
        "offers" : offers,
        "engineTypes" : EngineType.objects.all()
    })