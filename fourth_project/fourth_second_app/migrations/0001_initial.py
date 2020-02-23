# Generated by Django 3.0.3 on 2020-02-22 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewWebpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=265)),
                ('url', models.URLField(unique=True)),
                ('new_topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fourth_second_app.NewTopic')),
            ],
        ),
    ]
