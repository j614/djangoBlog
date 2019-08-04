from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly' #частота
    priority = 0.9      #актуальность

#возвращает QuerySet объектов для включения вфайл Sitemap
    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated