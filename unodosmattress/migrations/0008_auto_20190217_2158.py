# Generated by Django 2.1.1 on 2019-02-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unodosmattress', '0007_patient_contactperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(default='Active', max_length=45),
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(default='Active', max_length=45),
        ),
    ]
