# Generated by Django 3.1.3 on 2020-11-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myems', '0002_auto_20201118_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commercial_reference', models.CharField(max_length=50)),
                ('un_code', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'dg_project',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='ib_admin',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='ib_putaway',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='ib_unstuffing',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=False,
        ),
    ]
