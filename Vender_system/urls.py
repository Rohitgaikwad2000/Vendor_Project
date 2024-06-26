"""
URL configuration for Vender_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from Vender.urls import newurlpatterns
from Vender.views import VendorPerformanceAPIView, PurchaseViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("api/", include(newurlpatterns)),
    path("api/<int:id>", include(newurlpatterns)),
    path("api/", include(newurlpatterns)),
    path("api/<int:id>", include(newurlpatterns)),
    path("api/", include(newurlpatterns)),
    path("api/<int:pk>", include(newurlpatterns)),
    path("", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "api/vendors/<int:pk>/Performance/",
        VendorPerformanceAPIView.as_view(),
        name="VendorPerformanceAPIView",
    ),
    path(
        "api/purchase_orders/<int:pk>/acknowledge/",
        PurchaseViewSet.as_view({"post": "acknowledge"}),
    ),
]
