from django.urls import include, path
from rest_framework import routers
from SEL4C.app1 import views
from drf_spectacular.views import SpectacularAPIView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'home', views.HomeViewSet)

# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]