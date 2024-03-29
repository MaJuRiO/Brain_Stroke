# Generated by Django 4.1.4 on 2022-12-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="storage_history",
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
                ("visceral_level", models.IntegerField(blank=True, null=True)),
                ("body_fat", models.FloatField(blank=True, null=True)),
                ("basal_metabolism", models.FloatField(blank=True, null=True)),
                ("skeletal_muscle", models.FloatField(blank=True, null=True)),
                ("weight", models.FloatField(blank=True, null=True)),
                ("bmi", models.FloatField(blank=True, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("gender", models.CharField(blank=True, max_length=100, null=True)),
                ("quantity_activity", models.IntegerField(blank=True, null=True)),
                ("diet", models.CharField(blank=True, max_length=100, null=True)),
                ("high_blood", models.IntegerField(blank=True, null=True)),
                ("diabetes", models.CharField(blank=True, max_length=100, null=True)),
                ("drink", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
