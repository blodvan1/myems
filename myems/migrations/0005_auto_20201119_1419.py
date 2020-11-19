# Generated by Django 3.1.3 on 2020-11-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myems', '0004_auto_20201118_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dg',
            old_name='sn',
            new_name='id',
        ),
        migrations.AddField(
            model_name='dg',
            name='code_ean13',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dg',
            name='commercial_designation_in_english',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='dg',
            table='dg_gen',
        ),
    ]