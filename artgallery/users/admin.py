from django.contrib import admin
from .models import NewsArticle, InstagramPost, ProgressStat, AboutSection, HeroSection

admin.site.register(NewsArticle)
admin.site.register(InstagramPost)
admin.site.register(ProgressStat)
admin.site.register(AboutSection)
admin.site.register(HeroSection)