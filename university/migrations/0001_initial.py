# Generated by Django 4.2 on 2023-06-26 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persnr', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Vorlesung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorlnr', models.IntegerField(unique=True)),
                ('titel', models.CharField(max_length=128)),
                ('dozent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matnr', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=64)),
                ('hoert', models.ManyToManyField(blank=True, to='university.vorlesung')),
            ],
        ),
    ]