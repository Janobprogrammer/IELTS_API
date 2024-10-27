# Generated by Django 5.1 on 2024-10-27 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopicPartTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_part', models.TextField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='part2.topicparttwo')),
            ],
        ),
    ]