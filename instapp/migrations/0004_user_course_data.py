# Generated by Django 4.1 on 2022-09-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapp', '0003_feedback_data_delete_feedbackdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_course_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]
