# Generated by Django 4.2.2 on 2023-06-30 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('idtipoUsuario', models.AutoField(db_column='idtipo', primary_key=True, serialize=False, verbose_name='id_tipoUsuario')),
                ('tipoUsuario', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apaterno', models.CharField(max_length=30)),
                ('amaterno', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('clave', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('codpos', models.CharField(max_length=7)),
                ('tipoUsuario', models.ForeignKey(db_column='idtipo', on_delete=django.db.models.deletion.CASCADE, to='Botania.tipousuario')),
            ],
        ),
    ]