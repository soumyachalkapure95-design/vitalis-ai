from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MoodLog
from .forms import MoodLogForm

@login_required
def mental_health_home(request):
    if request.method == 'POST':
        form = MoodLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('mental_health_home')
    else:
        form = MoodLogForm()
        
    logs = MoodLog.objects.filter(user=request.user).order_by('-date')[:7]
    return render(request, 'mental_health/wellness.html', {
        'form': form,
        'logs': logs
    })
