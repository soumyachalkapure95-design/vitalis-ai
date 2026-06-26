from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm

@login_required
def appointment_list(request):
    if request.user.role == 'doctor':
        appointments = Appointment.objects.filter(doctor=request.user).order_by('-date')
    else:
        appointments = Appointment.objects.filter(patient=request.user).order_by('-date')
    return render(request, 'telemedicine/appointments.html', {'appointments': appointments})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('appointment_list')
    else:
        initial = {}
        doctor_id = request.GET.get('doctor_id')
        if doctor_id:
            initial['doctor'] = doctor_id
        form = AppointmentForm(initial=initial)
    return render(request, 'telemedicine/book.html', {'form': form})

@login_required
def manage_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    # Check permissions (only doctor can edit, or patient can cancel)
    if appointment.doctor != request.user and appointment.patient != request.user:
        return redirect('appointment_list')

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Appointment.STATUS_CHOICES):
            appointment.status = new_status
            appointment.save()
        return redirect('appointment_list')
        
    return render(request, 'telemedicine/manage.html', {'appointment': appointment})
