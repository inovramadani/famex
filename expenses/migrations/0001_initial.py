# Generated by Django 2.1.7 on 2019-02-19 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
            ],
        ),
    ]