# Generated by Django 3.2.16 on 2023-01-14 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("journal", "0005_auto_20230114_1134"),
    ]

    operations = [
        migrations.RenameField(
            model_name="featuredcollection",
            old_name="collection",
            new_name="target",
        ),
        migrations.RemoveField(
            model_name="featuredcollection",
            name="id",
        ),
        migrations.AddField(
            model_name="featuredcollection",
            name="piece_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="journal.piece",
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="featuredcollection",
            unique_together={("owner", "target")},
        ),
    ]
