from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.main, name="index"),
    path("create-contract", views.create_contract, name="create_contract"),
]
