# Generated by Django 5.0.6 on 2024-06-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Обычный пользователь'), (2, 'Редактор'), (3, 'Менеджер')], default=1),
        ),
    ]
