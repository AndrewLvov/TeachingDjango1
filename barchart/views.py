from django.shortcuts import render


def index(request):
	ctx = {
		'numbers': [5, 4, 2, -5, 6],
		'message': "Hello, guys!"
	}
	return render(request, 'index.html', ctx)