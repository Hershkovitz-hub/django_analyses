# Generated by Django 3.0.8 on 2020-07-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_analyses', '0003_remove_inputdefinition_value_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputdefinition',
            name='db_value_preprocessing',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]