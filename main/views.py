# main/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

def home(request):
    """
    Home page view - serves home.html template
    """
    return render(request, 'home.html')

def index(request):
    """
    Index page view - serves index.html template
    """
    return render(request, 'index.html')

@csrf_exempt
@require_POST
def contact_api(request):
    """
    Disabled contact form API endpoint
    """
    return JsonResponse({'status': 'disabled', 'message': 'Contact form is currently disabled'})

@csrf_exempt
@require_POST
def update_settings(request):
    """
    Disabled settings update API endpoint
    """
    return JsonResponse({'status': 'disabled', 'message': 'Settings update is currently disabled'})