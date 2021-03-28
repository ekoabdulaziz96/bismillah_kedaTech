from django.test import TestCase, Client
from django.urls import reverse
import json
from django.db.models.query import QuerySet
from django.http import request

from rest_framework.test import APIRequestFactory


from app_store import models
from app_store.api import serializers, views
# import pdb; pdb.set_trace() 

class TestApiViewsSupplier(TestCase):
    def setUp(self):
        #instance object client
        self.client = Client()
        self.factory = APIRequestFactory()

        #list url/roure path
        self.urlListCreate = reverse('as:api-supplier-list')
        self.urlRetrieveUpdateDestroy = reverse('as:api-supplier-detail', kwargs={'pk':1})

        self.data= {
            'name' : 'supplier1',
        }
        self.dataUpdate= {
            'name' : 'supplier1_update',
        }

    def testSupplier__apiViewsListCreate(self):
        #----------------------------------------------------
        #----------------------------------------------------POST (CREATE)
        response = self.client.post(self.urlListCreate,self.data)

        # --cek response status code response
        self.assertEquals(response.status_code, 201)

        # --cek response content-type 'application/json'
        self.assertEqual(response['content-type'], 'application/json')

        # --cek response data dan data asli
        self.assertEquals(response.data['name'], self.data['name']) #supplier1

        #--cek apakah object berhasil tersimpan di DB
        objectCreated = models.Supplier.objects.get(pk=1)
        self.assertEquals(objectCreated.name, self.data['name']) #supplier1

        #----------------------------------------------------
        #----------------------------------------------------GET (LIST)
        response = self.client.get(self.urlListCreate)
        # import pdb; pdb.set_trace() 

        #--cek response status code response
        self.assertEquals(response.status_code, 200)

        # --cek response content-type 'application/json'
        self.assertEqual(response['content-type'], 'application/json')

        #--cek jumlah data (DB) supplier yg return
        objectSupplierCount = models.Supplier.objects.all().count()
        self.assertEquals(len(response.data), objectSupplierCount) #1
       

    def testSupplier_apiViewRetrieveUpdateDestroy(self):
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
        self.assertEquals(response.data['name'], self.data['name']) #supplier1

        #--cek response object yg berhasil di get
        objectCreated = models.Supplier.objects.get(pk=1)
        self.assertEquals(objectCreated.name, self.data['name']) #supplier1
        #----------------------------------------------------
        #----------------------------------------------------Update
        response = self.client.put(self.urlRetrieveUpdateDestroy,self.dataUpdate,content_type='application/json')

        # --cek response status code response
        self.assertEquals(response.status_code, 200)

        # --cek response content-type 'application/json'
        self.assertEqual(response['content-type'], 'application/json')

        # --cek response data dan data asli setelah update
        self.assertEquals(response.data['name'], self.dataUpdate['name']) #supplier1_update

        #--cek apakah object berhasil tersimpan di DB
        objectCreated = models.Supplier.objects.get(pk=1)
        self.assertEquals(objectCreated.name, self.dataUpdate['name']) #supplier1_update
        #----------------------------------------------------
        #----------------------------------------------------delete
        response = self.client.delete(self.urlRetrieveUpdateDestroy)

        # --cek response status code response
        self.assertEquals(response.status_code, 204)

        #--cek apakah object berhasil dihapus
        objectSupplierCount = models.Supplier.objects.all().count()
        self.assertEquals(objectSupplierCount, 0) # sama dengan nol
