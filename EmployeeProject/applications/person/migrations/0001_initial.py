# Generated by Django 3.0.8 on 2020-07-16 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0002_auto_20200716_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('job', models.CharField(choices=[('0', 'Developer'), ('1', 'Administrator'), ('2', 'Support technician'), ('3', 'Web designer'), ('4', 'Others')], max_length=30, verbose_name='Job')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
            ],
        ),
    ]
