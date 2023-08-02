# Generated by Django 4.2.3 on 2023-08-01 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('house_type', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('budget_category', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('appliances_included', models.BooleanField()),
            ],
        ),
    ]
