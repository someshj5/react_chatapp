# Generated by Django 2.2.3 on 2019-07-04 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_auto_20190703_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='username',
            field=models.CharField(default='username', max_length=255),
        ),
    ]
