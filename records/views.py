from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HealthRecord
from .forms import HealthRecordForm

@login_required
def records_list(request):
    # Patients view their own, doctors can search all (if doctor role is implemented)
    if request.user.role == 'doctor':
        # Simple doctor view: show all records for supervision
        records = HealthRecord.objects.all().order_by('-created_at')
    else:
        records = HealthRecord.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'records/list.html', {'records': records})

@login_required
def add_record(request):
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect('records_list')
    else:
        form = HealthRecordForm()
    return render(request, 'records/form.html', {'form': form, 'title': 'Create Health Record'})

@login_required
def edit_record(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk)
    # Check permissions
    if record.user != request.user and request.user.role != 'doctor':
        return redirect('records_list')
        
    if request.method == 'POST':
        form = HealthRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('records_list')
    else:
        form = HealthRecordForm(instance=record)
    return render(request, 'records/form.html', {'form': form, 'title': 'Update Health Record'})

@login_required
def delete_record(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk)
    if record.user == request.user or request.user.role == 'doctor':
        record.delete()
    return redirect('records_list')
