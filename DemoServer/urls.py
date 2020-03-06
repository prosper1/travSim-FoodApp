from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from food import views
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = "CheF's Delight ";
admin.site.site_title = "Chef's Delight ";


router = routers.DefaultRouter()
router.register(r'food',views.FoodViewSet)
router.register(r'order', views.OrderViewSet)
# router.register(r'cancel-order',views.OrderCancelViewSet)
router.register(r'user',views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('rest-auth/',include('rest_auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

