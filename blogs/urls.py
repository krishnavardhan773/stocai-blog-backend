# blogs/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BlogPostViewSet,
    BlogPostList,
    CommentListCreateView,
    CommentList,
    StorySubmissionCreateView,
    FeedbackCreateView,
)

router = DefaultRouter()
router.register(r'blogs', BlogPostViewSet)

urlpatterns = [
    # Router-based URLs (e.g., /blogs/, /blogs/<id>/)
    path('', include(router.urls)),

    # Manually defined function/class-based views
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('stories/', StorySubmissionCreateView.as_view(), name='story-submit'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),

    # Optional: fallback blog list view (if used in frontend)
    path('blog-list/', BlogPostList.as_view(), name='blog-list'),

    # Optional: separate list view for comments if used
    path('comment-list/', CommentList.as_view(), name='comment-list'),
]

from .views import FeedbackListAdminView

urlpatterns += [
    path('admin/feedback/', FeedbackListAdminView.as_view(), name='admin-feedback'),
]
from .views import FeedbackListAdminView

urlpatterns += [
    path('admin/feedback/', FeedbackListAdminView.as_view(), name='admin-feedback'),
]
