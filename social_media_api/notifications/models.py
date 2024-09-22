{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from django.db import models\
from django.contrib.auth import get_user_model\
from django.contrib.contenttypes.fields import GenericForeignKey\
from django.contrib.contenttypes.models import ContentType\
\
User = get_user_model()\
\
class Notification(models.Model):\
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')\
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor_notifications')\
    verb = models.CharField(max_length=255)\
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)\
    target_object_id = models.PositiveIntegerField()\
    target = GenericForeignKey('target_content_type', 'target_object_id')\
    timestamp = models.DateTimeField(auto_now_add=True)\
    is_read = models.BooleanField(default=False)\
\
    def __str__(self):\
        return f'Notification for \{self.recipient\}'\
}