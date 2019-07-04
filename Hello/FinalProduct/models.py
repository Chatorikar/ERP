from django.db import models

# Create your models here.
class Process(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Components(models.Model):
    id = models.AutoField(primary_key=True)
    Model_name = models.CharField(max_length=50, default="")
    Part_name = models.CharField(max_length=50, default="")   
    Part_Number = models.IntegerField()
    Primary_Stock_Unit = models.IntegerField()#char
    Purchase_Stock_Unit = models.IntegerField()#char
    Material = models.CharField(max_length=50, default="")
    type_of_production = models.CharField(max_length=50, default="")
    cost = models.IntegerField()
    document = models.FileField(upload_to='documents/')
    process_list = models.ManyToManyField(Process)

    def __str__(self):
        return self.Model_name 

    # def __unicode__(self):
    #     return 

class Finalproduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    component_list = models.ManyToManyField(Components)
    # desciptions = models.TextField()

    def __str__(self):
        return self.name

    # def __unicode__(self):
    #     return 