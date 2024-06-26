# Generated by Django 4.2.7 on 2024-03-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EXC', models.CharField(max_length=50)),
                ('SUB', models.TextField(blank=True, choices=[('Chemistry', 'Chemistry'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics')], null=True)),
                ('QN', models.TextField(blank=True, choices=[('1', '1'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('2', '2'), ('20', '20'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], null=True)),
                ('QA', models.TextField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('NA', 'NA')], null=True)),
            ],
        ),
    ]
