from django.conf.urls import url
from rest_framework import routers
from .views import StockViewSet

router = routers.DefaultRouter()
router.register(r'stocks', StockViewSet)

urlpatterns = router.urls
