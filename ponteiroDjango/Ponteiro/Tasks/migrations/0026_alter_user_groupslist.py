# Generated by Django 4.2.7 on 2023-11-09 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0025_userlistnode_linkedlist_user_groupslist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groupsList',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tasks.linkedlist'),
        ),
    ]
