# Generated by Django 3.1.1 on 2020-09-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200904_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='members/')),
                ('designation', models.CharField(choices=[('Lead', 'Lead'), ('Developer', 'Developer'), ('Designer', 'Designer'), ('Programmer', 'Programmer'), ('Management', 'Management')], max_length=20)),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('dribbleorbehance', models.URLField(blank=True)),
                ('year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=5)),
            ],
        ),
    ]
