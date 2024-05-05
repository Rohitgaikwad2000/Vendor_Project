from Vender.views import (
    VenderModelViewSet,
    PurchaseModelViewSet,
    HistoricalModelViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"vendors", VenderModelViewSet, basename="vendors")
router.register(r"Purchase", PurchaseModelViewSet, basename="Purchase")
router.register(r"Historical", HistoricalModelViewSet, basename="Historical")

newurlpatterns = router.urls
