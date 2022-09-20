# Generated by Django 4.1 on 2022-09-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0013_alter_item_label"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[("G", "Group lesson"), ("I", "Individual lesson")],
                max_length=5,
            ),
        ),
    ]
