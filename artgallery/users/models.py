from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class InstagramPost(models.Model):
    image = models.ImageField(upload_to='instagram/')
    caption = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.caption or f"Post {self.id}"

class ProgressStat(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class AboutSection(models.Model):
    title = models.CharField(max_length=100, default="About Artistry")
    subtitle = models.CharField(max_length=200, default="We Arrange Arts Personally & Bring Happiness")
    description = models.TextField()
    ceo_name = models.CharField(max_length=100, default="John Doe", blank=True)
    ceo_title = models.CharField(max_length=100, default="CEO, Art Gallery", blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HeroSection(models.Model):
    title = models.CharField(max_length=200, default="Welcome to Our Art Gallery")
    description = models.TextField(default="Discover breathtaking art pieces created by talented artists from all around the world")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title