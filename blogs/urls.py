# blogs/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BlogPostViewSet,
    CommentListCreateView,
    StorySubmissionCreateView,
    FeedbackCreateView,
)

# 1. Set up router for BlogPostViewSet
router = DefaultRouter()
router.register(r'blogs', BlogPostViewSet)  # This handles /blogs/, /blogs/<id>/ etc.

# 2. Add all routes
urlpatterns = [
    path('api/', include(router.urls)),  # This makes /api/blogs/ available
    path('api/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('api/stories/', StorySubmissionCreateView.as_view(), name='story-submit'),
    path('api/feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
