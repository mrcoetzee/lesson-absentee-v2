# Generated by Django 5.0 on 2024-01-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_delete_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='reg_class',
            field=models.CharField(max_length=3, null=True),
        ),
    ]