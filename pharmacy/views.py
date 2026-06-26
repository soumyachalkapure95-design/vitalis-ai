from django.shortcuts import render
from django.db.models import Q
from .models import Medicine

def medicine_list(request):
    # Auto-populate mock medicines if empty
    if Medicine.objects.count() == 0:
        Medicine.objects.bulk_create([
            Medicine(
                name="Paracetamol (Acetaminophen)",
                description="Common analgesic used to treat pain and fever.",
                use="Pain Relief, Fever Reduction",
                dosage="1-2 tablets of 500mg every 4-6 hours, not exceeding 4g daily.",
                side_effects="Rare if used correctly. Excessive dosage may cause severe liver damage.",
                category="Analgesics",
                price=2.50,
                image="/static/pharmacy/images/paracetamol.png"
            ),
            Medicine(
                name="Ibuprofen",
                description="Nonsteroidal anti-inflammatory drug (NSAID) which reduces pain, inflammation, and fever.",
                use="Pain Relief, Joint Inflammation, Fever Reduction",
                dosage="400mg every 4-6 hours after food.",
                side_effects="Stomach discomfort, nausea, risk of gastrointestinal ulcers.",
                category="Analgesics",
                price=4.20,
                image="/static/pharmacy/images/ibuprofen.png"
            ),
            Medicine(
                name="Amoxicillin",
                description="Penicillin-class antibiotic that fights bacterial infections.",
                use="Bacterial Infections (Ear, Throat, UTI, Skin)",
                dosage="500mg three times daily for 5-7 days as prescribed.",
                side_effects="Diarrhea, nausea, allergic skin rashes.",
                category="Antibiotics",
                price=12.80,
                image="/static/pharmacy/images/amoxicillin.png"
            ),
            Medicine(
                name="Cetirizine (Zyrtec)",
                description="Antihistamine that blocks histamine release to relieve allergy symptoms.",
                use="Allergy Relief, Runny Nose, Itchy Eyes, Hives",
                dosage="10mg once daily.",
                side_effects="Mild drowsiness, dry mouth, tiredness.",
                category="Antihistamines",
                price=5.00,
                image="/static/pharmacy/images/cetirizine.png"
            ),
            Medicine(
                name="Metformin",
                description="First-line oral medication for type 2 diabetes that helps control blood sugar levels.",
                use="Type 2 Diabetes Management",
                dosage="500mg twice daily with meals to start, adjusted by clinician.",
                side_effects="Diarrhea, bloating, stomach cramping.",
                category="Antidiabetic",
                price=8.50,
                image="/static/pharmacy/images/metformin.png"
            ),
            Medicine(
                name="Atorvastatin (Lipitor)",
                description="Statin drug that reduces LDL 'bad' cholesterol and triglycerides.",
                use="Cholesterol Control, Cardiovascular Risk Prevention",
                dosage="10-20mg once daily, preferably in the evening.",
                side_effects="Muscle pain, headache, digestive problems.",
                category="Cardiovascular",
                price=15.30,
                image="/static/pharmacy/images/atorvastatin.png"
            ),
            Medicine(
                name="Omeprazole (Prilosec)",
                description="Proton pump inhibitor (PPI) that decreases stomach acid production.",
                use="Heartburn, GERD, Stomach Ulcers",
                dosage="20mg once daily, 30 minutes before breakfast.",
                side_effects="Headache, abdominal discomfort, nausea.",
                category="Gastrointestinal",
                price=6.70,
                image="/static/pharmacy/images/omeprazole.png"
            ),
            Medicine(
                name="Aspirin",
                description="Widely used to reduce pain, fever, and inflammation, as well as a blood thinner.",
                use="Pain Relief, Heart Attack Prevention, Anti-inflammatory",
                dosage="75-325mg daily as directed.",
                side_effects="Stomach irritation, bleeding risk.",
                category="Analgesics",
                price=3.00,
                image="/static/pharmacy/images/aspirin.png"
            ),
            Medicine(
                name="Albuterol (Inhaler)",
                description="Bronchodilator that relaxes muscles in the airways and increases air flow to the lungs.",
                use="Asthma Relief, COPD, Bronchospasm Treatment",
                dosage="1-2 puffs every 4-6 hours as needed.",
                side_effects="Tremors, nervousness, rapid heart rate.",
                category="Respiratory",
                price=24.50,
                image="/static/pharmacy/images/albuterol.png"
            ),
            Medicine(
                name="Lisinopril",
                description="ACE inhibitor used to treat high blood pressure and heart failure.",
                use="Hypertension Control, Heart Failure Management",
                dosage="10mg once daily.",
                side_effects="Persistent dry cough, dizziness, high potassium levels.",
                category="Cardiovascular",
                price=9.90,
                image="/static/pharmacy/images/lisinopril.png"
            ),
            Medicine(
                name="Insulin Glargine (Lantus)",
                description="Long-acting basal insulin analogue used to improve glycemic control.",
                use="Type 1 and Type 2 Diabetes Management",
                dosage="Injected subcutaneously once daily as prescribed.",
                side_effects="Hypoglycemia, injection site reactions.",
                category="Antidiabetic",
                price=45.00,
                image="/static/pharmacy/images/insulin.png"
            ),
        ])

    query = request.GET.get('q', '').strip()
    category_filter = request.GET.get('category', '').strip()
    
    medicines = Medicine.objects.all()
    
    if query:
        medicines = medicines.filter(
            Q(name__icontains=query) | Q(use__icontains=query) | Q(description__icontains=query)
        )
    if category_filter:
        medicines = medicines.filter(category__iexact=category_filter)
        
    categories = Medicine.objects.values_list('category', flat=True).distinct()
    
    return render(request, 'pharmacy/list.html', {
        'medicines': medicines,
        'categories': categories,
        'query': query,
        'selected_category': category_filter
    })
