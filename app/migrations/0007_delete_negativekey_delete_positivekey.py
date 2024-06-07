from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NegativeKey',
        ),
        migrations.DeleteModel(
            name='PositiveKey',
        ),
    ]