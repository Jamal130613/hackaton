from applications.cart.views import OrderView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', OrderView)


urlpatterns = []

urlpatterns.extend(router.urls)