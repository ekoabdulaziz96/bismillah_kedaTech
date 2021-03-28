from django.test import TestCase
from app_store import forms_material,forms_supplier, models

class TestFormsSupplier(TestCase):
    """
    pada test ini, menguji validasi dari sebuah data yg diterima kelas Form.
    """
    def testSupplier_formValidData(self):
        form = forms_supplier.FormSupplier(data = {
            'name' :   'testName1',
        })
        self.assertTrue(form.is_valid()) # True

    def testSupplier_formNoData(self):
        form = forms_supplier.FormSupplier(data = {})

        self.assertFalse(form.is_valid()) #False
        self.assertEquals(len(form.errors), 1) #error = 1, utk data name yg kosong

class TestFormsMaterial(TestCase):
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

    def testSupplier_formValidData(self):
        self.dataNoSupplier['supplier'] = self.supplier1
        form = forms_material.FormMaterial(self.dataNoSupplier)
        self.assertTrue(form.is_valid()) # True

    def testSupplier_formNoData(self):
        form = forms_material.FormMaterial(data = {})

        self.assertFalse(form.is_valid()) #False
        self.assertEquals(len(form.errors), 5) #error = 5, utk data supplier, code, name, type, buyPrice yg kosong
 
    def testSupplier_formNoData_supplierRefference(self):
        form = forms_material.FormMaterial(self.dataNoSupplier)

        self.assertFalse(form.is_valid()) #False
        self.assertEquals(len(form.errors), 1) #error = 1, utk data supplier, yg kosong

    def testSupplier_formNoValidDataType(self):
        self.dataNoSupplier['supplier'] = self.supplier1.id
        self.dataNoSupplier['type'] = 'SUTRA'
        form = forms_material.FormMaterial(self.dataNoSupplier)

        self.assertFalse(form.is_valid()) #False
        self.assertEquals(len(form.errors), 1)#error = 1, utk data type, yg tidak sesuai pilihan [FABRIC,JEANS, COTTON  ]
