# Generated by Django 4.0 on 2022-01-04 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_post_updated_by_post_updated_dt_topic_updated_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updated_dt',
            new_name='updated_date',
        ),
    ]
