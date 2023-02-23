from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    bio = models.CharField(max_length=1000)
    age = models.PositiveBigIntegerField()
    def __str__(self):
        return str(self.name)

class CompanyDataTable(models.Model):
    company_name = models.CharField(max_length=1000)
    city = models.CharField(max_length=500)
    country = models.CharField(max_length=50)
    patent_no = models.CharField(max_length=20)
    kind = models.CharField(max_length=10)

class PatentDataTable(models.Model):
    patentnumber = models.CharField(max_length=20)
    applicant = models.CharField(max_length=500)
    country = models.CharField(max_length=5)
    filingdate = models.CharField(max_length=10)
    grantdate = models.CharField(max_length=10)
    patentlang = models.CharField(max_length=10)
    patenttitle = models.CharField(max_length=5000)
    patentxmllink = models.CharField(max_length=5000)
    cpc_class = models.CharField(max_length=2000)
    kind = models.CharField(max_length=10)
    application_date = models.CharField(max_length=10)
    inventors_name = models.CharField(max_length=5000)
    company_name = models.CharField(max_length=5000)

class InventorsDataTable(models.Model):
    peoples_name = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=20)
    patent_no = models.CharField(max_length=20)
    kind = models.CharField(max_length=10)