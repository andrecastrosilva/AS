# Generated by Django 4.0.3 on 2022-05-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0003_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sprints',
            field=models.ManyToManyField(to='scrum.sprint'),
        ),
    ]