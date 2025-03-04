# Generated by Django 5.1.5 on 2025-03-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('tipo', models.CharField(choices=[('Guia', 'Guia'), ('Aventureiro', 'Aventureiro')], default='Aventureiro', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='userapi_usuario_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='userapi_usuario_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
