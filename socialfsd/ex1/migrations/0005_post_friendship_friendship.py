# Generated by Django 4.1.7 on 2023-12-27 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ex1", "0004_delete_friendship"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="friendship",
            field=models.BooleanField(default=False, verbose_name="FriendShip"),
        ),
        migrations.CreateModel(
            name="Friendship",
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
                (
                    "addressee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_addressee",
                        to="ex1.user",
                    ),
                ),
                (
                    "requester",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_requester",
                        to="ex1.user",
                    ),
                ),
            ],
        ),
    ]
