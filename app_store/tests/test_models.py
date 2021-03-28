from django.test import TestCase
from app_store import models

class TestModels(TestCase):
    """
    test ini berfokus terhadap fields pada Database, sudah sesuai desain ERD atau belum
    """
    def setUp(self):
        self.supplierModel_fields = [f.name for f in models.Supplier._meta.get_fields()]
        self.materialModel_fields = [f.name for f in models.Material._meta.get_fields()]

    def testSupplier_Modelfields(self):
        supplierModel_fields = [f.name for f in models.Supplier._meta.get_fields()]
        supplier_fields = ['id','name'] #ERD
        supplier_fields.append('materials') # filed relasi ke supplier
        
        for field in supplier_fields:
            # iterasi utk setiap field apakah terdapat pada model yg dibuat
            self.assertTrue(field in self.supplierModel_fields)

    def testMaterial_Modelfields(self):
        materialModel_fields = [f.name for f in models.Material._meta.get_fields()]
        material_fields = ['id','supplier', 'code', 'name', 'type', 'buyPrice' ] #ERD
        
        for field in material_fields:
            # iterasi utk setiap field apakah terdapat pada model yg dibuat
            self.assertTrue(field in self.materialModel_fields)

