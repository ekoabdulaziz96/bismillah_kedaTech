from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings

#--------------models
from .models import Material as ModelMaterial

#--------------forms
from .forms_material import FormMaterial

#--------------views

#---------------------------------------------------------------------extra_context
EC_material_listView = {
        'page_judul': 'Tabel Material',
        'page_deskripsi': 'untuk mengelola data Material',
        'page_role': 'Material',
    }

EC_material_createView= {
        'page_judul': 'Tambah Material',
        'page_deskripsi': 'untuk menambah data Material',
        'page_role': 'Material',
        'role': 'create',
    }

EC_material_updateView = {
        'page_judul': 'Edit Material',
        'page_deskripsi': 'untuk memperbarui data Material',
        'page_role': 'Material',
        'role': 'update',
    }

EC_material_detailView ={
        'page_judul': 'Detail Material',
        'page_deskripsi': 'untuk melihat detail data Material',
        'page_role': 'Material',
    }
#----------------------------------------------------------------------------------------------Class view
#---------------------------------------------------------------------Read (list)
class MaterialListView(ListView):
    model = ModelMaterial
    ordering = ['id']
    template_name = "app_store/material/index.html"
    context_object_name = 'materials'
    extra_context = EC_material_listView

    # def get_queryset(self):
        # queryset = self.model.objects.exclude(username=settings.USERNAME_DEVELOPER)
        # return queryset

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(MaterialListView, self).get_context_data(
            *args, **kwargs)
        context['typeChoices'] = ModelMaterial.TYPE_CHOICES
        return context
#-----------------------------------------------------------------------------------{{user}}
#---------------------------------------------------------------------Create
class MaterialCreateView(SuccessMessageMixin, CreateView):
    form_class = FormMaterial
    template_name = "app_store/material/create.html"
    success_url = reverse_lazy('as:material-index')
    context_object_name = 'forms'
    extra_context = EC_material_createView

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(MaterialCreateView, self).get_context_data(
            *args, **kwargs)

        return context

    def get_success_message(self, cleaned_data):
        return 'Data Material berhasil ditambahkan'

#---------------------------------------------------------------------Update
class MaterialUpdateView(SuccessMessageMixin, UpdateView):
    model = ModelMaterial
    form_class = FormMaterial
    template_name = "app_store/material/create.html"
    context_object_name = 'material'
    success_url = reverse_lazy('as:material-index')
    extra_context = EC_material_updateView
    
    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(MaterialUpdateView, self).get_context_data(
            *args, **kwargs)

        return context

    def get_success_message(self, cleaned_data):
        return 'Data Material berhasil diperbarui'

#---------------------------------------------------------------------Delete
class MaterialDeleteView(DeleteView):
    model = ModelMaterial
    # template_name = "app_store/material/create.html"
    success_url = reverse_lazy('as:material-index')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        self.object.delete()
        return HttpResponseRedirect(success_url)

#---------------------------------------------------------------------Detail
class MaterialDetailView(DetailView):
    model = ModelMaterial
    template_name = "app_store/material/detail.html"
    context_object_name = 'material'
    extra_context = EC_material_detailView

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        context = super(MaterialDetailView, self).get_context_data(
            *args, **kwargs)

        return context


