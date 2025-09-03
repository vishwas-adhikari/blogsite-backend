from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, ProjectViewSet, AboutInfoViewSet
from .views import CtfViewSet

router = DefaultRouter()
router.register(r'blog-posts', BlogPostViewSet, basename='blogpost')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'about', AboutInfoViewSet, basename='about')
router.register(r'ctfs', CtfViewSet, basename='ctf') # <-- ADD THIS LINE

urlpatterns = [
    path('', include(router.urls)),
]

 



