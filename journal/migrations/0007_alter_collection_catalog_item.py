# Generated by Django 3.2.16 on 2023-01-17 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_initial"),
        ("journal", "0006_auto_20230114_2139"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="catalog_item",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="journal_item",
                to="catalog.collection",
            ),
        ),
    ]
