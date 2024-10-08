{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from django.urls import path, include\
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView\
from rest_framework.routers import DefaultRouter\
\
router = DefaultRouter()\
router.register(r'posts', PostViewSet)\
router.register(r'comments', CommentViewSet)\
\
urlpatterns = [\
    path('', include(router.urls)),\
    path('feed/', FeedView.as_view(), name='feed'),  # Use FeedView instead of FeedViewSet\
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),  # Like a post\
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),  # Unlike a post\
]\
\
}