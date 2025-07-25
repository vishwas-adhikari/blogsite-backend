from rest_framework import serializers
from .models import Tag, BlogPost, Project, AboutInfo, SocialLink
from django.utils.html import strip_tags 

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)
    excerpt = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'content', 'publication_date', 'image', 'tags', 'read_time','excerpt']
    
     # 3. DEFINE THE METHOD TO CREATE THE EXCERPT
    def get_excerpt(self, obj):
        # Strip all HTML tags from the content
        plain_text = strip_tags(obj.content)
        # Return the first 150 characters, followed by an ellipsis
        return plain_text[:150] + '...'


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'tags', 'github_link']

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['id', 'platform_name', 'url']

class AboutInfoSerializer(serializers.ModelSerializer):
    socials = SocialLinkSerializer(many=True, read_only=True)
    resume = serializers.FileField(use_url=True)
    profile_image = serializers.ImageField(use_url=True)

    class Meta:
        model = AboutInfo
        fields = [
            'id', 'full_name', 'bio', 'profile_image', 'resume', 'experience_years',
            'vulnerabilities_found', 'certifications', 'ctf_teams', 'socials'
        ]