from rest_framework import viewsets
from .models import BlogPost, Project, AboutInfo
from .serializers import BlogPostSerializer, ProjectSerializer, AboutInfoSerializer
from django.http import JsonResponse #health check 

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


def health_check(request):
    """
    A simple view that returns a 200 OK response with minimal data.
    Perfect for a pinger service.
    """
    return JsonResponse({"status": "ok"})