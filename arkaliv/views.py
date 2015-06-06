from django.shortcuts import render

# Create your views here.

def files_list(request):
	return render(request, 'files/files_list.html')