# Generated by Django 4.0.2 on 2022-07-05 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_pledge_supporter_alter_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projects.project'),
        ),
    ]
