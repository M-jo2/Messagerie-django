# Generated by Django 3.1.2 on 2020-10-13 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0005_auto_20201012_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagerie',
            name='id_user1',
        ),
        migrations.RemoveField(
            model_name='messagerie',
            name='id_user2',
        ),
        migrations.AddField(
            model_name='messagerie',
            name='user1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firstUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='messagerie',
            name='user2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SecUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
