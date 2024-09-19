{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red184\green93\blue213;\red155\green162\blue177;\red81\green157\blue235;
\red136\green185\blue102;}
{\*\expandedcolortbl;;\cssrgb\c77647\c47059\c86667;\cssrgb\c67059\c69804\c74902;\cssrgb\c38039\c68627\c93725;
\cssrgb\c59608\c76471\c47451;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf3 \strokec3  django.urls \cf2 \strokec2 import\cf3 \strokec3  path\
\cf2 \strokec2 from\cf3 \strokec3  .views \cf2 \strokec2 import\cf3 \strokec3  RegisterView, CustomObtainAuthToken, UserProfileView\
\
urlpatterns \cf4 \strokec4 =\cf3 \strokec3  [\
    path(\cf5 \strokec5 'register/'\cf3 \strokec3 , RegisterView.as_view(), name\cf4 \strokec4 =\cf5 \strokec5 'register'\cf3 \strokec3 ),\
    path(\cf5 \strokec5 'login/'\cf3 \strokec3 , CustomObtainAuthToken.as_view(), name\cf4 \strokec4 =\cf5 \strokec5 'login'\cf3 \strokec3 ),\
    path(\cf5 \strokec5 'profile/'\cf3 \strokec3 , UserProfileView.as_view(), name\cf4 \strokec4 =\cf5 \strokec5 'profile'\cf3 \strokec3 ),\
]}