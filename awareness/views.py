from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    # Auto-populate mock articles if empty
    if Article.objects.count() == 0:
        Article.objects.bulk_create([
            Article(
                title="The Essential Guide to Daily Hydration",
                summary="Discover why drinking enough water is crucial for metabolic function, muscle recovery, and energy levels.",
                content="Water is the foundation of health. Every cell, tissue, and organ in your body needs water to work properly. For instance, water maintains body temperature, lubricates joints, protects sensitive tissues, and gets rid of wastes through urination, perspiration, and bowel movements.\n\nHow much should you drink? While the standard '8 glasses a day' is a good benchmark, individual needs vary based on exercise levels, climate, and general health. A better indicator is the color of your urine—it should be pale yellow or clear.\n\nTips to stay hydrated:\n1. Keep a reusable bottle near you.\n2. Add fresh lemon or cucumber for flavor.\n3. Drink a glass of water immediately after waking up.",
                category="Nutrition",
                read_time=3
            ),
            Article(
                title="Cardio vs Strength Training: Finding Balance",
                summary="Which training methodology matches your goals? We analyze the metabolic benefits of both.",
                content="A common debate in fitness is whether to prioritize cardiovascular exercise or strength training. Cardio burns more calories per session and strengthens the heart and lungs. Strength training, on the other hand, builds lean muscle mass which raises your basal metabolic rate (burning more calories at rest) and strengthens bones.\n\nFor optimal health, the World Health Organization recommends a combination of both. Aim for at least 150 minutes of moderate cardiovascular activity combined with two sessions of full-body resistance training per week.",
                category="Fitness",
                read_time=5
            ),
            Article(
                title="Mastering Sleep Hygiene for Mental Focus",
                summary="Struggling with fatigue? Read our checklist for establishing a restorative evening routine.",
                content="Quality sleep is just as important as diet and exercise. Poor sleep is linked to concentration issues, weight gain, weakened immunity, and long-term cardiovascular risks.\n\nTo improve your sleep, establish good sleep hygiene:\n1. Maintain a consistent sleep schedule (even on weekends).\n2. Remove screens (phones, TVs) at least 1 hour before bed; blue light suppresses melatonin production.\n3. Keep your room dark, quiet, and slightly cool.\n4. Avoid heavy meals and caffeine in the late afternoon and evening.",
                category="Preventive Care",
                read_time=4
            ),
            Article(
                title="Understanding Hand Hygiene and Microbe Defense",
                summary="Review clean handwashing steps to protect yourself and your family from infections.",
                content="Handwashing is one of the most effective ways to prevent the spread of germs and infections. Throughout the day, we touch objects that contain viruses and bacteria, and then we touch our eyes, nose, and mouth, letting the germs enter our body.\n\nProper handwashing technique:\n1. Wet hands with clean, running water.\n2. Apply soap and lather thoroughly.\n3. Scrub hands for at least 20 seconds, including the backs, between fingers, and under nails.\n4. Rinse well under running water.\n5. Dry hands using a clean towel.",
                category="Hygiene",
                read_time=3
            ),
        ])

    category_filter = request.GET.get('category', '').strip()
    
    articles = Article.objects.all().order_by('-created_at')
    if category_filter:
        articles = articles.filter(category__iexact=category_filter)
        
    categories = [choice[0] for choice in Article.CATEGORY_CHOICES]
    
    return render(request, 'awareness/articles.html', {
        'articles': articles,
        'categories': categories,
        'selected_category': category_filter
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'awareness/detail.html', {'article': article})
