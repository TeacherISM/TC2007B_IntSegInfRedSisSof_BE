from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from SEL4C.app1 import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r'home', views.HomeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path("api/schema/redoc/", SpectacularRedocView.as_view(), name='redoc-ui'),


]
#swagger y regor
