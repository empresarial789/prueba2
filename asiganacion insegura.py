# views.py (Vulnerable)
from django.shortcuts import render
from .models import UserProfile

def create_user(request):
    UserProfile.objects.create(**request.POST.dict())  # ¡Asignación masiva!
    return render(request, 'success.html')