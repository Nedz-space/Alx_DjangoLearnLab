
# Create your views here.

from rest_framework import viewsets, permissions, status, filters, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.models import Notification  # ✅ Ensure Notification model exists
from notifications.utils import create_notification  # ✅ Ensure function exists

class PostViewSet(viewsets.ModelViewSet):
    """Viewset for managing posts."""
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # ✅ Add filtering
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """Viewset for managing comments."""
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)

        # ✅ Create a notification when a comment is added
        Notification.objects.create(
            recipient=comment.post.author,
            actor=self.request.user,
            verb='commented on your post',
            target=comment.post
        )

class LikeViewSet(viewsets.ModelViewSet):
    """Viewset for managing likes."""
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        """Like a post"""
        post = generics.get_object_or_404(Post, pk=pk)  # ✅ Using `generics.get_object_or_404`
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # ✅ Create a notification when a post is liked
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        """Unlike a post"""
        try:
            like = Like.objects.get(user=request.user, post_id=pk)
            like.delete()
            return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'message': 'Like does not exist'}, status=status.HTTP_400_BAD_REQUEST)
