from django.contrib import admin

from .models import Supplier as SupplierModel, Material as MaterialModel
# Register your models here.

admin.site.register([SupplierModel,MaterialModel])