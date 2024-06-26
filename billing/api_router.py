from core import settings
from django.urls import path, include
from rest_framework_nested import routers

from billing.views.auth import APIRegistrationView, APILoginView
from billing.views.products import ProductViewSet
from billing.views.customers import CustomerViewSet
from billing.views.billings import BillViewSet
from billing.views.analytics import Analytics

app_name = "billing"

router = routers.SimpleRouter(trailing_slash=False)
if settings.DEBUG:
    router = routers.DefaultRouter(trailing_slash=False)

router.register(r"products", ProductViewSet)
router.register(r"customers", CustomerViewSet)
router.register(r"bills", BillViewSet)


auth_urls = [
    path("register", APIRegistrationView.as_view(), name="register"),
    path("login", APILoginView.as_view(), name="login"),
]

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include(auth_urls)),
    path("analytics", Analytics.as_view(), name="analytics"),
]
