# Generated by Django 3.0.8 on 2020-10-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('salutation_type', models.IntegerField(blank=True, choices=[(1, 'Mr'), (2, 'Mrs'), (3, 'Miss')], null=True)),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'male'), (2, 'female'), (3, 'others')], null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
