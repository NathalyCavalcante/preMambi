# Generated by Django 4.2 on 2023-05-18 20:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('worker', '0007_member_available'),
        ('conversation', '0004_alter_conversation_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conversation',
            new_name='ConversationArea',
        ),
    ]
