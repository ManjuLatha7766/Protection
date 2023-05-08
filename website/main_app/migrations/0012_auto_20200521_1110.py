# Generated by Django 3.0.6 on 2020-05-21 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20200521_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='relation',
            field=models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Husband', 'Husband'), ('Friend', 'Friend'), ('Relative', 'Relative'), ('Other', 'Other')], default='Other', max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]