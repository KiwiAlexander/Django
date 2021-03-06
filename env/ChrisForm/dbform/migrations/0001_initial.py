# Generated by Django 2.1.2 on 2018-10-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Email', models.CharField(max_length=100)),
                ('Notes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Volunteer', models.CharField(max_length=100)),
                ('Client', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Summary', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
    ]
