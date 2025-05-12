from django.shortcuts import render
from .models import NewsArticle, InstagramPost, ProgressStat, AboutSection, HeroSection

def home(request):
    hero = HeroSection.objects.first()
    about_section = AboutSection.objects.first()
    news_articles = NewsArticle.objects.all().order_by('-date')[:3]
    instagram_posts = InstagramPost.objects.all()[:6]
    progress_stats = ProgressStat.objects.all()[:4]
    context = {
        'hero': hero,
        'about_section': about_section,
        'news_articles': news_articles,
        'instagram_posts': instagram_posts,
        'progress_stats': progress_stats,
    }
    return render(request, 'home.html', context)

def about(request):
    about_section = AboutSection.objects.first()
    context = {
        'about_section': about_section,
    }
    return render(request, 'about.html', context)

def portfolio(request):
    # Placeholder for portfolio view; update with actual logic if needed
    return render(request, 'portfolio.html')

def team(request):
    # Placeholder for team view; update with actual logic if needed
    return render(request, 'team.html')

def contact(request):
    # Placeholder for contact view; update with actual logic if needed
    return render(request, 'contact.html')