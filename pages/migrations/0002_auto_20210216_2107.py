# Generated by Django 3.0.7 on 2021-02-16 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='facebook_link',
            new_name='github_link',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='google_plus',
            new_name='instagram_link',
        ),
    ]
