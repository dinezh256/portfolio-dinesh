# Generated by Django 2.1 on 2020-03-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=100, verbose_name='Stream name')),
                ('school', models.CharField(max_length=100, verbose_name='School name')),
                ('year', models.CharField(max_length=100, verbose_name='passing year')),
                ('grades', models.CharField(max_length=100, verbose_name='grades')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Education',
            },
        ),
    ]
