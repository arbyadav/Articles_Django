# Generated by Django 2.2.7 on 2019-11-19 06:54

import articles.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField(unique=True)),
                ('title', models.TextField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('likes', models.IntegerField(default=0)),
                ('thumbnail', models.FileField(upload_to=articles.models.get_upload_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='articles.Article')),
            ],
        ),
    ]
