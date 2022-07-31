from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20180930_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
