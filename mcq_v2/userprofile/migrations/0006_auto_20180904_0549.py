
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20180904_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='start_time',
            field=models.IntegerField(default=0),
        ),
    ]
