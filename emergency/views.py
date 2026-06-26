from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import EmergencyAlert
import json

def emergency_home(request):
    # Show active alarms for Doctors/Admins
    alerts = []
    if request.user.is_authenticated and (request.user.role == 'doctor' or request.user.is_staff):
        alerts = EmergencyAlert.objects.filter(status='Active').order_by('-created_at')
    return render(request, 'emergency/help.html', {'alerts': alerts})

def trigger_sos(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except Exception:
            data = request.POST
            
        lat = data.get('latitude')
        lng = data.get('longitude')
        desc = data.get('description', 'SOS alarm triggered via client portal.')
        
        # Convert values
        try:
            lat = float(lat) if lat else None
            lng = float(lng) if lng else None
        except (ValueError, TypeError):
            lat = None
            lng = None
            
        user = request.user if request.user.is_authenticated else None
        
        alert = EmergencyAlert.objects.create(
            user=user,
            latitude=lat,
            longitude=lng,
            description=desc
        )
        
        return JsonResponse({
            'status': 'success',
            'alert_id': alert.id,
            'message': 'SOS logged successfully. Emergency crews alerted.'
        })
        
    return JsonResponse({'status': 'error', 'message': 'Invalid HTTP request.'}, status=400)
