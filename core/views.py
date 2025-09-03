from rest_framework import viewsets
from .models import BlogPost, Project, AboutInfo
from .serializers import BlogPostSerializer, ProjectSerializer, AboutInfoSerializer
from .models import Ctf 
from .serializers import CtfSerializer 

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all().order_by('-publication_date')
    serializer_class = BlogPostSerializer
    lookup_field ='slug'

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer

class AboutInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutInfo.objects.all()
    serializer_class = AboutInfoSerializer



class CtfViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ctf.objects.all()
    serializer_class = CtfSerializer
    lookup_field = 'slug' # We'll use the slug for detail pages