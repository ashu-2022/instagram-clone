from django.urls import path
from core.views import (HomeView, FollowDoneView,
    UnfollowDoneView, PostCreateView, PostDeleteView,
    PostDetailView, PostLikeView, PostUnlikeView,
    PostCommentView,PostSaveView,PostUnsaveView ,
    LikePostsView, ExplorePostsView,SavePostsView)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('feed/',login_required(HomeView.as_view()),name='home_feed_view'),
    
    path('follow/done/',login_required(FollowDoneView.as_view()),name='follow_done_view'),
    path('unfollow/done/',login_required(UnfollowDoneView.as_view()),name='unfollow_done_view'),
    
    path('post/create/',login_required(PostCreateView.as_view()),name='post_create_view'),
    path('post/delete/<int:id>/',login_required(PostDeleteView.as_view()),name='post_delete_view'),
    path('post/save/<int:id>/',login_required(PostSaveView.as_view()),name='post_save_view'),
    path('post/unsave/<int:id>/',login_required(PostUnsaveView.as_view()),name='post_unsave_view'),
    
    path('post/like/',login_required(LikePostsView.as_view()),name='liked_posts_view'),
    path('post/explore/',login_required(ExplorePostsView.as_view()),name='explore_posts_view'),
    path('post/save/',login_required(SavePostsView.as_view()),name='saved_posts_view'),
    
    path('post/<int:id>/',login_required(PostDetailView.as_view()),name='post_detail_view'),
    path('post/like/<int:id>/',login_required(PostLikeView.as_view()),name='post_like_view'),
    path('post/unlike/<int:id>/',login_required(PostUnlikeView.as_view()),name='post_unlike_view'),
    path('post/comment/<int:id>/',login_required(PostCommentView.as_view()),name='post_comment_view'),
    
    
  
]
