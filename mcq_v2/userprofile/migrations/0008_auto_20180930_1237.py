from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20180930_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rem_time',
            field=models.IntegerField(default=1800),
        ),
    ]
