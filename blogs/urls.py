# blogs/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BlogPostViewSet,
    CommentListCreateView,
    StorySubmissionCreateView,
    FeedbackCreateView,
)

# 1. Router for blog CRUD
router = DefaultRouter()
router.register(r'blogs', BlogPostViewSet)

# 2. Correct URL patterns (no 'api/' here)
urlpatterns = [
    path('', include(router.urls)),  # Will become /api/blogs/
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('stories/', StorySubmissionCreateView.as_view(), name='story-submit'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
