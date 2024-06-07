from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0005_delete_sentimentanalysisresult_delete_textdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='NegativeKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PositiveKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField()),
            ],
        ),
    ]
