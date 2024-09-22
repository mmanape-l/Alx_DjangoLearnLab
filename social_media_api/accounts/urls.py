{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red184\green93\blue213;\red155\green162\blue177;\red0\green0\blue0;
\red81\green157\blue235;\red136\green185\blue102;}
{\*\expandedcolortbl;;\cssrgb\c77647\c47059\c86667;\cssrgb\c67059\c69804\c74902;\cssrgb\c0\c0\c0;
\cssrgb\c38039\c68627\c93725;\cssrgb\c59608\c76471\c47451;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \expnd0\expndtw0\kerning0
from\cf3  django.urls \cf2 import\cf3  path\
\cf2 from\cf3  .views \cf2 import\cf3  RegisterView, CustomObtainAuthToken, UserProfileView\
\pard\pardeftab720\partightenfactor0
\cf0 from .views import UserList, FollowUserView, UnfollowUserView\cf3 \
\
urlpatterns \cf5 =\cf3  [\
    path(\cf6 'register/'\cf3 , RegisterView.as_view(), name\cf5 =\cf6 'register'\cf3 ),\
    path(\cf6 'login/'\cf3 , CustomObtainAuthToken.as_view(), name\cf5 =\cf6 'login'\cf3 ),\
    path(\cf6 'profile/'\cf3 , UserProfileView.as_view(), name\cf5 =\cf6 'profile'\cf3 ),\
\pard\pardeftab720\li683\fi-57\partightenfactor0
\cf0 \outl0\strokewidth0 \strokec4 path('users/', UserList.as_view(), name='user-list'),\cf3 \outl0\strokewidth0 \
\pard\pardeftab720\li683\fi-4\partightenfactor0
\cf0 path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),\
\pard\pardeftab720\li668\fi10\partightenfactor0
\cf0 path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),\cf3 \
\pard\pardeftab720\partightenfactor0
\cf3 ]}