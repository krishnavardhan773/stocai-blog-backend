from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

router = DefaultRouter()
router.register(r'blogs', BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from .views import CommentListCreateView

urlpatterns += [
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]

from .views import StorySubmissionCreateView

urlpatterns += [
    path('stories/', StorySubmissionCreateView.as_view(), name='story-submit'),
]

from .views import FeedbackCreateView

urlpatterns += [
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]

# blogs/urls.py
from django.urls import path
from .views import CommentList

urlpatterns = [
    path("api/comments/", CommentList.as_view(), name="comment-list"),
]
