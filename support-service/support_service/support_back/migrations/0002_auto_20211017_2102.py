# Generated by Django 3.0.8 on 2021-10-17 21:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support_back', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Executor',
            new_name='Assistant',
        ),
        migrations.RenameModel(
            old_name='Customer',
            new_name='Client',
        ),
        migrations.RenameField(
            model_name='authoring',
            old_name='executor',
            new_name='assistant',
        ),
        migrations.RenameField(
            model_name='authoring',
            old_name='customer',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='executor',
            new_name='assistant',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='customer',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='ordering',
            old_name='executor',
            new_name='assistant',
        ),
        migrations.RenameField(
            model_name='ordering',
            old_name='customer',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='executor',
            new_name='assistant',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='executor',
            new_name='assistant',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='customer',
            new_name='client',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('1', 'Consultation'), ('2', 'Repair'), ('3', 'Troubleshooting'), ('4', 'Service maintenance'), ('5', 'I pressed something and everything broke'), ('6', 'Warranty service'), ('7', 'It’s because of you that everything doesn’t work for me')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('1', 'Consultation'), ('2', 'Repair'), ('3', 'Troubleshooting'), ('4', 'Service maintenance'), ('5', 'I pressed something and everything broke'), ('6', 'Warranty service'), ('7', 'It’s because of you that everything doesn’t work for me')], default='1', max_length=1),
        ),
    ]