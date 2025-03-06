# Copyright The IETF Trust 2025, All Rights Reserved

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doc", "0026_storedobject_content_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storedobject",
            name="created",
            field=models.DateTimeField(
                help_text="Instant object first became known. May not be the same as the storage's created value for the instance. It will hold the current mtime for objects imported from oder disk storage."
            ),
        ),
        migrations.AlterField(
            model_name="storedobject",
            name="store_created",
            field=models.DateTimeField(
                help_text="The instant the name was placed in the store for the first time"
            ),
        ),
    ]
