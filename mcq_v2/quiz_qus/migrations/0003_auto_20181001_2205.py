from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_qus', '0002_question_qus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qus_id',
            field=models.IntegerField(unique=True),
        ),
    ]
