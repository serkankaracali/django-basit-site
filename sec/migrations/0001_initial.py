# Generated by Django 2.2 on 2019-05-29 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilk_isim', models.CharField(max_length=200)),
                ('soy_isim', models.CharField(max_length=200)),
                ('konu', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('mesaj', models.TextField(max_length=1000)),
            ],
        ),
    ]
