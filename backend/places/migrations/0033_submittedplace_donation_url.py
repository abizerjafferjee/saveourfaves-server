# Generated by Django 3.0.4 on 2020-03-26 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0032_submittedplace_matched_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='submittedplace',
            name='donation_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
