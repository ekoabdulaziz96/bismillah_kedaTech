from rest_framework import generics, permissions, renderers

from app_store import models
from . import serializers

#-----------------------------------------------------Supplier
class SupplierList(generics.ListCreateAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SerializerModelSupplier


class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SerializerModelSupplier


#-----------------------------------------------------Material
class MaterialList(generics.ListCreateAPIView):
    queryset = models.Material.objects.all()
    serializer_class = serializers.SerializerModelMaterial


class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Material.objects.all()

    serializer_class = serializers.SerializerModelMaterial

