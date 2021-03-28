from django.test import TestCase, Client
from django.urls import reverse
from app_store import views_material, models,forms_material
import json
from django.db.models.query import QuerySet

#terdapat error librabry post data saat create/add data material baru. 
#perlu eksplorasi lebih dalam, karena menggunak generic views
#tapi, testing pada web -> normal
#----> solusi debug
# import pdb; pdb.set_trace() --> (dump)
# responsePost.context['form']['supplier'].errors --> (powershell)
# !!!!!!!!!!!!!important foreign key/relation model di tingkat post client data berupa ID 

class TestViewsMaterial(TestCase):
    def setUp(self):
        #instance object client
        self.client = Client()

        #list url/roure path
        self.urlList = reverse('as:material-index')
        self.urlCreate = reverse('as:material-create')
        self.urlUpdate = reverse('as:material-update', kwargs={'pk':1})
        self.urlDelete = reverse('as:material-delete', kwargs={'pk':1})
        self.urlDetail = reverse('as:material-detail', kwargs={'pk':1})

        self.supplier1 = models.Supplier.objects.create(name = 'supplier1')
        self.data= {
            'supplier' : self.supplier1.id,
            'code' :  'code1',
            'name' :  'name1',
            'type' :   models.Material.TYPE_CHOICES[0][0],
            'buyPrice' :  '10000'
        }
        self.dataUpdate= {
            'supplier' : self.supplier1.id,
            'code' :   'code123', #update data maks 10 char
            'name' :   'name1',
            'type' :   models.Material.TYPE_CHOICES[0][0],
            'buyPrice' :   '10000',
        }

    def testMaterial_viewsList(self):
        response = self.client.get(self.urlList)

        #--cek response status code response
        self.assertEquals(response.status_code, 200)
       
        #--cek response template (.html) yg digunakan
        self.assertTemplateUsed(response, views_material.MaterialListView.template_name)
       
        #--cek context (list of queryset data) yg oper ke template (.html) adalah queryset
        contextQueryset = response.context_data[views_material.MaterialListView.context_object_name]
        self.assertIsInstance(contextQueryset, QuerySet)
        
        #--cek value context (static data) yg dioper ke template berhasil
        key = list(views_material.EC_material_listView.keys())[-1]  # key : page_role, value:material
        contextStatic = response.context_data[key]
        self.assertEqual(response.context_data[key], contextStatic)

    def testMaterial_viewsCreate(self):
        #----------------------------------------------------GET
        response = self.client.get(self.urlCreate)
        #--cek response status code response
        self.assertEquals(response.status_code, 200)
       
        #--cek response template (.html) yg digunakan
        self.assertTemplateUsed(response, views_material.MaterialCreateView.template_name)
       
        #--cek value context (static data) yg dioper ke template berhasil
        key = list(views_material.EC_material_createView.keys())[-1]  # key : role, value:create
        contextStatic = response.context_data[key]
        self.assertEqual(response.context_data[key], contextStatic)

        #----------------------------------------------------POST
        response = self.client.post(self.urlCreate,self.data)

        #--cek response status code response
        self.assertEquals(response.status_code, 302)

        #--cek response redirect success url 
        self.assertRedirects(response, views_material.MaterialCreateView.success_url)

        #--cek response object yg berhasil di post (created)
        objectCreated = models.Material.objects.get(pk=1)
        self.assertEquals(objectCreated.code, self.data['code'])

    def testMaterial_viewsUpdate(self):
        #init
        self.client.post(self.urlCreate,self.data)

        #----------------------------------------------------GET
        response = self.client.get(self.urlUpdate)

        #--cek response status code response
        self.assertEquals(response.status_code, 200)
       
        #--cek response template (.html) yg digunakan
        self.assertTemplateUsed(response, views_material.MaterialUpdateView.template_name)
       
        #--cek context (queryset data) yg oper ke template (.html) adalah queryset
        contextQueryset = response.context_data[views_material.MaterialUpdateView.context_object_name]
        self.assertIsInstance(contextQueryset, models.Material)
        
        #--cek value context (static data) yg dioper ke template berhasil
        key = list(views_material.EC_material_listView.keys())[-1]  # key : role, value:update
        contextStatic = response.context_data[key]
        self.assertEqual(response.context_data[key], contextStatic)

        # #----------------------------------------------------POST
        response = self.client.post(self.urlUpdate,self.dataUpdate)
        # import pdb; pdb.set_trace()

        # --cek response status code response
        self.assertEquals(response.status_code, 302)

        #--cek response redirect success url 
        self.assertRedirects(response, views_material.MaterialCreateView.success_url)

        #--cek response object yg berhasil di post (updated)
        objectCreated = models.Material.objects.get(pk=1)
        self.assertEquals(objectCreated.code, self.dataUpdate['code'])

    def testMaterial_viewsDelete(self):
        #init
        self.client.post(self.urlCreate,self.data)

        #----------------------------------------------------POST
        response = self.client.delete(self.urlDelete)

        #--cek response status code response
        self.assertEquals(response.status_code, 302)

        #--cek response redirect success url 
        self.assertRedirects(response, views_material.MaterialUpdateView.success_url)

        #--jumlah data material seharusnya 0, setelah proses hapus/delete berhasil
        # objectCreated = models.Material.objects.get(pk=1)
        self.assertEquals(models.Material.objects.all().count(), 0)

    def testMaterial_viewsDetail(self):
        #init
        self.client.post(self.urlCreate,self.data)

        #----------------------------------------------------GET
        response = self.client.get(self.urlDetail)

        #--cek response status code response
        self.assertEquals(response.status_code, 200)
       
        #--cek response template (.html) yg digunakan
        self.assertTemplateUsed(response, views_material.MaterialDetailView.template_name)
       
        #--cek context (queryset data) yg oper ke template (.html) adalah queryset
        contextQueryset = response.context_data[views_material.MaterialDetailView.context_object_name]
        self.assertIsInstance(contextQueryset, models.Material)
        
        #--cek value context (static data) yg dioper ke template berhasil
        key = list(views_material.EC_material_listView.keys())[-1]  # key : role, value:detail
        contextStatic = response.context_data[key]
        self.assertEqual(response.context_data[key], contextStatic)

