# Generated by Django 5.0.7 on 2024-10-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
