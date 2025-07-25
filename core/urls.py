from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, ProjectViewSet, AboutInfoViewSet

router = DefaultRouter()
router.register(r'blog-posts', BlogPostViewSet, basename='blogpost')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'about', AboutInfoViewSet, basename='about')

urlpatterns = [
    path('', include(router.urls)),
]