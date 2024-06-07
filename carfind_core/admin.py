from django.contrib import admin
from .models import Make, Model, Offer, EngineType, OfferImage

admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Offer)
admin.site.register(EngineType)
admin.site.register(OfferImage)