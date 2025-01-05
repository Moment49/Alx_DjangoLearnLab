from django.urls import path
from rest_framework.routers import DefaultRouter
from posts.views import PostViewset, CommentViewset, UserFeedView

router = DefaultRouter()
router.register(r"posts", PostViewset,  basename="posts")
router.register(r"comments", CommentViewset,  basename="comments")

urlpatterns = [
   path('feed/', UserFeedView.as_view(), name="user_feed")
] + router.urls