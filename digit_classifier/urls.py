from .views import DigitViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'digit_classifier', DigitViewSet)

urlpatterns = router.urls