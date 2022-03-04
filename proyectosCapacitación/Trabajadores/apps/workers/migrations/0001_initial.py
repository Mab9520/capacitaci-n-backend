# Generated by Django 3.1 on 2022-03-03 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerTypeWork',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('workertype', models.CharField(max_length=50, verbose_name='Tipo')),
                ('time', models.CharField(max_length=10, verbose_name='Tiempo')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'tipo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('workername', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('email', models.CharField(max_length=50, verbose_name='Correo')),
                ('age', models.IntegerField(default=0, verbose_name='Edad')),
                ('address', models.CharField(max_length=150, verbose_name='Direccion')),
                ('password', models.CharField(max_length=150, verbose_name='Contraseña')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('workertype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.workertypework')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
                'db_table': 'trabajador',
                'ordering': ['id'],
            },
        ),
    ]
