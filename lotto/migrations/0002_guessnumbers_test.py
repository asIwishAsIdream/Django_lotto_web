# Generated by Django 3.2 on 2023-07-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guessnumbers',
            name='test',
            field=models.CharField(default='Test', max_length=255),
        ),
    ]