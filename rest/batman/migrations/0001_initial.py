# Generated by Django 5.2 on 2025-04-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=200)),
                ('sname', models.CharField(max_length=200)),
                ('stamil', models.IntegerField()),
                ('senglish', models.IntegerField()),
                ('smaths', models.IntegerField()),
                ('sscience', models.IntegerField()),
                ('ssocial', models.IntegerField()),
                ('stotal', models.IntegerField(blank=True, null=True)),
                ('sgrade', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'gotham',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
