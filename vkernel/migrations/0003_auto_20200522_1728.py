# Generated by Django 3.0.5 on 2020-05-22 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vkernel', '0002_auto_20200521_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='Member',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='vkernel.Membership'),
        ),
    ]
