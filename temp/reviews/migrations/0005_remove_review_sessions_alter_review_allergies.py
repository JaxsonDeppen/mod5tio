# Generated by Django 5.1.3 on 2025-02-07 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_allergies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='sessions',
        ),
        migrations.AlterField(
            model_name='review',
            name='allergies',
            field=models.CharField(choices=[('Dairy', 'Dairy'), ('Peanuts', 'Peanuts'), ('air', 'air')], max_length=50),
        ),
    ]
