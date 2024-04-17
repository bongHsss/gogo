# Generated by Django 5.0.4 on 2024-04-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_nasdaqindex'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchangerate',
            old_name='search_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='exchangerate',
            old_name='deal_bas_r',
            new_name='rate',
        ),
        migrations.RemoveField(
            model_name='exchangerate',
            name='cur_unit',
        ),
        migrations.AddField(
            model_name='exchangerate',
            name='type',
            field=models.CharField(default='exchange_rate', max_length=10),
        ),
    ]