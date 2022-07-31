from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20180904_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rem_time',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.IntegerField(),
        ),
    ]
