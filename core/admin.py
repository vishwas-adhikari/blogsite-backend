from django.contrib import admin
from .models import Tag, BlogPost, Project, AboutInfo, SocialLink
# backend/core/admin.py
from .models import Ctf # Add Ctf to your imports

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'publication_date', 'read_time')
    list_filter = ('tags', 'publication_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)   #fix for tag reuse 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link')
    list_filter = ('tags',)
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',) #fix for tag reuse 

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'experience_years')
    inlines = [SocialLinkInline]




# ... (your other admin classes are fine) ...

# --- ADD THIS NEW CLASS ---
@admin.register(Ctf)
class CtfAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'rank_score', 'is_featured')
    list_filter = ('event_date', 'is_featured')
    search_fields = ('event_name', 'team_name')
    prepopulated_fields = {'slug': ('event_name',)}