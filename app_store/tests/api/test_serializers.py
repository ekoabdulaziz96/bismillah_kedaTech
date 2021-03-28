from django.test import TestCase

from app_store.api import serializers
from app_store import models

# import pdb; pdb.set_trace() 

class TestApiSerializersSupplier(TestCase):
    """
    pada test ini, menguji validasi dari sebuah data yg diterima kelas Form.
    """
    def testSupplier__apiSerializerValidData(self):
        serializer = serializers.SerializerModelSupplier(data = {
            'name' :   'testName1',
        })
        self.assertTrue(serializer.is_valid()) # True

    def testSupplier__apiSerializerNoData(self):
        serializer = serializers.SerializerModelSupplier(data = {})

        self.assertFalse(serializer.is_valid()) #False
        self.assertEquals(len(serializer.errors), 1) #error = 1, utk data name yg kosong

class TestApiSerializersMaterial(TestCase):
    """
    pada test ini, menguji validasi dari sebuah data yg diterima kelas Form.
    """
    def setUp(self):
        self.supplier1 = models.Supplier.objects.create(name='supplier1')
        self.dataNoSupplier = {
            # 'supplier' : supplier1,
            'code' :   'code1',
            'name' :   'name1',
            'type' :   models.Material.TYPE_CHOICES[0][0],
            'buyPrice' :   10000,
        }

    def testSupplier__apiSerializerValidData(self):
        self.dataNoSupplier['supplier'] = self.supplier1.id
        serializer = serializers.SerializerModelMaterial(data=self.dataNoSupplier)
        self.assertTrue(serializer.is_valid()) # True

    def testSupplier__apiSerializerNoData(self):
        serializer = serializers.SerializerModelMaterial(data = {})

        self.assertFalse(serializer.is_valid()) #False
        self.assertEquals(len(serializer.errors), 5) #error = 5, utk data supplier, code, name, type, buyPrice yg kosong
 
    def testSupplier__apiSerializerNoData_supplierRefference(self):
        serializer = serializers.SerializerModelMaterial(data = self.dataNoSupplier)

        self.assertFalse(serializer.is_valid()) #False
        self.assertEquals(len(serializer.errors), 1) #error = 1, utk data supplier, yg kosong

    def testSupplier__apiSerializerNoValidDataType(self):
        self.dataNoSupplier['supplier'] = self.supplier1.id
        self.dataNoSupplier['type'] = 'SUTRA'
        serializer = serializers.SerializerModelMaterial(data = self.dataNoSupplier)

        self.assertFalse(serializer.is_valid()) #False
        self.assertEquals(len(serializer.errors), 1) #error = 1, utk data type, yg tidak sesuai pilihan [FABRIC,JEANS, COTTON  ]
