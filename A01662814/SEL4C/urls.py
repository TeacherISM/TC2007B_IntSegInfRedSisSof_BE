from django.urls import include, path
from rest_framework import routers
from SEL4C.app1 import views
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView, SpectacularRedocView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'reports', views.ReportViewSet)

#Wire up our API using automatic URL routing.
# Additionally, we include login URLS for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(),name = 'schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name="schema"), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name="schema"), name='redoc'),
]