# Generated by Django 4.2 on 2023-04-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_under_menu_mini_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
