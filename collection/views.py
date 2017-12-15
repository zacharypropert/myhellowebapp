from django.shortcuts import render, redirect
from collection.forms import ProjectForm
from collection.models import Project

# Create your views here.
def index(request):
	#number = 9
	#thing = "Octopus"
	#projects = Project.objects.all().order_by('?') #returns all entries in a random order
	#Project.objects.filter(name__contains = 'Text') #returns incomplete matches where the text field is atleast in the name 
	#projects = Project.objects.filter(name = 'text') #retrieve more than one result that match the criteria
	#correct_project = Project.objects.get(name = 'Exact Name')#when you want to grab one specific object

	projects = Project.objects.all().order_by('name') #retrieves all entries in database and orders them by name
	return render(request, 'index.html', {
		#'number': number,
		#'thing': thing,
		'projects': projects,
	})


def project_detail(request, slug):
	#grab the object 
	project = Project.objects.get(slug=slug)
	#pass to template
	return render(request, 'projects/project_detail.html', {
		'project' : project,
	})


def edit_project(request, slug):
	#grab the object
	project = Project.objects.get(slug=slug)
	#set the form we are using
	form_class = ProjectForm
	
	#if we're coming to this view from a submitted form,
	if request.method == 'POST':
		#grab the data from the submitted form
		form = form_class(data=request.POST, instance=project)
		if form.is_valid():
			#save new data
			form.save()
			return redirect('project_detail', slug=project.slug)
	#otherwise create the form
	else:
		form = form_class(instance=project)
	#render the template
	return render(request, 'projects/edit_project.html', {
		'project' : project,
		'form' : form,
	})
