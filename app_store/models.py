from django.db import models
from django.utils.text import slugify


# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=20,default='',unique=True)

    def __str__(self):
        return "[{}] Supplier {}".format(self.id,self.name)
        # return "Supplier {}".format(self.name)

#------------------------------------------------------------------------------------------
class Material(models.Model):
    TYPE_CHOICES = (
        ('FABRIC', 'Fabric'),
        ('JEANS', 'Jeans'),
        ('COTTON', 'Cotton'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,related_name='materials')

    code = models.CharField(max_length=10,default='')
    name = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=10,choices=TYPE_CHOICES, default='Cotton')
    buyPrice = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "[{}] Material {} | {}".format(self.id,self.name, self.supplier)
        # return "Material {} | {}".format(self.name, self.supplier)