from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls

more_url_patterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]

urlpatterns = urlpatterns + more_url_patterns
