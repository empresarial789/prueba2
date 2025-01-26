# views.py (Vulnerable)
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)  # ¡Sin validar tipo o tamaño!
    return HttpResponse("Archivo subido.")