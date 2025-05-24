from rest_framework import viewsets
from .models import BlogPost, Feedback
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reaction

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        blog = self.get_object()
        ip = request.META.get('REMOTE_ADDR')
        Reaction.objects.create(blog=blog, reaction_type='like', ip_address=ip)
        return Response({'status': 'liked'})

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        blog = self.get_object()
        ip = request.META.get('REMOTE_ADDR')
        Reaction.objects.create(blog=blog, reaction_type='dislike', ip_address=ip)
        return Response({'status': 'disliked'})

from rest_framework import generics
from .serializers import CommentSerializer
from .models import Comment

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        blog_id = self.request.query_params.get('blog_id')
        if blog_id:
            return Comment.objects.filter(blog_id=blog_id).order_by('-created_at')
        return Comment.objects.none()

from rest_framework import generics
from .models import StorySubmission
from .serializers import StorySubmissionSerializer

class StorySubmissionCreateView(generics.CreateAPIView):
    serializer_class = StorySubmissionSerializer
    queryset = StorySubmission.objects.all()

from .serializers import FeedbackSerializer

class FeedbackCreateView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

# blogs/views.py
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all().order_by('-created_at')  # optional: latest first
    serializer_class = CommentSerializer

from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostList(generics.ListAPIView):
    queryset = BlogPost.objects.all().order_by("-created_at")
    serializer_class = BlogPostSerializer

from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackListAdminView(generics.ListAPIView):
    queryset = Feedback.objects.all().order_by('-submitted_at')
    serializer_class = FeedbackSerializer
    # No permission_classes → open to all
    # 🔓 No permission_classes → open to public

from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class PublicBlogCreateView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # No authentication required
