import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentAnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy', models.FloatField(default=0.0)),
                ('text_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.textdata')),
            ],
        ),
    ]