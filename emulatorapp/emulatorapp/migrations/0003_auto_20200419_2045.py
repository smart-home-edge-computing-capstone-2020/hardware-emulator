# Generated by Django 3.0.5 on 2020-04-19 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emulatorapp', '0002_auto_20200419_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hardware',
            name='function_type',
        ),
        migrations.AddField(
            model_name='hardware',
            name='hardwareType',
            field=models.CharField(choices=[('s', 'Sensor'), ('a', 'Actuator'), ('n', 'Not Set')], default='n', max_length=1),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='valueType',
            field=models.CharField(choices=[('i', 'Integer'), ('b', 'Boolean'), ('f', 'Float'), ('n', 'Not Set')], default='n', max_length=1),
        ),
    ]
