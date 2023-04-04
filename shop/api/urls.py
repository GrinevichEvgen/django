from django.contrib.auth.views import LoginView

from api.users.views import RegistertView
from api.products.views import ProductsViewSet
from django.urls import include, path
from rest_framework import routers

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductsViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegistertView.as_view(), name="register"),
    path("login/" , LoginView.as_view)
]
