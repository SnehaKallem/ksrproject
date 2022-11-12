# Generated by Django 4.1 on 2022-09-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0002_feedbackdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ratings', models.IntegerField()),
                ('comments', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='feedbackdata',
        ),
    ]