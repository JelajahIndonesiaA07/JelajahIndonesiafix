# Generated by Django 4.1 on 2022-10-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kuisioner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('umur', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('vaksin', models.BooleanField()),
                ('negara', models.CharField(max_length=255)),
                ('tujuan', models.CharField(max_length=255)),
                ('prov', models.CharField(max_length=255)),
                ('kontak', models.CharField(max_length=15)),
            ],
        ),
    ]
