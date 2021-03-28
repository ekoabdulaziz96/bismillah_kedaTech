from django.test import SimpleTestCase
from django.urls import reverse, resolve

from app_store.api import views as viewsApi

class TestApiUrlsSupplier(SimpleTestCase):
    """
    Pada test ini, fokus untuk menguji route API (supplier) yang mengarah pada controller/views (supplier) tertentu
    """

    def testSupplier__apiUrlListResolves(self):
        url = reverse('as:api-supplier-list')
        self.assertEquals(resolve(url).func.view_class, viewsApi.SupplierList)   

    def testSupplier__apiUrlDetailResolves(self):
        url = reverse('as:api-supplier-detail', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, viewsApi.SupplierDetail)   


class TestApiUrlsMaterial(SimpleTestCase):
    """
    Pada test ini, fokus untuk menguji route API (material) yang mengarah pada controller/views (material) tertentu
    """

    def testMaterial__apiUrlListResolves(self):
        url = reverse('as:api-material-list')
        self.assertEquals(resolve(url).func.view_class, viewsApi.MaterialList)   

    def testMaterial__apiUrlDetailResolves(self):
        url = reverse('as:api-material-detail',  kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, viewsApi.MaterialDetail)      
