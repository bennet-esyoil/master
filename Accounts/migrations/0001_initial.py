# Generated by Django 3.0.4 on 2020-03-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('picture', models.CharField(default='https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500', max_length=1000)),
                ('mainContent', models.CharField(max_length=200000)),
                ('user', models.CharField(max_length=100)),
                ('date', models.CharField(default='00-00-0000', max_length=10)),
                ('url', models.CharField(default='none', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('picture', models.CharField(default='https://wikicdn.web.app/media/cat.png', max_length=1000)),
                ('description', models.CharField(default='there is nothing here', max_length=1000)),
                ('profilepicture', models.CharField(default='https://wikicdn.web.app/media/cat.png', max_length=1000)),
            ],
        ),
    ]
