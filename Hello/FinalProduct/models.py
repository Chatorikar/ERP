from django.db import models
from jsonfield import JSONField


# Create your models here.


class RawMaterial_Record(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    Component_Name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class RawMaterial(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    Material_type = models.CharField(max_length=50, default="")
    Primary_Stock_Unit = models.CharField(max_length=50, default="")  # char
    Unit_type = models.CharField(max_length=50, default="")
    quantity = models.IntegerField(blank=True)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Process(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    status = models.BooleanField(default=False)  # seq

    def __str__(self):
        return self.name


class Components(models.Model):
    id = models.AutoField(primary_key=True)
    Model_name = models.CharField(max_length=50, default="None")
    Part_name = models.CharField(max_length=50, default="Components-")
    Part_Number = models.IntegerField()
    Primary_Stock_Unit = models.IntegerField()  # char
    Purchase_Stock_Unit = models.IntegerField()  # char
    Material = models.CharField(max_length=50, default="")
    type_of_production = models.CharField(max_length=50, default="In House")
    cost = models.IntegerField()
    document = models.FileField(upload_to='documents/')
    process_list = models.ManyToManyField(Process)
    Rawmaterial_list = JSONField()
    Cheack_for_Allocation = models.BooleanField(default=False)  # seq
    Process_list = JSONField()
    Progress = models.IntegerField(default=0)

    def __str__(self):
        return self.Part_name

    # def __unicode__(self):
    #     return


class Finalproduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    component_list = models.ManyToManyField(Components)
    Progress = models.IntegerField(default=0)
    In_DataBase = models.BooleanField(default=True)

    # desciptions = models.TextField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, default="Customer-")
    email_id = models.CharField(max_length=60, default="customer@gmail.com")
    phone_no = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name
    # def __unicode__(self):
    #         return


class Purchase_Order(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="PO-")
    Final_Product_list = models.ManyToManyField(Finalproduct)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="members", null=True, blank=True)
    Progress = models.IntegerField(default=0)
    Approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
