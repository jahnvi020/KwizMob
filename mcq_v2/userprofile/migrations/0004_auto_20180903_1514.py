
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20180903_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
