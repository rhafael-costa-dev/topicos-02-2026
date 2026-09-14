from .models import Marca, Carro
from .serializers import MarcaSerializer, CarroSerializer
from .services import MarcaService
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .filters import CarroFilter

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['nome']

    def perform_create(self, serializer):
        MarcaService.criar(
            nome=serializer.validated_data["nome"],
            pais_origem=serializer.validated_data["pais_origem"]
        )


class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.select_related("marca").all()
    serializer_class = CarroSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_class = CarroFilter  # Usa o filtro avançado customiza