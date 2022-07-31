from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizze',
            name='time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
