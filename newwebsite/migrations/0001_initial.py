# Generated by Django 3.2.5 on 2021-08-09 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('ad_file', models.FileField(null=True, upload_to='ads/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_created=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('file', models.FileField(null=True, upload_to='files/')),
                ('name', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('posted_by', models.CharField(default='Godwin', max_length=30)),
                ('description', models.TextField(max_length=50000)),
                ('post_views', models.IntegerField(default=0)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newwebsite.category')),
            ],
        ),
    ]
