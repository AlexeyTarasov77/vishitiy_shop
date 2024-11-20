from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("accounts/", include("users.urls", namespace="users")),
    path("products/", include("products.urls", namespace="products")),
    path("email_form/", include("payments.urls", namespace="email_form")),
    path("cart/", include("cart.urls", namespace="cart")),
    path("payments/", include("payments.urls", namespace="payments")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
