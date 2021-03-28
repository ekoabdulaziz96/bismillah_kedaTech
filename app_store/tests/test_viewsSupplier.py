from django.test import TestCase, Client
from django.urls import reverse
from app_store import views_supplier, models
import json
from django.db.models.query import QuerySet

class TestViewsSupplier(TestCase):
    def setUp(self):
        #instance object client
        self.client = Client()

        #list url/roure path
        self.urlList = reverse('as:supplier-index')
        self.urlCreate = reverse('as:supplier-create')
        self.urlUpdate = reverse('as:supplier-update', kwargs={'pk':1})
        self.urlDelete = reverse('as:supplier-delete', kwargs={'pk':1})

        self.data= {
            'name' : 'supplier1',
        }
        self.dataUpdate= {
            'name' : 'supplier1_update',
        }

    def testSupplier_viewsList(self):
        response = self.client.get(self.urlList)

        #--cek response status code response
        self.assertEquals(response.status_code, 200)
       
        #--cek response template (.html) yg digunakan
        self.assertTemplateUsed(response, views_supplier.SupplierListView.template_name)
       
        #--cek context (list of queryset data) yg oper ke template (.html) adalah queryset
        contextQueryset = response.context_data[views_supplier.SupplierListView.context_object_name]
        self.assertIsInstance(contextQueryset, QuerySet)
        
        #--cek value context (static data) yg dioper ke template berhasil
        key = list(views_supplier.EC_supplier_listView.keys())[-1]  # key : page_role, value:supplier
        contextStatic = response.context_data[key]
        self.assertEqual(response.context_data[key], contextStatic)

    def testSupplier_viewsCreate(self):
        #----------------------------------------------------GET
        response = self.client.get(self.urlCreate)

        #--cek response status code response
        self.assertEquals(response.status_code, 200)
       
        #--cek response template (.html) yg digunakan
        self.assertTemplateUsed(response, views_supplier.SupplierCreateView.template_name)
       
        #--cek value context (static data) yg dioper ke template berhasil
        key = list(views_supplier.EC_supplier_createView.keys())[-1]  # key : role, value:create
        contextStatic = response.context_data[key]
        self.assertEqual(response.context_data[key], contextStatic)

        #----------------------------------------------------POST
        response = self.client.post(self.urlCreate,self.data)

        #--cek response status code response
        self.assertEquals(response.status_code, 302)

        #--cek response redirect success url 
        self.assertRedirects(response, views_supplier.SupplierCreateView.success_url)

        #--cek response object yg berhasil di post (created)
        objectCreated = models.Supplier.objects.get(pk=1)
        self.assertEquals(objectCreated.name, self.data['name'])

    def testSupplier_viewsUpdate(self):
        #init
        self.client.post(self.urlCreate,self.data)
        #----------------------------------------------------GET
        response = self.client.get(self.urlUpdate)

        #--cek response status code response
        self.assertEquals(response.status_code, 200)
       
        #--cek response template (.html) yg digunakan
        self.assertTemplateUsed(response, views_supplier.SupplierUpdateView.template_name)
       
        #--cek context (queryset data) yg oper ke template (.html) adalah queryset
        contextQueryset = response.context_data[views_supplier.SupplierUpdateView.context_object_name]
        self.assertIsInstance(contextQueryset, models.Supplier)
        
        #--cek value context (static data) yg dioper ke template berhasil
        key = list(views_supplier.EC_supplier_updateView.keys())[-1]  # key : role, value:update
        contextStatic = response.context_data[key]
        self.assertEqual(response.context_data[key], contextStatic)

        #----------------------------------------------------POST
        response = self.client.post(self.urlUpdate,self.dataUpdate)

        #--cek response status code response
        self.assertEquals(response.status_code, 302)

        #--cek response redirect success url 
        self.assertRedirects(response, views_supplier.SupplierCreateView.success_url)

        #--cek response object yg berhasil di post (updated)
        objectCreated = models.Supplier.objects.get(pk=1)
        self.assertEquals(objectCreated.name, self.dataUpdate['name'])

    def testSupplier_viewsDelete(self):
        #init
        self.client.post(self.urlCreate,self.data)

        #----------------------------------------------------POST
        response = self.client.delete(self.urlDelete)

        #--cek response status code response
        self.assertEquals(response.status_code, 302)

        #--cek response redirect success url 
        self.assertRedirects(response, views_supplier.SupplierUpdateView.success_url)

        #--jumlah data supplier seharusnya 0, setelah proses hapus/delete berhasil
        self.assertEquals(models.Supplier.objects.all().count(), 0)


       

