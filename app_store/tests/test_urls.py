from django.test import SimpleTestCase
from django.urls import reverse, resolve

from app_store import views_supplier, views_material

class TestUrlsSupplier(SimpleTestCase):
    """
    Pada test ini, fokus untuk menguji route (supplier) yang mengarah pada controller/views (supplier) tertentu
    """

    def testSupplier_urlListResolves(self):
        url = reverse('as:supplier-index')
        self.assertEquals(resolve(url).func.view_class, views_supplier.SupplierListView)   

    def testSupplier_urlCreateResolves(self):
        url = reverse('as:supplier-create')
        self.assertEquals(resolve(url).func.view_class, views_supplier.SupplierCreateView)   

    def testSupplier_urlUpdateResolves(self):
        url = reverse('as:supplier-update', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, views_supplier.SupplierUpdateView)

    def testSupplier_urlDeleteResolves(self):
        url = reverse('as:supplier-delete',  kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, views_supplier.SupplierDeleteView)      

class TestUrlsMaterial(SimpleTestCase):
    """
    Pada test ini, fokus untuk menguji route (material) yang mengarah pada controller/views (material) tertentu
    """

    def testMaterial_urlListResolves(self):
        url = reverse('as:material-index')
        self.assertEquals(resolve(url).func.view_class, views_material.MaterialListView)   

    def testMaterial_urlCreateResolves(self):
        url = reverse('as:material-create')
        self.assertEquals(resolve(url).func.view_class, views_material.MaterialCreateView)   

    def testMaterial_urlUpdateResolves(self):
        url = reverse('as:material-update', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, views_material.MaterialUpdateView)

    def testMaterial_urlDeleteResolves(self):
        url = reverse('as:material-delete',  kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, views_material.MaterialDeleteView)      

    def testMaterial_urlDetailResolves(self):
        url = reverse('as:material-detail',  kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, views_material.MaterialDetailView)      
