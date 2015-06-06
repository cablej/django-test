from django.shortcuts import render
from django.utils import timezone
from .models import File

# Create your views here.

def files_list(request):
	files = File.objects.filter(published_date__lt=timezone.now()).order_by('published_date')
	return render(request, 'files/files_list.html', {'files': files})