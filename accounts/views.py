from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = "Invalid username or password"
    return render(request, 'accounts/login.html', {'error': error})

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    records = []
    appointments = []
    moods = []
    predictions = []
    
    try:
        from records.models import HealthRecord
        records = HealthRecord.objects.filter(user=request.user).order_by('-created_at')[:5]
    except Exception:
        pass
        
    try:
        from telemedicine.models import Appointment
        if request.user.role == 'doctor':
            appointments = Appointment.objects.filter(doctor=request.user).order_by('-date')[:5]
        else:
            appointments = Appointment.objects.filter(patient=request.user).order_by('-date')[:5]
    except Exception:
        pass
        
    try:
        from mental_health.models import MoodLog
        moods = MoodLog.objects.filter(user=request.user).order_by('-date')[:5]
    except Exception:
        pass
        
    try:
        from disease_tracker.models import DiseasePrediction
        predictions = DiseasePrediction.objects.filter(user=request.user).order_by('-created_at')[:5]
    except Exception:
        pass

    context = {
        'records': records,
        'appointments': appointments,
        'moods': moods,
        'predictions': predictions,
    }
    return render(request, 'accounts/dashboard.html', context)