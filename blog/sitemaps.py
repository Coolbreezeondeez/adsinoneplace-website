# blog/sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import Post  # <--- CHECK THIS: Is your model named 'Post'?

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # This returns all posts. 
        # If you have a 'status' field, use: Post.objects.filter(status='published')
        return Post.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        # This tells Google when the post was last updated
        return obj.updated_at
