from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_sentimentanalysisresult'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SentimentAnalysisResult',
        ),
        migrations.DeleteModel(
            name='TextData',
        ),
    ]
