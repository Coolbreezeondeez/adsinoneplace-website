"""
URL configuration for adagency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogSitemap 

# Define the sitemap dictionary
sitemaps = {
    'blog': BlogSitemap,
}

# ONE single list for everything
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Core pages
    path('', core_views.home, name='home'),
    path('about/', core_views.about, name='about'),
    path('services/', core_views.services, name='services'),
    path('demo/', core_views.demo_dashboard, name='demo_dashboard'),
    
    # App includes
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),

    # The Sitemap (Moved inside here!)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

# This is needed for images to load if you are in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
