from django.urls import path

from products import views

app_name = "products"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("detail/<slug:slug>/", views.ProductDetailView.as_view(), name="detail"),
    path("custom-design/", views.CustomDesignView.as_view(), name="custom-design"),
]
