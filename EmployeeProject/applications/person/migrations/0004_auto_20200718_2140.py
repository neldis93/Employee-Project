# Generated by Django 3.0.8 on 2020-07-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_employee_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['first_name'], 'verbose_name': 'My Employee'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Skill'},
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.CharField(choices=[('0', 'Developer'), ('1', 'Administrator'), ('2', 'Support technician'), ('3', 'Web designer'), ('4', 'Others')], max_length=30, verbose_name='Job'),
        ),
    ]