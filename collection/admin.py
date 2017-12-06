from django.contrib import admin

#Import our model
from collection.models import Project

# Register your models here.
#admin.site.register(Project)

class ProjectAdmin(admin.ModelAdmin):
	model = Project
	list_display = ('name', 'description',)
	prepopulated_fields = { 'slug': ('name',)}


admin.site.register(Project, ProjectAdmin)
