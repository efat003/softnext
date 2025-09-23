from django.db import models
from django.utils.text import slugify

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="SoftNext")
    logo = models.ImageField(upload_to='site/logo/', blank=True, null=True)
    email = models.EmailField(default="info@softnext.com")
    phone = models.CharField(max_length=20, default="+880 1627457073")
    address = models.TextField(default="Mirpur, Dhaka, Bangladesh")
    
    # Social Media
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    
    # Content
    hero_title = models.CharField(max_length=200, default="Transform Your Ideas Into Digital Reality")
    hero_description = models.TextField(default="We create custom software solutions that drive growth, innovation, and success for businesses worldwide.")
    footer_text = models.TextField(default="© 2025 SoftNext | All Rights Reserved By SoftNext")
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class, e.g., 'fas fa-laptop-code'")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    description = models.TextField()
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['display_order', 'title']

class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('app', 'Mobile Apps'),
        ('ui', 'UI/UX Design'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_featured', 'display_order']

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    bio = models.TextField()
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['display_order', 'name']

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.company}"

    class Meta:
        ordering = ['-created_at']

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['display_order']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-received_at']

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-subscribed_at']