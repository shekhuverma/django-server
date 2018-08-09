from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR=(os.path.split(BASE_DIR))[0] #/server


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html',{ 'documents': documents })


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html',{'form': form})
def temp(request):
    documents = Document.objects.all()
    #try:
    path=os.path.join(BASE_DIR+(Document.objects.all()[0]).document.url).replace("\\","/")
    os.remove(path)
    (Document.objects.all()[0]).delete()
    return render(request, 'core/home.html',{ 'documents': documents })
    #except IndexError:
     #   return render(request, 'core/home.html',{ 'documents': documents })
