# Generated by Django 2.1.1 on 2018-11-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unodosmattress', '0006_news_idpatient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='contactperson',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
