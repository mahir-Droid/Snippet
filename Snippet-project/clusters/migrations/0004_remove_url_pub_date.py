# Generated by Django 2.2 on 2021-11-29 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0003_remove_cluster_text_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='pub_date',
        ),
    ]
