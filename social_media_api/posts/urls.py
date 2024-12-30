from django.urls import path
from rest_framework.routers import DefaultRouter
from posts.views import PostViewset, CommentViewset

router = DefaultRouter()
router.register(r"posts", PostViewset,  basename="posts")
router.register(r"comments", CommentViewset,  basename="posts")

urlpatterns = [

] + router.urls