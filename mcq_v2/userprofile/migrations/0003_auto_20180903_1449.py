

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profile_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
