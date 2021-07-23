# Generated by Django 3.1.2 on 2021-06-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2000, verbose_name='コメント')),
            ],
            options={
                'db_table': 'topic',
            },
        ),
    ]