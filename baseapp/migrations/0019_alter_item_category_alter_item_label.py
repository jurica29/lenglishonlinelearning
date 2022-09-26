# Generated by Django 4.1 on 2022-09-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0018_remove_order_billing_address_remove_order_coupon_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[("L", "Lesson"), ("C", "Course")], max_length=5
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="label",
            field=models.CharField(
                choices=[("P", "Package of lessons"), ("S", "Single lesson")],
                max_length=5,
            ),
        ),
    ]