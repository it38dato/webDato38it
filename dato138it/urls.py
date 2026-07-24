from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from webApp import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('webApp.urls')),
    #path('ckeditor/',include('ckeditor_uploader.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('', views.contents),
    #path('urls-rest/', include('webApp.urls')),    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui',),
    #path('api/redoc/',SpectacularRedocView.as_view(url_name='schema'),name='redoc',),
    # Swagger UI
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui',),
    # ReDoc
    path('api/schema/redoc/',SpectacularRedocView.as_view(url_name='schema'),name='redoc',),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)