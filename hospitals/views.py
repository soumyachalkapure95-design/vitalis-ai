from django.shortcuts import render
from django.db.models import Q
from .models import Hospital, Doctor
from accounts.models import CustomUser

def hospital_list(request):
    # Auto-populate mock hospitals and doctors if dataset is empty or old
    if not Hospital.objects.filter(name="Sri Sai Krupa Hospital").exists():
        Hospital.objects.all().delete()
        
        # 1. Sri Sai Krupa Hospital
        h1 = Hospital.objects.create(
            name="Sri Sai Krupa Hospital",
            address="Main Road, Kalaburagi",
            city="Kalaburagi",
            phone="08472-123456",
            specialties="General, Orthopedics, Cardiology, Emergency",
            beds_available=15,
            rating=4.5
        )
        for d_data in [
            {"name": "Dr. Rajesh Kumar", "spec": "General Surgery", "qual": "MBBS, MS", "exp": 12, "fee": 500, "slots": "09:00 AM - 10:00 AM, 02:00 PM - 03:00 PM, 04:00 PM - 05:00 PM", "rating": 4.7, "img": "https://via.placeholder.com/200?text=Dr.Rajesh"},
            {"name": "Dr. Priya Sharma", "spec": "Pediatrics", "qual": "MBBS, MD", "exp": 8, "fee": 400, "slots": "10:00 AM - 11:00 AM, 03:00 PM - 04:00 PM", "rating": 4.6, "img": "https://via.placeholder.com/200?text=Dr.Priya"},
            {"name": "Dr. Arun Singh", "spec": "Orthopedics", "qual": "MBBS, MS Ortho", "exp": 15, "fee": 600, "slots": "09:30 AM - 10:30 AM, 02:30 PM - 03:30 PM", "rating": 4.8, "img": "https://via.placeholder.com/200?text=Dr.Arun"}
        ]:
            username = d_data["name"].lower().replace("dr. ", "").replace(" ", "_")
            user, _ = CustomUser.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@sraisaikrupa.com", "role": "doctor"}
            )
            Doctor.objects.create(
                user=user,
                hospital=h1,
                name=d_data["name"],
                specialization=d_data["spec"],
                qualification=d_data["qual"],
                experience=d_data["exp"],
                consultation_fee=d_data["fee"],
                available_slots=d_data["slots"],
                rating=d_data["rating"],
                image=d_data["img"]
            )

        # 2. Adarsh Maternity Nursing Home
        h2 = Hospital.objects.create(
            name="Adarsh Maternity Nursing Home",
            address="Hospital Road, Kalaburagi",
            city="Kalaburagi",
            phone="08472-654321",
            specialties="Maternity, Obstetrics, Gynecology, Pediatrics",
            beds_available=8,
            rating=4.4
        )
        for d_data in [
            {"name": "Dr. Neha Patel", "spec": "Obstetrics & Gynecology", "qual": "MBBS, MS OB-GYN", "exp": 14, "fee": 700, "slots": "10:00 AM - 11:00 AM, 04:00 PM - 05:00 PM", "rating": 4.9, "img": "https://via.placeholder.com/200?text=Dr.Neha"},
            {"name": "Dr. Anjali Desai", "spec": "Pediatrics", "qual": "MBBS, MD Pediatrics", "exp": 10, "fee": 450, "slots": "09:00 AM - 10:00 AM, 02:00 PM - 03:00 PM, 05:00 PM - 06:00 PM", "rating": 4.7, "img": "https://via.placeholder.com/200?text=Dr.Anjali"}
        ]:
            username = d_data["name"].lower().replace("dr. ", "").replace(" ", "_")
            user, _ = CustomUser.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@adarshmaternity.com", "role": "doctor"}
            )
            Doctor.objects.create(
                user=user,
                hospital=h2,
                name=d_data["name"],
                specialization=d_data["spec"],
                qualification=d_data["qual"],
                experience=d_data["exp"],
                consultation_fee=d_data["fee"],
                available_slots=d_data["slots"],
                rating=d_data["rating"],
                image=d_data["img"]
            )

        # 3. Aditya Hospital
        h3 = Hospital.objects.create(
            name="Aditya Hospital",
            address="Central Plaza, Kalaburagi",
            city="Kalaburagi",
            phone="08472-789012",
            specialties="Cardiology, Neurology, General Medicine, Emergency",
            beds_available=22,
            rating=4.6
        )
        for d_data in [
            {"name": "Dr. Vikram Reddy", "spec": "Cardiology", "qual": "MBBS, MD, DM Cardiology", "exp": 18, "fee": 1000, "slots": "09:00 AM - 10:00 AM, 03:00 PM - 04:00 PM", "rating": 4.9, "img": "https://via.placeholder.com/200?text=Dr.Vikram"},
            {"name": "Dr. Sudha Nair", "spec": "General Medicine", "qual": "MBBS, MD", "exp": 9, "fee": 350, "slots": "10:00 AM - 11:00 AM, 02:00 PM - 03:00 PM, 04:00 PM - 05:00 PM, 05:30 PM - 06:30 PM", "rating": 4.5, "img": "https://via.placeholder.com/200?text=Dr.Sudha"},
            {"name": "Dr. Rajesh Rao", "spec": "Neurology", "qual": "MBBS, MD, DM Neurology", "exp": 11, "fee": 800, "slots": "11:00 AM - 12:00 PM, 03:00 PM - 04:00 PM", "rating": 4.8, "img": "https://via.placeholder.com/200?text=Dr.Rajesh"}
        ]:
            username = d_data["name"].lower().replace("dr. ", "").replace(" ", "_")
            user, _ = CustomUser.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@adityahospital.com", "role": "doctor"}
            )
            Doctor.objects.create(
                user=user,
                hospital=h3,
                name=d_data["name"],
                specialization=d_data["spec"],
                qualification=d_data["qual"],
                experience=d_data["exp"],
                consultation_fee=d_data["fee"],
                available_slots=d_data["slots"],
                rating=d_data["rating"],
                image=d_data["img"]
            )

        # 4. Al Shifa Dental Clinic
        h4 = Hospital.objects.create(
            name="Al Shifa Dental Clinic",
            address="Shopping Complex, Kalaburagi",
            city="Kalaburagi",
            phone="08472-345678",
            specialties="Dentistry, Orthodontics, Cosmetic Dentistry",
            beds_available=2,
            rating=4.3
        )
        for d_data in [
            {"name": "Dr. Ahmed Khan", "spec": "General Dentistry", "qual": "BDS, MDS", "exp": 8, "fee": 300, "slots": "09:00 AM - 10:00 AM, 10:30 AM - 11:30 AM, 02:00 PM - 03:00 PM, 03:30 PM - 04:30 PM", "rating": 4.6, "img": "https://via.placeholder.com/200?text=Dr.Ahmed"},
            {"name": "Dr. Fatima Ali", "spec": "Orthodontics", "qual": "BDS, MDS Ortho", "exp": 6, "fee": 400, "slots": "11:00 AM - 12:00 PM, 04:00 PM - 05:00 PM", "rating": 4.4, "img": "https://via.placeholder.com/200?text=Dr.Fatima"}
        ]:
            username = d_data["name"].lower().replace("dr. ", "").replace(" ", "_")
            user, _ = CustomUser.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@alshifadental.com", "role": "doctor"}
            )
            Doctor.objects.create(
                user=user,
                hospital=h4,
                name=d_data["name"],
                specialization=d_data["spec"],
                qualification=d_data["qual"],
                experience=d_data["exp"],
                consultation_fee=d_data["fee"],
                available_slots=d_data["slots"],
                rating=d_data["rating"],
                image=d_data["img"]
            )

        # 5. Anand Hospital
        h5 = Hospital.objects.create(
            name="Anand Hospital",
            address="Market Area, Kalaburagi",
            city="Kalaburagi",
            phone="08472-456789",
            specialties="General Medicine, ENT, Dermatology, Emergency",
            beds_available=12,
            rating=4.5
        )
        for d_data in [
            {"name": "Dr. Ramesh Verma", "spec": "General Medicine", "qual": "MBBS, MD", "exp": 13, "fee": 400, "slots": "09:00 AM - 10:00 AM, 02:00 PM - 03:00 PM, 05:00 PM - 06:00 PM", "rating": 4.7, "img": "https://via.placeholder.com/200?text=Dr.Ramesh"},
            {"name": "Dr. Deepak Singh", "spec": "ENT", "qual": "MBBS, MS ENT", "exp": 10, "fee": 500, "slots": "10:00 AM - 11:00 AM, 03:00 PM - 04:00 PM", "rating": 4.6, "img": "https://via.placeholder.com/200?text=Dr.Deepak"},
            {"name": "Dr. Kavya Malhotra", "spec": "Dermatology", "qual": "MBBS, MD Dermatology", "exp": 7, "fee": 450, "slots": "11:00 AM - 12:00 PM, 04:00 PM - 05:00 PM, 05:30 PM - 06:30 PM", "rating": 4.5, "img": "https://via.placeholder.com/200?text=Dr.Kavya"}
        ]:
            username = d_data["name"].lower().replace("dr. ", "").replace(" ", "_")
            user, _ = CustomUser.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@anandhospital.com", "role": "doctor"}
            )
            Doctor.objects.create(
                user=user,
                hospital=h5,
                name=d_data["name"],
                specialization=d_data["spec"],
                qualification=d_data["qual"],
                experience=d_data["exp"],
                consultation_fee=d_data["fee"],
                available_slots=d_data["slots"],
                rating=d_data["rating"],
                image=d_data["img"]
            )

        # 6. Ashirwad Maternity and Children Hospital
        h6 = Hospital.objects.create(
            name="Ashirwad Maternity and Children Hospital",
            address="Civil Lines, Kalaburagi",
            city="Kalaburagi",
            phone="08472-567890",
            specialties="Pediatrics, Maternity, Neonatal ICU, Child Development",
            beds_available=19,
            rating=4.7
        )
        for d_data in [
            {"name": "Dr. Mala Krishnan", "spec": "Pediatrics", "qual": "MBBS, MD, DCH", "exp": 16, "fee": 500, "slots": "09:00 AM - 10:00 AM, 02:00 PM - 03:00 PM, 04:00 PM - 05:00 PM", "rating": 4.9, "img": "https://via.placeholder.com/200?text=Dr.Mala"},
            {"name": "Dr. Priya Banerjee", "spec": "Neonatology", "qual": "MBBS, MD, DM Neonatology", "exp": 12, "fee": 800, "slots": "10:00 AM - 11:00 AM, 03:00 PM - 04:00 PM", "rating": 4.8, "img": "https://via.placeholder.com/200?text=Dr.Priya"}
        ]:
            username = d_data["name"].lower().replace("dr. ", "").replace(" ", "_")
            user, _ = CustomUser.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@ashirwadchildcare.com", "role": "doctor"}
            )
            Doctor.objects.create(
                user=user,
                hospital=h6,
                name=d_data["name"],
                specialization=d_data["spec"],
                qualification=d_data["qual"],
                experience=d_data["exp"],
                consultation_fee=d_data["fee"],
                available_slots=d_data["slots"],
                rating=d_data["rating"],
                image=d_data["img"]
            )

    query = request.GET.get('q', '').strip()
    city_filter = request.GET.get('city', '').strip()
    
    hospitals = Hospital.objects.all().prefetch_related('doctors')
    
    if query:
        hospitals = hospitals.filter(
            Q(name__icontains=query) | Q(specialties__icontains=query)
        )
    if city_filter:
        hospitals = hospitals.filter(city__iexact=city_filter)
        
    cities = Hospital.objects.values_list('city', flat=True).distinct()
    
    return render(request, 'hospitals/list.html', {
        'hospitals': hospitals,
        'cities': cities,
        'query': query,
        'selected_city': city_filter
    })
