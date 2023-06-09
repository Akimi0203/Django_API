# Generated by Django 4.1.7 on 2023-03-24 19:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('cpf', models.CharField(max_length=14, null=True)),
            ],
        ),
    ]
