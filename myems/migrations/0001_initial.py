# Generated by Django 3.1.3 on 2020-11-18 01:30

from django.db import migrations, models
import django.db.models.deletion
import myems.models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='DeptEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_no', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, to='myems.department')),
            ],
            options={
                'db_table': 'dept_emp',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=1)),
                ('hire_date', models.DateField()),
                ('image', stdimage.models.StdImageField(blank=True, max_length=255, null=True, storage=myems.models.LocalFileSystemStorage(), upload_to=myems.models.upload_path_handler)),
                ('departments', models.ManyToManyField(related_name='departments', through='myems.DeptEmp', to='myems.Department')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(blank=True, null=True)),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='employeeTitles', to='myems.employee')),
            ],
            options={
                'db_table': 'titles',
            },
        ),
        migrations.AddField(
            model_name='deptemp',
            name='emp_no',
            field=models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='myems.employee'),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_amount', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='employeeSalaries', to='myems.employee')),
            ],
            options={
                'db_table': 'salaries',
                'unique_together': {('emp_no', 'from_date')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='deptemp',
            unique_together={('emp_no', 'dept_no')},
        ),
    ]
