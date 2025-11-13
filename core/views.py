from django.shortcuts import render
from blog.models import Post


def home(request):
    """Homepage view"""
    # Get latest 3 published blog posts for homepage
    latest_posts = Post.objects.filter(status='published')[:3]
    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page view"""
    return render(request, 'core/about.html')


def services(request):
    """Services page view"""
    # You can add service data here or from database
    services_list = [
        {
            'name': 'Facebook & Instagram Ads',
            'description': 'Reach your target audience on Meta platforms with precision targeting and compelling creative.',
            'icon': 'fab fa-facebook-square'
        },
        {
            'name': 'Google Ads',
            'description': 'Capture high-intent customers with search, display, and shopping campaigns.',
            'icon': 'fab fa-google'
        },
        {
            'name': 'TikTok Advertising',
            'description': 'Connect with younger demographics through engaging short-form video content.',
            'icon': 'fab fa-tiktok'
        },
        {
            'name': 'CTV/OTT Advertising',
            'description': 'Reach cord-cutters with targeted streaming TV advertising campaigns.',
            'icon': 'fas fa-tv'
        },
        {
            'name': 'Display & Banner Ads',
            'description': 'Build brand awareness across premium publisher networks.',
            'icon': 'fas fa-rectangle-ad'
        },
        {
            'name': 'Analytics & Reporting',
            'description': 'Data-driven insights and comprehensive campaign performance dashboards.',
            'icon': 'fas fa-chart-line'
        },
    ]
    context = {
        'services': services_list,
    }
    return render(request, 'core/services.html', context)
