# Generated by Django 3.0.3 on 2020-02-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubstitutionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_number', models.IntegerField()),
                ('absent_teacher', models.CharField(max_length=30)),
                ('class_tag', models.CharField(max_length=30)),
                ('subject_name', models.CharField(max_length=30)),
                ('classroom', models.CharField(max_length=30)),
                ('substitute_teacher', models.CharField(max_length=30)),
            ],
        ),
    ]
