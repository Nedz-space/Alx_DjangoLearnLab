from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', LikeViewSet.as_view({'post': 'like'}), name='like-post'),
    path('posts/<int:pk>/unlike/', LikeViewSet.as_view({'post': 'unlike'}), name='unlike-post'),
]

