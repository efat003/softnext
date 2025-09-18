from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')   # removed SiteSetting dependency

@csrf_exempt
@require_POST
def contact_api(request):
    return JsonResponse({'status': 'disabled'})   # disabled contact form

@csrf_exempt
@require_POST
def update_settings(request):
    return JsonResponse({'status': 'disabled'})   # disabled settings update
