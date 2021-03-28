from django.urls import path, include
from . import views_supplier, views_material

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .api import views as viewsApi

app_name = 'app_store'

#---------ROUTE WEb
urlpatternsWeb = [
    #------------------------------------------------------------Supplier
    path('supplier/delete/<int:pk>', views_supplier.SupplierDeleteView.as_view(), name='supplier-delete'),
    path('supplier/update/<int:pk>', views_supplier.SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier/create/', views_supplier.SupplierCreateView.as_view(),name='supplier-create'),
    path('supplier/', views_supplier.SupplierListView.as_view(), name='supplier-index'),
    #------------------------------------------------------------Material
    path('material/detail/<int:pk>', views_material.MaterialDetailView.as_view(), name='material-detail'),
    path('material/delete/<int:pk>', views_material.MaterialDeleteView.as_view(), name='material-delete'),
    path('material/update/<int:pk>', views_material.MaterialUpdateView.as_view(), name='material-update'),
    path('material/create/', views_material.MaterialCreateView.as_view(),name='material-create'),
    path('material/', views_material.MaterialListView.as_view(), name='material-index'),
]



@api_view(['GET'])
def api_store(request, format=None):
    return Response({
        'suppliers': reverse('as:api-supplier-list', request=request, format=format),
        'materials': reverse('as:api-material-list', request=request, format=format),
    })

#---------ROUTE API
urlpatternsApi = [
    # path('', views.index),
    path('api/', api_store,name='api-root'),
    # ----------------------------------------------------------------supplier
    path('api/supplier', viewsApi.SupplierList.as_view(), name='api-supplier-list'),
    path('api/supplier/<int:pk>/', viewsApi.SupplierDetail.as_view(),  name='api-supplier-detail'),
    # ----------------------------------------------------------------material
    path('api/material/', viewsApi.MaterialList.as_view(), name='api-material-list'),
    path('api/material/<int:pk>/', viewsApi.MaterialDetail.as_view(),  name='api-material-detail'),
]

urlpatterns = urlpatternsWeb + urlpatternsApi
