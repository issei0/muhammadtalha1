from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)

class Main(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    text1 = models.CharField(max_length=200, blank=True, null=True)
    text2 = models.CharField(max_length=200, blank=True, null=True)
    text3 = models.CharField(max_length=200, blank=True, null=True)
    text4 = models.CharField(max_length=200, blank=True, null=True)
    homeimage = models.ImageField(blank=True, null=True)
    image1 = models.ImageField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    button1 = models.CharField(max_length=200, blank=True, null=True)
    link1 = models.URLField(max_length=200, blank=True, null=True)
    button2 = models.CharField(max_length=200, blank=True, null=True)
    link2 = models.URLField(max_length=200, blank=True, null=True)
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
    def __str__(self):
        return str(self.name)
    
class Heading(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    text1 = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    desc1 = models.TextField(blank=True, null=True)
    desc2 = models.TextField(blank=True, null=True) 
    button1 = models.CharField(max_length=200, blank=True, null=True)
    link1 = models.URLField(max_length=200, blank=True, null=True)
    button2 = models.CharField(max_length=200, blank=True, null=True)
    link2 = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    
class Service(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    
class Experience(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    button = models.CharField(max_length=200, blank=True, null=True)
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
    def __str__(self):
        return str(self.name)
    
class Project(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    

    def __str__(self):
        return str(self.email_address) + " by " + f'{self.first_name}' + f'{self.last_name}'
    
class Footer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    paragraph = models.TextField(blank=True, null=True)
    copyright = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)