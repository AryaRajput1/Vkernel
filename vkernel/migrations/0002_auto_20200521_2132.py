# Generated by Django 3.0.5 on 2020-05-21 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vkernel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='Member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vkernel.Membership'),
        ),
    ]
