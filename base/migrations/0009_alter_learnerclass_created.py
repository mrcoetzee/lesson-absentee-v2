# Generated by Django 5.0.1 on 2024-02-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_learnerclass_lesson_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnerclass',
            name='created',
            field=models.DateTimeField(),
        ),
    ]