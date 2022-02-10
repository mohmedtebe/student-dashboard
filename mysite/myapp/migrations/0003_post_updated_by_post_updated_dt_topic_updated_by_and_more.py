# Generated by Django 4.0 on 2022-01-04 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myapp', '0002_topic_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth.user'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_dt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth.user'),
        ),
        migrations.AddField(
            model_name='topic',
            name='updated_date',
            field=models.DateTimeField(null=True),
        ),
    ]
