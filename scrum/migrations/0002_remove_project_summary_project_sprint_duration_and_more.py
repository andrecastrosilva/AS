# Generated by Django 4.0.3 on 2022-05-25 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scrum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='summary',
        ),
        migrations.AddField(
            model_name='project',
            name='sprint_duration',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='sprints',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='annotations',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='project',
            name='tasks',
        ),
        migrations.AddField(
            model_name='project',
            name='tasks',
            field=models.ManyToManyField(to='scrum.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='for+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tasks', models.ManyToManyField(to='scrum.task')),
            ],
        ),
    ]
