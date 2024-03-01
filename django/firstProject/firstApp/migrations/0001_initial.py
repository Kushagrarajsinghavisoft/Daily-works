# Generated by Django 5.0.2 on 2024-03-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('score', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
