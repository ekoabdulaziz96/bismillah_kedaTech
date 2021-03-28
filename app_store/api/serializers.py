from rest_framework import serializers
from app_store import models

class SerializerModelSupplier(serializers.ModelSerializer):

    class Meta:
        model = models.Supplier
        fields = ['url', 'id', 'name']
        extra_kwargs = {
            'url':{'view_name':'as:api-supplier-detail'},
            'name':{'required':True},
        }

class SerializerModelMaterial(serializers.ModelSerializer):


    class Meta:
        model = models.Material
        fields = ['url', 'id','supplier', 'code',
                  'name', 'type', 'buyPrice']
        extra_kwargs = {
            'url':{'view_name':'as:api-material-detail'},
            'code':{'required':True},
            'name':{'required':True},
            'type':{'required':True},
            'buyPrice':{'required':True},

            # 'supplier':{'view_name':'as:api-supplier-detail'},
        }

    def validate_buyPrice(self, value):
        """
        Check that the blog post is about Django.
        """
        if value < 0:
            raise serializers.ValidationError("Harga jual harus lebih besar dari nol")
        return value

