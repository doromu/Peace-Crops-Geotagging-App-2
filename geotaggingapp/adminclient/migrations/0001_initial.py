# Generated by Django 4.0.4 on 2023-04-06 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmerID', models.CharField(max_length=255)),
                ('farmerName', models.CharField(max_length=255)),
                ('birthDate', models.DateField()),
                ('gender', models.CharField(max_length=255)),
                ('numWorkers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantID', models.CharField(max_length=255)),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('datePlanted', models.DateField()),
                ('farmerID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminclient.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordID', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('plantID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='adminclient.plant')),
            ],
        ),
    ]
