from django.db import models

# Create your models here.
class About(models.Model):
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="about/")

    class Meta:
        verbose_name = 'About me'
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"

class Service(models.Model):
    name = models.CharField(max_length=1000,verbose_name="Service name",blank=True)
    description = models.TextField(blank=True, null=True,verbose_name="About service")

    def __str__(self):
        return self.name

class RecentWork(models.Model):
    title = models.CharField(max_length=1000,verbose_name="Work title",blank=True)
    image = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=1000,verbose_name="Client name",blank=True)
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients/")

    def __str__(self):
        return self.name


class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to="about/")
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title