# Generated by Django 3.2.18 on 2023-04-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('antipasti', 'Antipasti'), ('main_courses', 'Main Courses'), ('dessert', 'Dessert'), ('red_wine', 'Red Wine(glass)'), ('white_wine', 'White Wine(glass)'), ('beers', 'Beers'), ('soft_drinks', 'Soft Drinks'), ('hot_drinks', 'Hot Drinks')], max_length=20)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='WineList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('red_wine', 'Red Wine'), ('white_wine', 'White Wine')], max_length=20)),
                ('description', models.TextField()),
                ('price_per_glass', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('price_per_bottle', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
