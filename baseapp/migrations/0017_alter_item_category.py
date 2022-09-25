# Generated by Django 4.1 on 2022-09-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0016_alter_item_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[("I", "Individual lesson"), ("G", "Group lesson")],
                max_length=5,
            ),
        ),
    ]
