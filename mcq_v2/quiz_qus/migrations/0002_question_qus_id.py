from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_qus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qus_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
