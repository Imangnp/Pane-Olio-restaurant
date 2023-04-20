# Generated by Django 3.2.18 on 2023-04-20 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.CharField(max_length=50, unique=True)),
                ('capacity', models.IntegerField(choices=[(2, '2 People'), (3, '3 People'), (4, '4 People'), (5, '5 People')])),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='is_confirmed',
        ),
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='booking_system.table'),
        ),
    ]