# Generated by Django 5.0.4 on 2024-04-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExchangeRate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cur_unit", models.CharField(max_length=10)),
                ("deal_bas_r", models.FloatField()),
                ("search_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="GoldPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gold_type", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("closing_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="OilPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("oil_category", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("avg_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
