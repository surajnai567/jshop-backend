# Generated by Django 3.1.1 on 2020-10-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categry', models.CharField(max_length=15)),
                ('cateimg', models.ImageField(upload_to='')),
            ],
        ),
    ]
