from django.shortcuts import render

# Create your views here.
def index(request):
	number = 9
	thing = "Octopus" 
	return render(request, 'index.html', {
		'number': number,
		'thing': thing,
	})
