from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="A URL-friendly version of the title.")
    content = RichTextField()

    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    read_time = models.PositiveIntegerField(help_text="Estimated reading time in minutes.")

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    tags = models.ManyToManyField(Tag, related_name='projects')
    github_link = models.URLField()

    def __str__(self):
        return self.title

class AboutInfo(models.Model):
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='about_images/')
    resume = models.FileField(upload_to='resumes/')
    experience_years = models.PositiveIntegerField()
    vulnerabilities_found = models.PositiveIntegerField()
    certifications = models.CharField(max_length=300, help_text="Comma-separated list of certifications.")
    ctf_teams = models.CharField(max_length=300, help_text="Comma-separated list of CTF teams.")

    def __str__(self):
        return self.full_name

class SocialLink(models.Model):
    platform_name = models.CharField(max_length=50) # e.g., "GitHub", "LinkedIn", "Twitter"
    url = models.URLField()
    about_info = models.ForeignKey(AboutInfo, on_delete=models.CASCADE, related_name='socials')

    def __str__(self):
        return f"{self.platform_name} Link"