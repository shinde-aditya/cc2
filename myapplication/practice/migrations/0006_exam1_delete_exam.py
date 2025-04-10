# Generated by Django 5.2 on 2025-04-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_exam_delete_exams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_no', models.IntegerField()),
                ('studentName', models.CharField(max_length=100)),
                ('physics', models.IntegerField()),
                ('chemistry', models.IntegerField()),
                ('math', models.IntegerField()),
                ('Result', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
    ]
