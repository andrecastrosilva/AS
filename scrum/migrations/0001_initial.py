# Generated by Django 4.0.3 on 2022-05-25 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('as_a', models.TextField()),
                ('i_want', models.TextField()),
                ('so_that', models.TextField()),
                ('points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'To Do'), (2, 'In Progress'), (3, 'In Review'), (4, 'Finished'), (5, 'Canceled')], null=True)),
                ('assigned_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abc', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tasks', models.DateTimeField(auto_now_add=True)),
                ('state', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'In Progress'), (2, 'Finished')], null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
            options={
                'permissions': (('master', 'Master Permissions'), ('developer', 'Developer Permissions'), ('boss', 'Boss Permissions')),
            },
        ),
    ]
