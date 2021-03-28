from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings

#--------------models
from .models import Supplier as ModelSupplier

#--------------forms
from .forms_supplier import FormSupplier

#--------------views

#---------------------------------------------------------------------extra_context
EC_supplier_listView = {
        'page_judul': 'Tabel Supplier',
        'page_deskripsi': 'untuk mengelola data Supplier',
        'page_role': 'Supplier',
    }

EC_supplier_createView= {
        'page_judul': 'Tambah Supplier',
        'page_deskripsi': 'untuk menambah data Supplier',
        'page_role': 'Supplier',
        'role': 'create',
    }

EC_supplier_updateView = {
        'page_judul': 'Edit Supplier',
        'page_deskripsi': 'untuk memperbarui data Supplier',
        'page_role': 'Supplier',
        'role': 'update',
    }

EC_supplier_detailView ={
        'page_judul': 'Detail Supplier',
        'page_deskripsi': 'untuk melihat detail data Supplier',
        'page_role': 'Supplier',
    }
#----------------------------------------------------------------------------------------------Class view
#---------------------------------------------------------------------Read (list)
class SupplierListView(ListView):
    model = ModelSupplier
    ordering = ['id']
    template_name = "app_store/supplier/index.html"
    context_object_name = 'suppliers'
    extra_context = EC_supplier_listView

    # def get_queryset(self):
        # queryset = self.model.objects.exclude(username=settings.USERNAME_DEVELOPER)
        # return queryset

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(SupplierListView, self).get_context_data(
            *args, **kwargs)

        return context
#-----------------------------------------------------------------------------------{{user}}
#---------------------------------------------------------------------Create
class SupplierCreateView(SuccessMessageMixin, CreateView):
    form_class = FormSupplier
    template_name = "app_store/supplier/create.html"
    success_url = reverse_lazy('as:supplier-index')
    context_object_name = 'forms'
    extra_context = EC_supplier_createView

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(SupplierCreateView, self).get_context_data(
            *args, **kwargs)

        return context

    def get_success_message(self, cleaned_data):
        return 'Data Supplier berhasil ditambahkan'

#---------------------------------------------------------------------Update
class SupplierUpdateView(SuccessMessageMixin, UpdateView):
    model = ModelSupplier
    form_class = FormSupplier
    template_name = "app_store/supplier/create.html"
    context_object_name = 'supplier'
    success_url = reverse_lazy('as:supplier-index')
    extra_context = EC_supplier_updateView
    
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(SupplierUpdateView, self).get_context_data(
            *args, **kwargs)

        return context

    def get_success_message(self, cleaned_data):
        return 'Data Supplier berhasil diperbarui'

#---------------------------------------------------------------------Delete
class SupplierDeleteView(DeleteView):
    model = ModelSupplier
    # template_name = "app_store/supplier/create.html"
    success_url = reverse_lazy('as:supplier-index')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        self.object.delete()
        return HttpResponseRedirect(success_url)

#---------------------------------------------------------------------Detail
class SupplierDetailView(DetailView):
    model = ModelSupplier
    template_name = "app_store/supplier/detail.html"
    context_object_name = 'supplier'
    extra_context = EC_supplier_detailView

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(SupplierDetailView, self).get_context_data(
            *args, **kwargs)

        return context


