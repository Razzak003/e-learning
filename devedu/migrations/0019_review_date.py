# Generated by Django 4.1.4 on 2023-08-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devedu", "0018_alter_reviewcoursemiddle_course"),
    ]

    operations = [
        migrations.AddField(
            model_name="review", name="date", field=models.DateField(auto_now=True),
        ),
    ]