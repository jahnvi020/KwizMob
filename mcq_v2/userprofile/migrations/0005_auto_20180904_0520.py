
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20180903_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='start_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
