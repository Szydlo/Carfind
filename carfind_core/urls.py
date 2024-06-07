from django.urls import path

from .views import views, account_view, offer_view

app_name = "carfind_core"
urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.list, name="list"),
    path("api/make/<int:make_id>", views.api_make, name="api_make"),


    path("account/dashboard", account_view.account, name="user_account"),
    path("account/add_offer", offer_view.add_offer, name="add_offer"),
    path("account/add_offer_form", offer_view.add_offer_form, name="add_offer_form"),
    path("account/edit_offer/<int:offer_id>", offer_view.user_edit_form, name="user_edit_offer"),

    path("account/logout", account_view.user_logout, name="user_logout"),
    path("account/login_form", account_view.user_login_form, name="user_login_form"),
    path("account/login", account_view.user_login, name="user_login"),

    path("account/register_form", account_view.user_register_form, name="user_register_form"),
    path("account/register", account_view.user_register, name="user_register"),


    path("offer/delete/<int:offer_id>", offer_view.offer_delete, name="offer_delete"),
    path("offer/edit/<int:offer_id>", offer_view.offer_edit, name="offer_edit"),
    path("offer/preview/<int:offer_id>", offer_view.offer_preview, name="offer_preview"),
]