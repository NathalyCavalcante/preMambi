# Generated by Django 4.2 on 2023-05-18 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0003_rename_member_conversation_worker'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ('-modified_at',)},
        ),
    ]
