
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz_qus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='quizze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ques', models.ManyToManyField(to='quiz_qus.question')),
            ],
        ),
    ]
