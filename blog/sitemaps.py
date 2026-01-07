# blog/sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import Post  # <--- CHECK THIS: Is your model named 'Post'?

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all().order_by('-created_at')

   def lastmod(self, obj):
    return obj.updated_at
