# Generated by Django 4.2.1 on 2023-06-30 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='totalMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.IntegerField()),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Student.studentid')),
            ],
        ),
    ]
