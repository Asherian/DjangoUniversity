# Generated by Django 3.0.7 on 2020-06-23 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('CourseNum', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('Title', models.CharField(default='', max_length=60)),
                ('Instructor', models.CharField(default='', max_length=60)),
                ('Duration', models.FloatField()),
            ],
        ),
    ]
