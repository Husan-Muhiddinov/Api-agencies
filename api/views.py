from rest_framework import viewsets
from .models import AgencyModel, FacilityModel
from .serializers import AgencySerializer, FacilitySerializer
from .permissions import IsOwnerOrReadOnly
from django.db.models.functions import ExtractMonth


class AgencyViewSet(viewsets.ModelViewSet):
    queryset = AgencyModel.objects.all()
    serializer_class = AgencySerializer
    permission_classes = [IsOwnerOrReadOnly]


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = FacilityModel.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [IsOwnerOrReadOnly]


class MonthlyAgencyViewSet(viewsets.ModelViewSet):
    serializer_class = AgencySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        month = self.request.query_params.get('month')
        if month:
            facilities = FacilityModel.objects.annotate(month=ExtractMonth('_from')).filter(month=month)
        else:
            return AgencyModel.objects.none()


class PricedAgencyViewSet(viewsets.ModelViewSet):
    serializer_class = AgencySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        price = self.request.query_params.get('price')
        if price:
            return AgencyModel.objects.filter(price=price)
        else:
            return AgencyModel.objects.none()
