# Generated by Django 4.1.7 on 2023-05-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]