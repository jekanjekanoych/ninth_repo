# Generated by Django 4.2.1 on 2023-05-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_alter_code_code_alter_number_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="code",
            name="number",
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
