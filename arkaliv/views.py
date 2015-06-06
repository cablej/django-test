from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import File
from .forms import PostForm

# Create your views here.

def files_list(request):
	files = File.objects.filter(published_date__lt=timezone.now()).order_by('published_date')
	return render(request, 'files/files_list.html', {'files': files})

def file_detail(request, pk):
	file = get_object_or_404(File, pk=pk)
	return render(request, 'files/file_detail.html', {'file': file})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('arkaliv.views.file_detail', pk=post.pk)
	else: 
		form = PostForm()
	return render(request, 'files/post_edit.html', {'form': form})

def file_edit(request, pk):
    file = get_object_or_404(File, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=file)
        if form.is_valid():
            file = form.save(commit=False)
            file.author = request.user
            file.published_date = timezone.now()
            file.save()
            return redirect('arkaliv.views.file_detail', pk=file.pk)
    else:
        form = PostForm(instance=file)
    return render(request, 'files/post_edit.html', {'form': form})



