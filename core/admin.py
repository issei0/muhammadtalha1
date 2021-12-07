from django.contrib import admin
from .models import Experience, Footer, Link, Main, Heading, Service, Project, Contact

# # Register your models here.
admin.site.register(Link),

admin.site.register(Main),

admin.site.register(Heading),

class ServiceAdminModel(admin.ModelAdmin):
    search_fields=('name',)
admin.site.register(Service, ServiceAdminModel),

class ProjectAdminModel(admin.ModelAdmin):
    search_fields=('name',)
admin.site.register(Project, ProjectAdminModel),

class ExperienceAdminModel(admin.ModelAdmin):
    search_fields=('name',)
admin.site.register(Experience, ExperienceAdminModel),

class ContactAdminModel(admin.ModelAdmin):
    search_fields=('name',)
admin.site.register(Contact, ContactAdminModel),

admin.site.register(Footer),