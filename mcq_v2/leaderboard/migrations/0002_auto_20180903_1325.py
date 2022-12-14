from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='attempted_qus',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='message',
            field=models.CharField(default='Congo', max_length=255),
            preserve_default=False,
        ),
    ]
