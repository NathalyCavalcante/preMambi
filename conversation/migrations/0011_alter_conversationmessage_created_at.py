# Generated by Django 4.2 on 2023-05-26 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0010_alter_conversationmessage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
