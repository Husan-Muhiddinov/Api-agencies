from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacilityViewSet, MonthlyAgencyViewSet, PricedAgencyViewSet, AgencyViewSet

router = DefaultRouter()
router.register(r'agencies', AgencyViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'agencies/monthly', MonthlyAgencyViewSet, basename='monthly-agencies')
router.register(r'agencies/prices', PricedAgencyViewSet, basename='priced-agencies')


urlpatterns = [
    path('', include(router.urls)),
]
