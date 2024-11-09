from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("get_algolia_credentials/", views.get_algolia_credentials_view, name="get_algolia_credentials"),
    path("about_us/", views.about_us_view, name="about_us"),
    path("contacts/", views.contacts_view, name="contacts"),
]
