# Generated by Django 3.0.8 on 2020-07-18 20:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20200718_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skills',
            options={'ordering': ['id'], 'verbose_name': 'Skill'},
        ),
        migrations.AddField(
            model_name='employee',
            name='cv',
            field=ckeditor.fields.RichTextField(default='text'),
            preserve_default=False,
        ),
    ]
