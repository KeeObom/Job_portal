from django.shortcuts import render, redirect
from .forms import CVForm
# from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("CV Upload")

def cv_upload(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.save()
            return redirect('cv_list')
        else:
            form = CVForm()
        return render(request, 'cv_upload.html', {'form': form})

