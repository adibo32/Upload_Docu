from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm

def index(request):
    documents = Document.objects.all()
    form = DocumentForm()
    context = {'all_documents': documents, 'document_form':form}
    return render(request, "index.html", context)

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})
