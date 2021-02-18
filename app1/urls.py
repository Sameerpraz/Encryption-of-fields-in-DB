#drf

from rest_framework import routers
from app1.views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', CustomerViewSet)



urlpatterns = [
   # path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
  
   # path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+router.urls