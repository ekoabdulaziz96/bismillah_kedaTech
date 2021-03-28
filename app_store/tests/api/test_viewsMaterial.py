from django.test import TestCase, Client
from django.urls import reverse
import json
from django.db.models.query import QuerySet
from django.http import request


from app_store import models
from app_store.api import serializers, views
# import pdb; pdb.set_trace() 

class TestApiViewsMaterial(TestCase):
    def setUp(self):
        #instance object client
        self.client = Client()

        #list url/roure path
        self.urlListCreate = reverse('as:api-material-list')
        self.urlRetrieveUpdateDestroy = reverse('as:api-material-detail', kwargs={'pk':1})

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

    def testMaterial__apiViewsListCreate(self):
        #----------------------------------------------------
        #----------------------------------------------------POST (CREATE)
        response = self.client.post(self.urlListCreate,self.data)

        # --cek response status code response
        self.assertEquals(response.status_code, 201)

        # --cek response content-type 'application/json'
        self.assertEqual(response['content-type'], 'application/json')

        # --cek response data dan data asli
        self.assertEquals(response.data['code'], self.data['code'])  #code1

        #--cek apakah object berhasil tersimpan di DB
        objectCreated = models.Material.objects.get(pk=1)
        self.assertEquals(objectCreated.code, self.data['code']) #code1

        #----------------------------------------------------
        #----------------------------------------------------GET (LIST)
        response = self.client.get(self.urlListCreate)
        # import pdb; pdb.set_trace() 

        #--cek response status code response
        self.assertEquals(response.status_code, 200)

        # --cek response content-type 'application/json'
        self.assertEqual(response['content-type'], 'application/json')

        #--cek jumlah data (DB) material yg return
        objectMaterialCount = models.Material.objects.all().count()
        self.assertEquals(len(response.data), objectMaterialCount) #1
       

    def testMaterial_apiViewRetrieveUpdateDestroy(self):
        # init 
        response = self.client.post(self.urlListCreate,self.data)

        #----------------------------------------------------
        #----------------------------------------------------GET/ retrieve
        response = self.client.get(self.urlRetrieveUpdateDestroy)
        # --cek response status code response
        self.assertEquals(response.status_code, 200)

        # --cek response content-type 'application/json'
        self.assertEqual(response['content-type'], 'application/json')

        # --cek response data dan data asli
        self.assertEquals(response.data['code'], self.data['code']) #code1

        #--cek response object yg berhasil di get
        objectCreated = models.Material.objects.get(pk=1)
        self.assertEquals(objectCreated.code, self.data['code']) #code1
        #----------------------------------------------------
        #----------------------------------------------------Update
        response = self.client.put(self.urlRetrieveUpdateDestroy,self.dataUpdate,content_type='application/json')

        # --cek response status code response
        self.assertEquals(response.status_code, 200)

        # --cek response content-type 'application/json'
        self.assertEqual(response['content-type'], 'application/json')

        # --cek response data dan data asli setelah update
        self.assertEquals(response.data['code'], self.dataUpdate['code']) #code123

        #--cek apakah object berhasil tersimpan di DB
        objectCreated = models.Material.objects.get(pk=1)
        self.assertEquals(objectCreated.code, self.dataUpdate['code']) #code123
        #----------------------------------------------------
        #----------------------------------------------------delete
        response = self.client.delete(self.urlRetrieveUpdateDestroy)

        # --cek response status code response
        self.assertEquals(response.status_code, 204)

        #--cek apakah object berhasil dihapus
        objectMaterialCount = models.Material.objects.all().count()
        self.assertEquals(objectMaterialCount, 0) # sama dengan nol
