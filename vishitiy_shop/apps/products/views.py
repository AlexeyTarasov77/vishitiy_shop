from typing import Any

from django import http
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, EmailMultiAlternatives
from django.db.models import QuerySet
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views import generic
from django.utils.translation import gettext as _
from django.core.files.uploadedfile import InMemoryUploadedFile

from products import filters, forms, models


class ProductListView(generic.ListView):
    template_name = "products/product_list.html"
    queryset = models.Product.objects.all().select_related("collection")

    def get_template_names(self) -> list[str]:
        if self.request.headers.get("Hx-Request") == "true":  # if request is ajax
            print("is ajax")
            return ["products/includes/product_list_p.html"]
        return super().get_template_names()

    def get_queryset(self) -> QuerySet[models.Product]:
        qs = super().get_queryset()
        self.filterset = filters.ProductFilter(self.request.GET, queryset=qs)
        return self.filterset.qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


class ProductDetailView(generic.DetailView):
    queryset = models.Product.objects.all().select_related("collection")
    template_name = "products/product_detail.html"


class CustomDesignView(LoginRequiredMixin, generic.FormView):
    form_class = forms.CustomDesignForm
    template_name = "products/custom_design.html"
    success_url = reverse_lazy("main:index")

    def form_valid(self, form: forms.CustomDesignForm) -> http.HttpResponse:
        data = form.cleaned_data
        user = self.request.user
        context = {**data, "user": user}
        print(context)
        email_html_content = render_to_string("products/email_custom_design.html", context)
        email_plain_content = strip_tags(email_html_content)
        mail = EmailMultiAlternatives(
            f"{user.username}'s Customized Design",
            email_plain_content,
            from_email=user.email,
            to=[settings.ADMIN_EMAIL],
        )
        mail.attach_alternative(email_html_content, "text/html")
        design_image: InMemoryUploadedFile | None = data.get("design_image")
        if design_image:
            with design_image.open("rb") as f:
                mail.attach(_("design_image"), f.read(), f.content_type)
                print("FILE ATTACHED")
        mail.send()
        # send_mail(
        #     f"{user.username}'s Customized Design",
        #     email_plain_content,
        #     from_email=user.email,
        #     recipient_list=[settings.ADMIN_EMAIL],
        #     html_message=email_html_content,
        # )
        messages.success(
            self.request,
            "Ви залишили заявку на створення дизайну. Менеджер зв'яжеться з вами через деякий час",
        )
        return super().form_valid(form)
